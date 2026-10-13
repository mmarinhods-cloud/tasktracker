"""Validações das regras de negócio, sem depender do terminal."""


def validar_titulo(valor: str) -> str:
    titulo = valor.strip()
    if not titulo:
        raise ValueError("O título é obrigatório e não pode conter apenas espaços.")
    return titulo


def validar_prioridade(valor: str) -> str:
    # Media é a única grafia alternativa autorizada pelo enunciado.
    prioridades = {"Alta": "Alta", "Média": "Média", "Media": "Média", "Baixa": "Baixa"}
    prioridade = valor.strip()
    if prioridade not in prioridades:
        raise ValueError("Prioridade inválida. Use Alta, Média (ou Media) ou Baixa.")
    return prioridades[prioridade]
