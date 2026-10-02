# pokeIFRN

Projeto de exemplo da disciplina de **Programação para Internet** (IFRN).
Uma página em React que lista Pokémon consumindo a [PokeAPI](https://pokeapi.co).

Feito com [Vite](https://vite.dev) + [React](https://react.dev).

---

## Como rodar no Windows

O Node.js já está instalado nos computadores do laboratório. São três passos: **baixar → instalar dependências → rodar**.

Abra o **Prompt de Comando** (tecla `Windows`, digite `cmd`, Enter) e siga:

### 1. Baixar o projeto

Escolha uma pasta para guardar seus projetos e entre nela:

```cmd
cd %USERPROFILE%\Documents
mkdir projetos
cd projetos
```

Agora clone o repositório:

```cmd
git clone https://github.com/JefersonQueiroga/poke-ifrn.git
cd poke-ifrn
```

> Sem Git na máquina? Baixe pelo botão verde **Code → Download ZIP** no GitHub, extraia a pasta e entre nela com `cd`.

### 2. Instalar as dependências

```cmd
npm install
```

Esse comando baixa as bibliotecas (React, Vite…) para dentro da pasta `node_modules`. **Demora alguns minutos na primeira vez** e precisa de internet. Avisos amarelos (`warn`) são normais — só se preocupe com erros vermelhos.

Você só roda isso uma vez, ou quando o professor adicionar uma biblioteca nova ao projeto.

### 3. Rodar

```cmd
npm run dev
```

Vai aparecer algo assim:

```
  VITE v8.2.0  ready in 412 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
```

Abra o navegador em **http://localhost:5173** — ou segure `Ctrl` e clique no link do terminal.

Pronto. Toda vez que você salvar um arquivo (`Ctrl + S`), a página atualiza sozinha.

**Para parar o servidor:** clique no terminal e aperte `Ctrl + C`.

### 4. Abrir o código no editor

Com o terminal na pasta do projeto:

```cmd
code .
```

(O ponto significa "a pasta atual".) Ou clique com o botão direito na pasta `poke-ifrn` → **Abrir com Code**.

> Dica: o VS Code tem terminal embutido — `Ctrl + '` (Ctrl + aspas simples). Dá para rodar o `npm run dev` por ali, sem precisar do Prompt de Comando separado.
>
> Extensões que ajudam: **ES7+ React/Redux/React-Native snippets** (atalhos para criar componentes) e **ESLint** (aponta erros enquanto você digita).

---

## Estrutura do projeto

```
poke-ifrn/
├── index.html                  ponto de entrada do site
├── package.json                dependências e comandos (scripts)
├── vite.config.js              configuração do Vite
└── src/
    ├── main.jsx                liga o React ao index.html
    ├── App.jsx                 componente principal (a tela)
    ├── App.css                 estilos da tela
    ├── index.css               estilos globais
    └── components/
        ├── PokemonCard.jsx     o card de cada Pokémon
        └── PokemonCard.css     estilos do card
```

A pasta `node_modules/` **não** vai para o GitHub (está no `.gitignore`) — é pesada, e cada um gera a sua com o `npm install`.

---

## Problemas comuns

### `npm : O arquivo não pode ser carregado porque a execução de scripts foi desabilitada`

Esse erro só acontece no **PowerShell**. Duas saídas:

1. **Mais simples:** use o **Prompt de Comando (cmd)** em vez do PowerShell.
2. Ou abra o **PowerShell como Administrador** (botão direito → Executar como administrador) e rode:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Confirme com `S` e feche o PowerShell.

### `Port 5173 is already in use`

Já tem um `npm run dev` rodando em outro terminal. Feche o outro terminal, ou apenas use a porta que o Vite sugerir (ele costuma subir na 5174 sozinho).

### O `npm install` falhou / deu erro no meio

Rode `npm install` de novo — muitas vezes é só instabilidade de rede. Se continuar, apague a pasta `node_modules` e rode mais uma vez.

### A página abre mas fica em branco / sem os Pokémon

O projeto busca os dados na internet (PokeAPI). Confira sua conexão.

Vale também abrir o **DevTools** do navegador (`F12`), aba **Console**, para ver a mensagem de erro.

### `'node' não é reconhecido como um comando interno ou externo`

O terminal não está enxergando o Node. Feche **todos** os terminais e abra um novo. Se continuar, avise o professor — pode ser que a máquina precise de reinstalação do Node.

### Caminho com espaços ou acentos

Evite colocar o projeto em pastas com acentos, `ç` ou nomes muito longos (ex.: `C:\Users\João\Área de Trabalho\...`). Algumas ferramentas ainda engasgam com isso. Prefira algo como `C:\Users\SeuNome\Documents\projetos`.

---

## Fluxo do dia a dia

Depois da primeira instalação, sua rotina é só isto:

```cmd
cd %USERPROFILE%\Documents\projetos\poke-ifrn
npm run dev
```

E, quando o professor atualizar o repositório:

```cmd
git pull
npm install
npm run dev
```

---

## Links úteis

- [Documentação do React (em português)](https://pt-br.react.dev)
- [Documentação do Vite](https://vite.dev/guide/)
- [PokeAPI](https://pokeapi.co/docs/v2)
- [Repositório do projeto](https://github.com/JefersonQueiroga/poke-ifrn)
