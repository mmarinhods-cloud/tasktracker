"""Cadastro e consulta de tarefas mantidas em memória."""

if __package__:
    from .tarefa import Tarefa, criar_tarefa
    from .utils import validar_prioridade, validar_titulo
else:
    from tarefa import Tarefa, criar_tarefa
    from utils import validar_prioridade, validar_titulo


class GerenciadorTarefas:
    def __init__(self) -> None:
        self._tarefas: list[Tarefa] = []

    def cadastrar(
        self,
        titulo: str,
        descricao: str,
        responsavel: str,
        prioridade: str,
        data_limite: str,
    ) -> Tarefa:
        # Valida antes de adicionar: uma tentativa inválida não gera registro.
        titulo = validar_titulo(titulo)
        prioridade = validar_prioridade(prioridade)
        tarefa = criar_tarefa(
            len(self._tarefas) + 1,
            titulo,
            descricao.strip(),
            responsavel.strip(),
            prioridade,
            data_limite.strip(),
        )
        self._tarefas.append(tarefa)
        return tarefa.copy()

    def listar(self) -> list[Tarefa]:
        """Devolve cópias para impedir alterações acidentais nos registros."""
        return [tarefa.copy() for tarefa in self._tarefas]
