# Publicação no GitHub

O projeto já possui um repositório Git local, a branch `main` e commits separados.
Não execute `git init` novamente e não apague a pasta `.git`: ela guarda o histórico.
Até a preparação desta versão, nenhum remoto foi configurado e nenhum push foi feito.

## 1. Criar o repositório remoto

Entre na sua conta do GitHub e crie um novo repositório:

- Nome: `tasktracker`.
- Descrição sugerida: `Gerenciador de tarefas em Python - Bootcamp II CEUB`.
- Visibilidade: Público facilita a avaliação por link.
- Crie o repositório **vazio**, sem README, `.gitignore` ou licença automáticos,
  pois os arquivos e o histórico já existem localmente.

## 2. Conferir o projeto local

No terminal Linux, use a pasta do projeto:

```bash
cd "/home/th/Documents/Cursos/Bootcamp CEUB/tasktracker-projeto"
git status
git log --oneline --reverse
python3 -m unittest discover -s tests -v
```

O status esperado é uma árvore de trabalho limpa. O histórico deve mostrar as
etapas de estrutura, menu/cadastro/listagem, validações, testes e documentação.

## 3. Vincular e enviar

Substitua `SEU_USUARIO` pelo seu usuário do GitHub antes de executar:

```bash
git remote add origin https://github.com/SEU_USUARIO/tasktracker.git
git push -u origin main
```

Use a URL real exibida pelo GitHub se escolher outro nome para o repositório.
O envio depende da autenticação da sua conta no computador.

Se `origin` já tiver sido adicionado, confira a URL com `git remote -v`.
Se ela estiver errada, ajuste antes do push:

```bash
git remote set-url origin https://github.com/SEU_USUARIO/tasktracker.git
```

## 4. Conferir a entrega publicada

- Abra a página do repositório e confira o README renderizado.
- Abra `src/main.py` e confira os demais módulos e `tests/`.
- Abra `docs/planejamento_logico.pdf` e confirme que o documento aparece.
- Abra o histórico de commits da branch `main`.
- Confirme que `__pycache__/` e ambientes virtuais não foram publicados.
- Abra o link sem estar conectado à conta para verificar o acesso do avaliador.

O push envia os commits já existentes; não é necessário recriar o histórico na
interface do GitHub nem enviar cada arquivo manualmente.

## Alterações futuras

Após modificar um arquivo, verifique o que será registrado:

```bash
git status
git diff
git add CAMINHO_DO_ARQUIVO
git commit -m "docs: atualiza instrucoes de entrega"
git push
```

`CAMINHO_DO_ARQUIVO` é um marcador: substitua pelo arquivo realmente alterado.
Escolha uma mensagem que descreva a mudança realizada. A pasta `.git` deve
continuar junto do projeto quando ele for movido ou copiado para outro computador.
