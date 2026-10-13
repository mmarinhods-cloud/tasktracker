"""Testes das regras e dos fluxos reais do terminal, sem pacotes externos."""

from contextlib import redirect_stdout
from datetime import datetime
from io import StringIO
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import patch

from src.gerenciador import GerenciadorTarefas
from src.main import main
from src.utils import validar_prioridade, validar_titulo


RAIZ = Path(__file__).resolve().parents[1]


class TestValidacoes(unittest.TestCase):
    def test_titulo_remove_espacos_externos(self):
        self.assertEqual(validar_titulo("  Revisar código  "), "Revisar código")

    def test_titulo_rejeita_vazio_e_apenas_espacos(self):
        for titulo in ("", " ", "   ", "\t\n"):
            with self.subTest(titulo=titulo), self.assertRaises(ValueError):
                validar_titulo(titulo)

    def test_prioridades_permitidas_e_grafia_media(self):
        for entrada, esperado in (
            ("Alta", "Alta"), ("Média", "Média"),
            ("Media", "Média"), ("Baixa", "Baixa"), (" Media ", "Média"),
        ):
            with self.subTest(entrada=entrada):
                self.assertEqual(validar_prioridade(entrada), esperado)

    def test_prioridades_fora_do_padrao_sao_rejeitadas(self):
        for prioridade in ("", " ", "Urgente", "1", "alta", "ALTA", "media", "Normal"):
            with self.subTest(prioridade=prioridade), self.assertRaises(ValueError):
                validar_prioridade(prioridade)


class TestGerenciador(unittest.TestCase):
    def setUp(self):
        self.gerenciador = GerenciadorTarefas()

    def cadastrar(self, **alteracoes):
        dados = dict(
            titulo="  Revisar código  ", descricao="  Conferir regras  ",
            responsavel=" Matheus ", prioridade="Media", data_limite=" 20/10/2026 ",
        )
        dados.update(alteracoes)
        return self.gerenciador.cadastrar(**dados)

    def test_lista_inicial_vazia(self):
        self.assertEqual(self.gerenciador.listar(), [])

    def test_cadastro_preserva_campos_e_define_status(self):
        tarefa = self.cadastrar()
        self.assertEqual(tarefa["id"], 1)
        self.assertEqual(tarefa["titulo"], "Revisar código")
        self.assertEqual(tarefa["descricao"], "Conferir regras")
        self.assertEqual(tarefa["responsavel"], "Matheus")
        self.assertEqual(tarefa["prioridade"], "Média")
        self.assertEqual(tarefa["data_limite"], "20/10/2026")
        self.assertEqual(tarefa["status"], "Pendente")
        datetime.fromisoformat(tarefa["data_criacao"])
        self.assertEqual(self.gerenciador.listar(), [tarefa])

    def test_cadastro_invalido_nao_insere_nem_consume_id(self):
        for dados in ({"titulo": "   "}, {"prioridade": "Urgente"}):
            with self.subTest(dados=dados), self.assertRaises(ValueError):
                self.cadastrar(**dados)
        self.assertEqual(self.gerenciador.listar(), [])
        self.assertEqual(self.cadastrar()["id"], 1)

    def test_titulos_iguais_tem_ids_distintos_e_ordem_de_cadastro(self):
        self.cadastrar()
        self.cadastrar()
        self.assertEqual([t["id"] for t in self.gerenciador.listar()], [1, 2])

    def test_opcionais_vazios_e_prazo_livre(self):
        tarefa = self.cadastrar(descricao="", responsavel="", data_limite="")
        for campo in ("descricao", "responsavel", "data_limite"):
            self.assertEqual(tarefa[campo], "")
        self.assertEqual(self.cadastrar(data_limite="próxima semana")["data_limite"],
                         "próxima semana")

    def test_copias_de_consulta_nao_alteram_registros(self):
        tarefa = self.cadastrar()
        tarefa["titulo"] = "Alterado externamente"
        lista = self.gerenciador.listar()
        lista[0]["status"] = "Concluída"
        lista.clear()
        registro = self.gerenciador.listar()[0]
        self.assertEqual(registro["titulo"], "Revisar código")
        self.assertEqual(registro["status"], "Pendente")

    def test_sessoes_sao_independentes(self):
        self.cadastrar()
        self.assertEqual(GerenciadorTarefas().listar(), [])


class TestTerminal(unittest.TestCase):
    def rodar(self, linhas, como_modulo=False):
        comando = [sys.executable, "-m", "src.main"] if como_modulo else [
            sys.executable, str(RAIZ / "src" / "main.py")
        ]
        resultado = subprocess.run(
            comando, input="\n".join(linhas) + "\n", text=True,
            capture_output=True, cwd=RAIZ, timeout=5,
        )
        self.assertEqual(resultado.returncode, 0, resultado.stderr)
        self.assertEqual(resultado.stderr, "")
        return resultado.stdout

    def test_lista_vazia_menu_invalido_e_saida(self):
        saida = self.rodar(["2", "abc", "", "9", "3"])
        self.assertIn("Nenhuma tarefa cadastrada.", saida)
        self.assertEqual(saida.count("Opção inválida."), 3)
        self.assertIn("Até logo!", saida)

    def test_fluxo_com_erros_cadastro_e_todos_os_campos(self):
        saida = self.rodar([
            "1", "", "   ", "Entregar etapa 2", "Implementar TaskTracker",
            "Matheus", "Urgente", "media", "Media", "20/10/2026", "2", "3",
        ])
        self.assertEqual(saida.count("O título é obrigatório"), 2)
        self.assertEqual(saida.count("Prioridade inválida."), 2)
        self.assertEqual(saida.count("Tarefa cadastrada com sucesso."), 1)
        for campo in (
            "Tarefa #1", "Título: Entregar etapa 2",
            "Descrição: Implementar TaskTracker", "Responsável: Matheus",
            "Prioridade: Média", "Data limite: 20/10/2026", "Status: Pendente",
            "Data de criação:",
        ):
            self.assertIn(campo, saida)

    def test_lista_todas_as_tarefas_na_mesma_sessao(self):
        saida = self.rodar([
            "1", "Primeira", "", "", "Alta", "", "1", "Segunda", "", "",
            "Baixa", "próxima semana", "2", "3",
        ])
        self.assertEqual(saida.count("Tarefa cadastrada com sucesso."), 2)
        self.assertIn("Tarefa #1", saida)
        self.assertIn("Tarefa #2", saida)
        self.assertIn("Título: Primeira", saida)
        self.assertIn("Título: Segunda", saida)
        self.assertEqual(saida.count("Status: Pendente"), 2)

    def test_campos_opcionais_vazios_na_listagem(self):
        saida = self.rodar(["1", "Teste", "", "", "Alta", "", "2", "3"])
        self.assertIn("Descrição: Não informada", saida)
        self.assertIn("Responsável: Não informado", saida)
        self.assertIn("Data limite: Não informada", saida)

    def test_fim_da_entrada_nao_salva_cadastro_incompleto(self):
        saida = self.rodar(["1", "Cadastro interrompido"])
        self.assertIn("Entrada interrompida.", saida)
        self.assertNotIn("Tarefa cadastrada com sucesso.", saida)

    def test_execucao_como_modulo(self):
        self.assertIn("Até logo!", self.rodar(["3"], como_modulo=True))

    def test_ctrl_c_encerra_sem_traceback(self):
        captura = StringIO()
        with patch("src.main.executar", side_effect=KeyboardInterrupt):
            with redirect_stdout(captura):
                main()
        self.assertIn("Entrada interrompida.", captura.getvalue())


if __name__ == "__main__":
    unittest.main()
