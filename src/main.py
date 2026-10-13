"""Interface de terminal do TaskTracker. Execute: python3 src/main.py."""

from typing import Callable

if __package__:
    from .gerenciador import GerenciadorTarefas
    from .utils import validar_prioridade, validar_titulo
else:
    from gerenciador import GerenciadorTarefas
    from utils import validar_prioridade, validar_titulo


def exibir_menu() -> None:
    print("\n=== TaskTracker ===")
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Sair da aplicação")


def ler_valor_validado(mensagem: str, validador: Callable[[str], str]) -> str:
    """Repete somente o campo inválido, preservando os demais dados digitados."""
    while True:
        try:
            return validador(input(mensagem))
        except ValueError as erro:
            print(f"Erro: {erro}")


def cadastrar_tarefa(gerenciador: GerenciadorTarefas) -> None:
    print("\n--- Cadastro de tarefa ---")
    titulo = ler_valor_validado("Título: ", validar_titulo)
    descricao = input("Descrição (opcional): ")
    responsavel = input("Responsável (opcional): ")
    prioridade = ler_valor_validado(
        "Prioridade (Alta, Média/Media ou Baixa): ", validar_prioridade
    )
    data_limite = input("Data limite (opcional, ex.: DD/MM/AAAA): ")
    gerenciador.cadastrar(titulo, descricao, responsavel, prioridade, data_limite)
    print("Tarefa cadastrada com sucesso.")


def listar_tarefas(gerenciador: GerenciadorTarefas) -> None:
    tarefas = gerenciador.listar()
    if not tarefas:
        print("\nNenhuma tarefa cadastrada.")
        return

    print("\n--- Tarefas cadastradas ---")
    for tarefa in tarefas:
        print(f"\nTarefa #{tarefa['id']}")
        print(f"Título: {tarefa['titulo']}")
        print(f"Descrição: {tarefa['descricao'] or 'Não informada'}")
        print(f"Responsável: {tarefa['responsavel'] or 'Não informado'}")
        print(f"Prioridade: {tarefa['prioridade']}")
        print(f"Data limite: {tarefa['data_limite'] or 'Não informada'}")
        print(f"Status: {tarefa['status']}")
        print(f"Data de criação: {tarefa['data_criacao']}")


def executar() -> None:
    gerenciador = GerenciadorTarefas()
    print("Bem-vindo ao TaskTracker!")
    print("As tarefas ficam em memória e serão perdidas ao sair.")
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            cadastrar_tarefa(gerenciador)
        elif opcao == "2":
            listar_tarefas(gerenciador)
        elif opcao == "3":
            print("Encerrando o TaskTracker. Até logo!")
            break
        else:
            print("Opção inválida. Escolha 1, 2 ou 3.")


def main() -> None:
    try:
        executar()
    except (EOFError, KeyboardInterrupt):
        print("\nEntrada interrompida. Encerrando o TaskTracker.")


if __name__ == "__main__":
    main()
