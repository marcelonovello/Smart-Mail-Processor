<div align="left" style="position: relative;">
  <img src="https://img.icons8.com/external-tal-revivo-regular-tal-revivo/96/external-readme-is-a-easy-to-build-a-developer-hub-that-adapts-to-the-user-logo-regular-tal-revivo.png" 
       align="right" width="30%" style="margin: -20px 0 0 20px;">
  <h1>CLEARINBOX</h1>
  <p align="left">
    <em><code>❯ Automatically classify your emails as productive or unproductive</code></em>
  </p>

  <p align="left">Built with the following tools and technologies:</p>
  <p align="left">
    <a href="https://www.python.org/">
      <img src="https://skillicons.dev/icons?i=python&theme=light" width="60"/>
    </a>
    <a href="https://flask.palletsprojects.com/">
      <img src="https://skillicons.dev/icons?i=flask&theme=light" width="60"/>
    </a>
    <a href="https://www.w3.org/html/">
      <img src="https://skillicons.dev/icons?i=html&theme=light" width="60"/>
    </a>
    <a href="https://www.markdownguide.org/">
      <img src="https://skillicons.dev/icons?i=md&theme=light" width="60"/>
    </a>
  </p>

  <p align="left">
    <a href="https://github.com/marcelonovello/clearInbox/network/members">
      <img src="https://img.shields.io/github/forks/marcelonovello/clearInbox?style=flat-square&label=forks&color=555555" height="20"/>
    </a>
    <a href="https://github.com/marcelonovello/clearInbox/issues">
      <img src="https://img.shields.io/github/issues/marcelonovello/clearInbox?style=flat-square&label=issues&color=4caf50" height="20"/>
    </a>
    <a href="https://github.com/marcelonovello/clearInbox/blob/main/LICENSE">
      <img src="https://img.shields.io/github/license/marcelonovello/clearInbox?style=flat-square&label=license&color=4caf50" height="20"/>
    </a>
  </p>
</div>

<br clear="right">
<details><summary>Table of Contents</summary>

- [ Overview](#-overview)
- [ Features](#-features)
- [ Project Structure](#-project-structure)
  - [ Project Index](#-project-index)
- [ Getting Started](#-getting-started)
  - [ Prerequisites](#-prerequisites)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
  - [ Testing](#-testing)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)

</details>
<hr>

##  Overview

<code>❯ **Clear-In-box** is a Python Flask application that automatically classifies your emails as **productive** or **unproductive**, helping you focus on what matters and keep your inbox organized.</code>

---

##  Features

<code>❯ Automatic email classification</code><br>
<code>❯ Clean and simple interface</code><br>
<code>❯ Flask backend with HTML/CSS frontend</code><br>
<code>❯ Easily extensible for more features</code><br>

---

##  Project Structure

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


###  Project Index
<details open> <summary><b>CLEARINBOX/</b></summary> <table> <tr> <td><b>
<a href='https://github.com/marcelonovello/clearInbox/blob/master/app.py'>app.py</a></b></td> <td>Main Flask application entrypoint</td> </tr> <tr> <td><b>
  <a href='https://github.com/marcelonovello/clearInbox/blob/master/requirements.txt'>requirements.txt</a></b></td> <td>Python dependencies</td> </tr> <tr> <td><b>
    <a href='https://github.com/marcelonovello/clearInbox/blob/master/templates/index.html'>index.html</a></b></td> <td>Main HTML template</td> </tr> <tr> <td><b>
      <a href='https://github.com/marcelonovello/clearInbox/blob/master/static/style.css'>static/style.css</b></td> <td>CSS styling for the interface</td> </tr> </table> </details>

---
##  Getting Started

###  Prerequisites

Before getting started with clearInbox, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Pip

###  Installation

Install clearInbox using one of the following methods:

**Build from source:**

1. Clone the clearInbox repository:
```sh
❯ git clone https://github.com/marcelonovello/clearInbox
```

2. Navigate to the project directory:
```sh
❯ cd clearInbox
```

3. Install the project dependencies:


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r requirements.txt
```




###  Usage
Run clearInbox using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python {entrypoint}
```


###  Testing
Run the test suite using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pytest
```


---
##  Project Roadmap

- [X] **`Task 1`**: Initial email classification feature.
- [ ] **`Task 2`**: UI improvements.
- [ ] **`Task 3`**: Integration with real email services.
- [ ] **`Task 4`**: Initial email classification feature

---

##  Contributing

- **💬 [Join the Discussions](https://github.com/marcelonovello/clearInbox/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/marcelonovello/clearInbox/issues)**: Submit bugs found or log feature requests for the `clearInbox` project.
- **💡 [Submit Pull Requests](https://github.com/marcelonovello/clearInbox/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/marcelonovello/clearInbox
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/marcelonovello/clearInbox/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=marcelonovello/clearInbox">
   </a>
</p>
</details>

---

##  License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

##  Acknowledgments

- Flask
- Icons8
- Skillicons.dev
- Inspiration from productivity tools and email automation

---
