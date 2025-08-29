<div align="center" style="position: relative;">
   <h1 align="center">CLEAR INBOX 📬</h1>
  <p align="center">
     Uma ferramenta inteligente de gestão de emails que classifica automaticamente suas mensagens como produtivas ou improdutivas, ajudando você a focar no que realmente importa e manter sua caixa de entrada organizada.
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

## 🔎 Visão Geral

O **Clear Inbox** é uma API inteligente para classificação automática de emails. Utiliza um modelo de Machine Learning para distinguir entre mensagens de suporte/solicitações e mensagens comuns, ajudando na triagem e organização automática da caixa de entrada

## 🛠 Tecnologias
<p>
  <img src="https://skillicons.dev/icons?i=python,html,css" />
</p></div>

## 📑 Sumário

- 📖 [Visão Geral](#-visão-geral)
- 🛠 [Tecnologias](#-tecnologias)
- ✨ [Funcionalidades](#-funcionalidades)
- 🏗 [Estrutura do Projeto](#-estrutura-do-projeto)
- 🚀 [Começando](#-começando)
  - 🛠 [Pré-requisitos](#-pré-requisitos)
  - ⚙️ [Instalação](#-instalação)
  - 🚀 [Uso](#-uso)
  - 🧪 [Testes](#-testes)
  	- 🔧 [Resolução de Problemas](#-resolução-de-Problemas)
- 🗺 [Roteiro do Projeto](#-roteiro-do-projeto)
- 👥 [Contribuindo](#-contribuindo)
- 📄 [Licença](#-licença)
- 📚 [Agradecimentos](#-agradecimentos)

---

## ✨ Funcionalidades

- 📧 Classificação automática de e-mails<br>
- 🎨 Interface limpa e simples<br>
- ⚙️ Backend Flask com frontend em HTML/CSS<br>
- ➕ Facilmente extensível para mais funcionalidades<br>

---

## 🏗 Estrutura do Projeto

```sh
└── 📦 clearInbox/
    ├── 📄 LICENSE
    ├── 📄 README.md
    ├── 📄 app.py
    ├── 📄 requirements.txt
    ├── 📂 static
    │   └── 📄 style.css
    └── 📂 templates
        └── 📄 index.html
```

---
## ⚡ Começando

### 🛠 Pré-requisitos

Antes de começar com clearInbox, verifique se seu ambiente atende aos seguintes requisitos:

- [<img align="center" src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white" />](https://www.python.org/)

## ⚙️ Instalação

Instale o clearInbox usando um dos métodos::

**Build a partir do código-fonte:**

1. Clone o repositório:
```sh
git clone https://github.com/marcelonovello/clearInbox
```

2. Navegue até o diretório do projeto:
```sh
cd clearInbox
```

3. Instale as dependências:
```sh
pip install -r requirements.txt
```

## 🚀 Uso
Execute o CleanInbox usando o seguinte comando:<br>
```sh
py app.py
```

## 🧪 Testes
Execute os testes usando o seguinte comando:<br>

```sh
pytest
```

## 🔧 Resolução de Problemas
🚫 Erros de Autenticação:
```bash
# Verifique se as credenciais do Gmail estão corretas
# Certifique-se que a autenticação de 2 fatores está desativada
# Gere uma senha específica para aplicativos se necessário
```

📧 Limite de Requisições da API
```bash
# Aumente o intervalo entre operações
python clear_inbox.py --delay 2

# Execute em horários de menor movimento
# Divida as operações em lotes menores
```

🌐 Problemas de Conexão
```bash
# Verifique sua conexão com a internet
# Use modo verboso para diagnóstico
python clear_inbox.py --verbose

# Tente uma rede diferente
# Aumente as configurações de timeout
```

🔍 E-mails Não Encontrados
```bash
# Teste critérios de busca com dry-run
python clear_inbox.py --dry-run --verbose

# Ajuste filtros de data se necessário
# Verifique permissões da conta de e-mail
```

⚡ Erros Inesperados
```bash
# Sempre teste com dry-run primeiro
python clear_inbox.py --dry-run

# Limite o escopo com max-emails
python clear_inbox.py --max-emails 100

# Verifique logs detalhados
python clear_inbox.py --verbose
```

🛡️ Medidas de Segurança
```bash
# Sempre teste primeiro com dry-run
python clear_inbox.py --dry-run --verbose

# Comece com pequenos lotes
python clear_inbox.py --max-emails 50

# Use intervalos maiores inicialmente
python clear_inbox.py --delay 3
```

📋 Para Contas Grandes (>50 mil e-mails)
```bash
# Recomendações
# Processe por intervalos de data
python clear_inbox.py --after-date 2023-01-01 --before-date 2023-06-30

# Use lotes menores com pausas
python clear_inbox.py --max-emails 1000 && sleep 300
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

- ⚗️ Flask
- 🎨 Icons8
- 🖼️ Skillicons.dev
- 📧 Inspirado em ferramentas de produtividade e automação de e-mails

---
