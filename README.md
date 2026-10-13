# TaskTracker

Projeto acadêmico de gerenciamento de tarefas para o Bootcamp II do CEUB.

**Estudante:** Matheus Santos Marinho de Souza  
**Curso:** Ciência da Computação - Asa Norte, matutino

Aplicação de terminal para cadastrar e visualizar tarefas, reduzindo a perda de
informações na organização das atividades. Esta versão implementa o escopo da
etapa intermediária: menu contínuo, regras de negócio e controle de versão.

## Funcionalidades

- Cadastrar título, descrição, responsável, prioridade e data limite.
- Rejeitar título vazio ou composto apenas por espaços, repetindo a pergunta.
- Aceitar somente `Alta`, `Média`, `Media` ou `Baixa` na prioridade.
- Converter `Media` para `Média` na tarefa salva.
- Atribuir automaticamente identificador, data de criação e status `Pendente`.
- Listar todas as propriedades das tarefas, na ordem de cadastro.
- Informar quando nenhuma tarefa estiver cadastrada.
- Tratar opções de menu inválidas e encerrar com a opção `3`.

**Armazenamento:** as tarefas ficam apenas na memória da execução atual.
Ao sair, elas são perdidas. Persistência em arquivo ou banco é uma evolução futura.

## Tecnologias e instalação

Python 3.10 ou superior, biblioteca padrão do Python, Git e GitHub.
Não é necessário instalar pacotes com `pip`; `requirements.txt` documenta isso.

Com o projeto baixado, abra um terminal na pasta `tasktracker-projeto`:

```bash
python3 --version
python3 src/main.py
```

No Windows, se o comando `python3` não existir, utilize `py src/main.py`.
Também é possível executar `python3 -m src.main` a partir da raiz do projeto.

## Uso

```text
=== TaskTracker ===
1. Cadastrar nova tarefa
2. Visualizar tarefas cadastradas
3. Sair da aplicação
```

Exemplo de cadastro: título `Entregar etapa 2`, descrição `Revisar o projeto`,
responsável `Matheus`, prioridade `Alta` e data limite `20/10/2026`.
A data é apenas um exemplo; não representa o prazo oficial da atividade.
Depois do cadastro, escolha `2` para visualizar a tarefa com status `Pendente`.

O título é obrigatório. Descrição, responsável e data limite podem ficar vazios.
O prazo aceita texto livre ou `DD/MM/AAAA`, conforme permitido no enunciado;
esta versão não verifica se a data existe no calendário.
Espaços externos são removidos. A prioridade exige as grafias indicadas no menu:
`alta`, `ALTA`, `Urgente` e números são rejeitados. Não há seleção manual de status.

## Estrutura

```text
tasktracker-projeto/
├── .gitignore
├── README.md
├── requirements.txt
├── docs/
│   ├── planejamento_logico.pdf
│   ├── analise_etapa_2.md
│   ├── publicar_github.md
│   └── roteiro_video.md
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── tarefa.py
│   ├── gerenciador.py
│   └── utils.py
└── tests/
    └── test_tasktracker.py
```

`main.py` contém o menu, a interação de cadastro/listagem e a repetição dos campos
inválidos. `gerenciador.py` mantém a lista e valida os dados antes do cadastro.
`tarefa.py` representa cada tarefa como dicionário. `utils.py` reúne as validações.
O fluxo é: usuário → menu → gerenciador → validações/modelo → resultado no terminal.

Os arquivos obrigatórios da etapa 2 estão presentes. Os módulos adicionais e os
testes preservam a organização prevista na etapa 1. O PDF original foi copiado
sem alterações para o nome `docs/planejamento_logico.pdf` exigido nesta etapa.

## Validação

Execute na raiz do projeto:

```bash
python3 -m unittest discover -s tests -v
```

São 18 testes automatizados, incluindo entradas inválidas, ausência de registros
parciais, normalização de `Media`, status inicial, múltiplas tarefas, listagem
completa e execução real da CLI. O encerramento com fim da entrada e `Ctrl+C`
também é verificado. Para uma demonstração manual, veja o roteiro de vídeo.

## Versionamento e entrega

O repositório local usa a branch `main` e registra separadamente estrutura,
funcionalidades, validações, testes e documentação. Para visualizar a evolução:

```bash
git log --oneline --reverse
git status
```

- [Análise dos documentos e decisões de escopo](docs/analise_etapa_2.md)
- [Como publicar este histórico no GitHub](docs/publicar_github.md)
- [Roteiro de apresentação de cinco minutos](docs/roteiro_video.md)
- [Planejamento original da etapa 1](docs/planejamento_logico.pdf)

**Pendências externas:** criar o repositório no GitHub e publicar com `git push`;
gravar e publicar o vídeo; entregar os links no ambiente da disciplina.
O repositório remoto e o vídeo desta etapa ainda não foram publicados.

## Continuidade

O planejamento inicial inclui editar, excluir e alterar status. Essas funções
ficam registradas para evolução; nesta entrega o menu segue as três opções
expressamente solicitadas na etapa 2. A etapa 3 prevê empacotamento, Docker,
testes e deploy, conforme o enunciado intermediário.
