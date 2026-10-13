"""Representação de uma tarefa como dicionário."""

from datetime import datetime
from typing import TypedDict


class Tarefa(TypedDict):
    id: int
    titulo: str
    descricao: str
    responsavel: str
    prioridade: str
    data_limite: str
    status: str
    data_criacao: str


def criar_tarefa(
    identificador: int,
    titulo: str,
    descricao: str,
    responsavel: str,
    prioridade: str,
    data_limite: str,
) -> Tarefa:
    """Monta a tarefa; o gerenciador fornece os dados já tratados."""
    return {
        "id": identificador,
        "titulo": titulo,
        "descricao": descricao,
        "responsavel": responsavel,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente",
        "data_criacao": datetime.now().isoformat(timespec="seconds"),
    }
