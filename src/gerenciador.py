"""Cadastro e consulta de tarefas mantidas em memória."""

if __package__:
    from .tarefa import Tarefa, criar_tarefa
else:
    from tarefa import Tarefa, criar_tarefa


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
        tarefa = criar_tarefa(
            len(self._tarefas) + 1,
            titulo.strip(),
            descricao.strip(),
            responsavel.strip(),
            prioridade.strip(),
            data_limite.strip(),
        )
        self._tarefas.append(tarefa)
        return tarefa.copy()

    def listar(self) -> list[Tarefa]:
        """Devolve cópias para impedir alterações acidentais nos registros."""
        return [tarefa.copy() for tarefa in self._tarefas]
