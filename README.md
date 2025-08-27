<div align="center" style="position: relative;">
   <h1 align="center">CLEAR INBOX 📬</h1>
  <p align="center">
     Organize sua caixa de entrada: identifique automaticamente e-mails produtivos e improdutivos.
  </p>

  <!-- Botões interativos -->
  <p align="center">
    <a href="https://github.com/marcelonovello/clearInbox/network/members" style="text-decoration:none;">
      <img src="https://img.shields.io/badge/👥%20Contribuidores-555555?style=for-the-badge&logo=github" />
    </a>
    <a href="https://github.com/marcelonovello/clearInbox/issues" style="text-decoration:none;">
      <img src="https://img.shields.io/badge/🐛%20Issues-4caf50?style=for-the-badge&logo=github" />
    </a>
    <a href="https://github.com/marcelonovello/clearInbox/blob/main/LICENSE" style="text-decoration:none;">
      <img src="https://img.shields.io/badge/📄%20Licença-4caf50?style=for-the-badge&logo=github" />
    </a>
  </p>

<br clear="right"> 
</div>

<details><summary>📑 Sumário</summary>

- [ Visão Geral](#-overview)
- [ Tecnologias](#-tecnologias)
- [ Funcionalidades](#-features)
- [ Estrutura do Projeto](#-project-structure)
  - [ Índice do Projeto](#-project-index)
- [ Começando](#-getting-started)
  - [ Pré-requisitos](#-prerequisites)
  - [ Instalação](#-installation)
  - [ Uso](#-usage)
  - [ Testes](#-testing)
- [ Roteiro do Projeto](#-project-roadmap)
- [ Contribuindo](#-contributing)
- [ Licença](#-license)
- [ Agradecimentos](#-acknowledgments)

</details>

---

## 🔎 Visão Geral

**Clear-In-box** é uma aplicação Python Flask que classifica automaticamente seus e-mails como **produtivos** ou **improdutivos**, ajudando você a focar no que importa e manter sua caixa de entrada organizada.</code>

---

## 🛠 Tecnologias
<p>
  <img src="https://skillicons.dev/icons?i=python,html,css" />
</p></div>

---

## ✨ Funcionalidades

- 📧 Classificação automática de e-mails<br>
- 🎨 Interface limpa e simples<br>
- ⚙️ Backend Flask com frontend em HTML/CSS<br>
- ➕ Facilmente extensível para mais funcionalidades<br>


---

## 🏗 Estrutura do Projeto

```sh
└── clearInbox/
    ├── LICENSE
    ├── README.md
    ├── app.py
    ├── requirements.txt
    ├── static
    │   └── style.css
    └── templates
        └── index.html
```


## 📂 Índice do Projeto
<details open> <summary><b>CLEARINBOX/</b></summary> <table> <tr> <td><b>
<a href='https://github.com/marcelonovello/clearInbox/blob/master/app.py'>app.py</a></b></td> <td>Ponto de entrada principal da aplicação Flask</td> </tr> <tr> <td><b>
  <a href='https://github.com/marcelonovello/clearInbox/blob/master/requirements.txt'>requirements.txt</a></b></td> <td>Dependências do Python</td> </tr> <tr> <td><b>
    <a href='https://github.com/marcelonovello/clearInbox/blob/master/templates/index.html'>index.html</a></b></td> <td>Template HTML principal</td> </tr> <tr> <td><b>
      <a href='https://github.com/marcelonovello/clearInbox/blob/master/static/style.css'>static/style.css</b></td> <td>Estilo CSS para a interface</td> </tr> </table> </details>

---
## ⚡ Começando

### 🛠 Pré-requisitos

Antes de começar com clearInbox, verifique se seu ambiente atende aos seguintes requisitos:

- **Programming Language:** Python
- **Package Manager:** Pip

## ⚙️ Instalação

Instale o clearInbox usando um dos métodos::

**Build a partir do código-fonte:**

1. Clone o repositório:
```sh
❯ git clone https://github.com/marcelonovello/clearInbox
```

2. Navegue até o diretório do projeto:
```sh
❯ cd clearInbox
```

3. Instale as dependências:

**Usando:** [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r requirements.txt
```


## 🚀 Uso
Execute o CleanInbox usando o seguinte comando:<br>

**Usando:** [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python {entrypoint}
```


### 🧪 Testes
Execute os testes usando o seguinte comando:<br>

**Usando:** [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pytest
```


---
##  🗺 Roteiro do Projetop

- [X] **`Tarefa 1`**: Funcionalidade inicial de classificação de e-mails.
- [ ] **`Tarefa 2`**: Melhorias na interface.
- [ ] **`Tarefa 3`**: Integração com serviços reais de e-mail.
- [ ] **`Tarefa 4`**: Funcionalidade inicial de classificação de e-mails.

---

## 👥 Contribuindo

- **💬 [Participe das Discussões](https://github.com/marcelonovello/clearInbox/discussions)**: Compartilhe suas ideias, forneça feedback ou faça perguntas.
- **🐛 [Reportar Problemas](https://github.com/marcelonovello/clearInbox/issues)**: Envie bugs encontrados ou registre solicitações de funcionalidades para o projeto `clearInbox`.
- **💡 [Submeta Pull Requests](https://github.com/marcelonovello/clearInbox/blob/main/CONTRIBUTING.md)**: Revise PRs abertos e envie seus próprios PRs.

<details closed>
<summary>Diretrizes para Contribuição</summary>

1. **Fork do Repositório**: Comece fazendo um fork do repositório para sua conta no GitHub.
2. **Clone Localmente**: Clone o repositório forked para sua máquina usando um cliente git.
   ```sh
   git clone https://github.com/marcelonovello/clearInbox
   ```
3. **Crie uma Nova Branch**: Sempre trabalhe em uma nova branch, dando um nome descritivo.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Faça Suas Alterações**: Desenvolva e teste suas alterações localmente.
5. **Commit das Alterações**: Faça commit com uma mensagem clara descrevendo suas atualizações.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push para o github**: Envie as alterações para seu repositório forked.
   ```sh
   git push origin new-feature-x
   ```
7. **Submeta um Pull Request**: Crie um PR contra o repositório original. Descreva claramente as mudanças e suas motivações.
8. **Revisão**: Uma vez que o PR seja revisado e aprovado, ele será mergeado na branch principal. Parabéns pela contribuição!
</details>

<details closed>
<summary>Gráfico de Contribuidores</summary>
<br>
<p align="left">
   <a href="https://github.com{/marcelonovello/clearInbox/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=marcelonovello/clearInbox">
   </a>
</p>
</details>

---

## 📄 Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.


---

## 📚 Agradecimentos

- Flask
- Icons8
- Skillicons.dev
- Inspirado em ferramentas de produtividade e automação de e-mails

---
