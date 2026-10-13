# Análise geral e implementação da etapa 2

## Documentos analisados

1. **Enunciado - Etapa Inicial - Bootcamp II.pdf**, 14 páginas: orienta a
   decomposição do problema, entradas e saídas, regras, algoritmo em português,
   arquitetura para Git/GitHub e apresentação em vídeo.
2. **Planejamento lógico TaskTracker - Matheus santos marinho de souza.pdf**,
   14 páginas: trabalho produzido na etapa 1, preservado neste repositório em
   [planejamento_logico.pdf](planejamento_logico.pdf).
3. **Desafio Etapa Intermediária Bootcamp II-1.pdf**, 5 páginas: define a aplicação
   CLI em Python, a estrutura obrigatória, a progressão dos commits, a publicação
   no GitHub e o vídeo de cinco minutos.

Os enunciados originais permanecem na pasta acima do projeto. Não foram alterados.

## Avaliação do planejamento existente

O documento identifica o estudante, o problema de organização de tarefas e a
solução proposta. Separa entradas, saídas e regras, descreve os fluxos de cadastro
e listagem e define módulos com responsabilidades claras. Esses elementos
oferecem uma base suficiente para implementar o núcleo da segunda etapa.

O planejamento também propõe responsável, identificador, datas, alteração de
status, edição e exclusão. Ele é mais amplo do que o mínimo pedido agora.
Não há necessidade de implementar interface web, login, equipes ou banco de dados
para satisfazer o escopo explícito da etapa intermediária.

Há divergências a resolver de forma documentada:

| Ponto | Planejamento da etapa 1 | Enunciado da etapa 2 | Decisão nesta versão |
| --- | --- | --- | --- |
| Menu | Seis operações, incluindo manutenção | Cadastro, visualização e sair | Usar as três opções expressas da etapa 2 |
| Organização | `main.py`, `tarefa.py`, `gerenciador.py`, `utils.py`, testes | Árvore mínima com `src/main.py` | Manter os módulos planejados, além de todos os arquivos obrigatórios |
| PDF | Nome sugerido com hífen | `docs/planejamento_logico.pdf` | Usar o nome exigido agora, preservando o conteúdo original |
| Prioridade | Alta, Média e Baixa | Também permite `Media` | Aceitar as quatro grafias, salvando `Media` como `Média` |
| Prazo | Opcional | Texto livre ou DD/MM/AAAA | Armazenar texto opcional, sem validação de calendário |
| Status | Prevê estados e mudanças | Cadastro sempre como Pendente | Definir automaticamente Pendente, sem opção de alteração nesta versão |

A decisão sobre o menu prioriza a instrução específica da etapa atual. O barema
também menciona fidelidade ao algoritmo da etapa 1; por isso as diferenças ficam
explícitas, e os fluxos de cadastro/listagem e a separação em módulos foram
preservados. Se o professor exigir todo o escopo adicional da etapa 1, será
necessário ampliar o menu posteriormente. Esta análise não substitui uma
confirmação do professor sobre esse ponto de interpretação.

## Correspondência entre requisitos e implementação

| Requisito | Implementação / evidência |
| --- | --- |
| Menu contínuo com três opções | `src/main.py`, funções `exibir_menu` e `executar` |
| Título obrigatório e nova tentativa | `validar_titulo` em `utils.py` e `ler_valor_validado` em `main.py` |
| Prioridade estrita e nova tentativa | `validar_prioridade` e o mesmo laço de leitura |
| Dados da tarefa em objeto/dicionário | `Tarefa`, um `TypedDict`; os registros em execução são dicionários |
| Status inicial Pendente | Atribuído por `criar_tarefa` em `tarefa.py` |
| Lista de tarefas em memória | `GerenciadorTarefas` em `gerenciador.py` |
| Lista vazia e exibição de todas as propriedades | `listar_tarefas` em `main.py` |
| Organização da etapa 1 | Módulos, `requirements.txt`, `docs/` e `tests/` preservados |
| README e arquivos ignorados | `README.md` e `.gitignore` |
| Planejamento cumulativo | Cópia integral em `docs/planejamento_logico.pdf` |
| Histórico de evolução | Commits separados de estrutura, funcionalidade, validação, testes e documentação |
| Publicação remota | Pendente; instruções em `publicar_github.md` |
| Vídeo de cinco minutos | Gravação pendente; preparação em `roteiro_video.md` |

Além dos cinco campos obrigatórios, a aplicação registra responsável, identificador
e data de criação, mantendo parte dos dados previstos no planejamento. Esses
campos também aparecem na listagem. O responsável é opcional.

A validação ocorre na leitura para repetir o campo inválido e também no
gerenciador para impedir registros inválidos quando chamado por outro código.
Um cadastro interrompido antes da última resposta não é adicionado à lista.
Não existe persistência entre execuções nesta versão.

## Avaliação da etapa intermediária

O barema distribui **15,0 pontos** em:

- **4,0:** estrutura Git/GitHub, arquivos exigidos e múltiplos commits coerentes.
- **6,0:** funcionamento do Python, validações e exibição das tarefas.
- **5,0:** vídeo com requisitos técnicos e explicação do GitHub e do terminal.

O código local e a documentação estão preparados, mas a entrega acadêmica ainda
depende da publicação remota e do vídeo. Os testes não asseguram uma nota; eles
verificam o comportamento do programa frente aos requisitos implementados.

## Atenção ao vídeo

No final do planejamento há a observação de que o estudante não possui webcam.
O enunciado atual exige rosto visível durante a explicação, webcam ligada e voz
própria sem IA generativa. Portanto, será necessário providenciar câmera antes
da gravação. Uma câmera disponível ou um celular usado como webcam pode resolver
isso, desde que a gravação resultante cumpra a exigência de rosto e tela visíveis.

O vídeo deve ter cinco minutos, proporção horizontal 16:9, publicação no YouTube
como Público ou Não Listado e link acessível. O link antigo do planejamento
corresponde à etapa 1 e não comprova a apresentação da implementação atual.
Não foi feita verificação do conteúdo ou da disponibilidade desse vídeo antigo.

Os tempos sugeridos no enunciado da etapa 2 somam **4min30s**, apesar da duração
exigida de cinco minutos. O roteiro preparado acrescenta 30 segundos para
explicar a organização do código e completa 5min.

## Verificação e próximos passos

A execução de `python3 -m unittest discover -s tests -v` passou nos **18 testes**.
Há testes das regras, do gerenciador e de fluxos reais do programa via subprocesso,
incluindo erros repetidos, cadastro completo, múltiplas tarefas e encerramento.
O PDF copiado foi comparado ao original para confirmar a preservação dos bytes.

1. Executar o programa pessoalmente e compreender o fluxo entre os módulos.
2. Criar um repositório vazio chamado `tasktracker` no GitHub.
3. Vincular `origin` e enviar a branch `main`, preservando os commits existentes.
4. Conferir no GitHub a árvore, o PDF, o README e o histórico.
5. Ensaiar e gravar a demonstração com rosto visível e voz própria.
6. Publicar o vídeo e conferir acesso aos dois links antes de entregar.

O documento intermediário não informa prazo de entrega nem detalha o formulário
de submissão no AVA. Esses dados devem ser consultados no ambiente da disciplina.
Docker e deploy ficam para a etapa 3.
