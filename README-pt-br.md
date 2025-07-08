<!-- |||||||||||||||||||| EN - PT |||||||||||||||||||| -->
<p align='center'>
  <a href="https://github.com/dev-ggomes/auto-unfollow-and-remove-follower4-instagram/blob/main/README.md">🇺🇸 English</a> | 
  <a href="https://github.com/dev-ggomes/auto-unfollow-and-remove-follower4-instagram/blob/main/README-pt-pt.md">ᴘᴛ Português</a> | 
  <a href="https://github.com/dev-ggomes/auto-unfollow-and-remove-follower4-instagram/blob/main/README-pt-br.md">🇧🇷 Português</a>
</p>

<h1 align="center">
  🚀 Instagram CLI Manager
</h1>

<p align='center'>
  :octocat: Siga o passo a passo para usar este código da maneira certa.
</p>

<p align="center">
  ⭐ Se gostou deste repositório, me ajuda contribuindo com uma estrelinha
</p>

<!-- |||||||||||||||||||| SPONSORS & STARS |||||||||||||||||||| -->
<p align='center'>
  <a href="https://github.com/sponsors/dev-ggomes"><img alt="Sponsor" src="https://img.shields.io/badge/sponsor-30363D?style=social&logo=GitHub-Sponsors&logoColor=#white" /></a>
  &nbsp;
  <a href="#"><img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/dev-ggomes/auto-unfollow-and-remove-follower4-instagram?style=social" /></a>
</p>

<br>

## ✔️ Pré-requisitos

<p>
  
  - **Python 3.8+** instalado no seu sistema;
  - Uma conta Instagram válida com senha e nome de usuário;
  - Uma boa conexão com a internet.

</p>

---

## 🚀 Instalação

<p>

  #### 1. Clonar o repositório:

  - `git clone https://github.com/dev-ggomes/auto-unfollow-and-remove-follower4-instagram.git` <br>
  - `cd auto-unfollow-and-remove-follower4-instagram`

  #### 2. Verificar a sua versão do Python:

  - `python --version`

  >[!IMPORTANT]
  > Verifique que a sua versão é **3.8** ou superior.

  #### 3. Torne o código executável (apenas necessário para Linux & Mac):

  - `chmod +x main.py`
  
</p>

## ⚙️ Configuração

<p>
  Quando correr o script, ele irá pedir suas credenciais do Instagram.
</p>

>[!NOTE]
> Nenhuma das credenciais que você colocar será guardada em lado algum.

## 🏃‍♂️ Como usar

<p>
  
  Corra o script com a ação desejada e com os nomes de usuários (sem o `@`):

  - **Deixar de seguir**
    `python main.py unfollow usuário1 usuário2 usuário3`

  - **Remover seguidores**
    `python main.py remove seguidor1 seguidor2 seguidorr3`

  ### Exemplo de Output

  ```bash
  $ python main.py unfollow alice bob
  Username Instagram: seu_nome_de_usuário_aqui (sem o @)
  Password Instagram: sua_senha_aqui (a sua senha não vai ser guardada em nenhum lugar)
  Login successful.
  Unfollowed alice: OK
  Unfollowed bob: OK
  ```
</p>

## 🛠 Troubleshooting

<p>

  - **Erros CSRF** ou respostas inesperadas: Aguarde uns segundos e tente novamente--O Instagram pode bloquear várias ações muito repetidas;
  - **Falhas no Login**: Verifique se o seu nome de usuário e senha estão corretos;
  - **Blocks temporários**: Se o Instagram bloquear temporariamente sua conta ou seu IP, espere no mínimo 15 minutos antes de tentar denovo.

    <br>

---

> [!WARNING]
> Eu **NÃO SOU** responsável por nenhuma ação que o Instagram tenha com a sua conta ou com seu IP, seja ela temporária ou permanente. Este projeto foi desenvolvido para **testar meu conhecimento**. Use **por conta própria** e com **seu próprio risco**.

---
</p>

## 📄 Licença

<p>
  
  Este projeto é distribuído com a **Licença MIT**. Acesse [LICENSE](https://github.com/dev-ggomes/auto-unfollow-and-remove-follower4-instagram?tab=MIT-1-ov-file) para saber os termos.

</p>
