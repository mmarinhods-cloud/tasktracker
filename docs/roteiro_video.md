# Roteiro de apresentação - 5 minutos

Use este material como guia para ensaiar e explique com suas próprias palavras.
A apresentação deve usar seu rosto visível e sua voz, sem narração por IA.

## Preparação

- Grave no formato horizontal 16:9, com tela e rosto visíveis durante a explicação.
- Providencie uma câmera; se necessário, use um celular como webcam.
- Confira áudio, enquadramento e legibilidade do terminal antes de gravar.
- Publique o repositório antes de gravar a parte que mostra o GitHub.
- Abra a página do repositório, o histórico de commits e um terminal na raiz do projeto.
- Deixe o código acessível para mostrar as funções principais.

O enunciado sugere blocos que totalizam 4min30s. O bloco de organização do código
abaixo completa os 30 segundos restantes, atingindo os cinco minutos pedidos.

## 00:00 a 00:30 - Identificação e contexto

Apresente seu nome completo, Matheus Santos Marinho de Souza, o curso de Ciência
da Computação e o polo Asa Norte. Explique o problema: organizar e acompanhar
tarefas. Diga que esta é a etapa 2, que transforma o planejamento em uma aplicação
de terminal em Python com versionamento Git.

## 00:30 a 02:00 - Repositório no GitHub

Mostre, na página já publicada:

1. O nome do repositório e o README: objetivo, tecnologias e comando de execução.
2. `src/main.py`, os módulos auxiliares, `tests/` e `.gitignore`.
3. `docs/planejamento_logico.pdf`, ligando o planejamento à implementação.
4. O histórico: estrutura inicial, funcionamento, validações, testes e documentação.

Explique o papel de um commit como registro de uma etapa do desenvolvimento.
Diferencie o repositório local Git da cópia remota no GitHub.

## 02:00 a 04:00 - Demonstração prática

No terminal, execute:

```bash
python3 src/main.py
```

Siga esta sequência, digitando uma resposta de cada vez:

| Ação / campo | Resposta | O que mostrar |
| --- | --- | --- |
| Menu inicial | `2` | Mensagem de lista vazia |
| Menu | `9` | Erro de opção inválida e retorno ao menu |
| Menu | `1` | Início do cadastro |
| Título | Pressione Enter sem digitar | Erro de título obrigatório e repetição |
| Título, segunda tentativa | Digite três espaços e pressione Enter | Espaços também são rejeitados |
| Título válido | `Entregar etapa 2` | Continuidade do cadastro |
| Descrição | `Revisar o TaskTracker` | Campo livre |
| Responsável | `Matheus` | Dado previsto na etapa 1 |
| Prioridade inválida | `Urgente` | Erro e repetição do mesmo campo |
| Prioridade válida | `Media` | Grafia permitida, armazenada como Média |
| Data limite | `20/10/2026` | Exemplo de prazo, sem relação com a data oficial da entrega |
| Menu após sucesso | `2` | Todos os campos, identificador, data de criação e status Pendente |
| Menu | `3` | Encerramento |

Explique que o status inicial é automático, que o cadastro só é adicionado
depois de todas as respostas e que as tarefas ficam na memória durante a execução.

## 04:00 a 04:30 - Organização do código

Mostre rapidamente:

- O `while True` de `executar` e as opções do menu em `main.py`.
- `ler_valor_validado` e os validadores em `utils.py`.
- A lista em `gerenciador.py` e o dicionário em `tarefa.py`.

Explique que os módulos seguem a organização planejada. Se houver tempo,
mostre o resultado dos 18 testes já executados. Priorize explicar o funcionamento
em vez de ler o código linha a linha.

## 04:30 a 05:00 - Encerramento

Retome o que foi demonstrado: aplicação funcionando, regras validadas e histórico
publicado. Explique que o menu segue as três opções da etapa atual e que as
funções adicionais do planejamento podem ser desenvolvidas depois.
Mencione que a próxima etapa prevê empacotamento e Docker.

## Conferência depois da gravação

- O vídeo tem cinco minutos e está em 16:9 horizontal.
- Seu rosto aparece durante a explicação e a voz é sua, clara e audível.
- O terminal mostra erro de validação, cadastro bem-sucedido e listagem.
- O GitHub mostra estrutura, README e histórico de commits.
- A publicação no YouTube está como Público ou Não Listado, sem formato Shorts.
- O link abre sem exigir acesso à sua conta.
- Os links do repositório e deste vídeo foram colocados nos campos de entrega
  solicitados no AVA. Consulte ali o prazo e o formato de submissão.
