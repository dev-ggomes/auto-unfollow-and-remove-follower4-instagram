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
  :octocat: Segue o passo a passo para usar este código da maneira correta.
</p>

<p align="center">
  ⭐ Se gostou deste repositório, por favor contribua com uma estrela
</p>

<!-- |||||||||||||||||||| SPONSORS & STARS |||||||||||||||||||| -->
<p align='center'>
  <a href="https://github.com/sponsors/dev-ggomes"><img alt="Sponsor" src="https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#white" /></a>
  &nbsp;
  <a href="#"><img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/dev-ggomes/auto-unfollow-and-remove-follower4-instagram?style=for-the-badge" /></a>
</p>

<br>

## ✔️ Pré-requisitos

<p>
  
  - **Python 3.8+** instalado no teu sistema;
  - Uma conta de Instagram válida com nome de utilizador e password;
  - Boa conexão à internet.

</p>

---

## 🚀 Instalação

<p>

  #### 1. Clonar este repositório:

  - `git clone https://github.com/dev-ggomes/auto-unfollow-and-remove-follower4-instagram.git` <br>
  - `cd auto-unfollow-and-remove-follower4-instagram`

  #### 2. Verificar a versão do Python:

  - `python --version`

  >[!IMPORTANT]
  > Confirma que a versão é **3.8** ou superior.

  #### 3. Tornar o script executável (apenas com Linux & Mac):

  - `chmod +x main.py`
  
</p>

## ⚙️ Configuração

<p>
  Ao iniciar, o script irá pedir pelas tuas credenciais do Instagram (nome de utilizador e password).
</p>

>[!NOTE]
> Nenhuma credencial é guardada neste repositório nem em lado nenhum.

## 🏃‍♂️ Como usar

<p>
  
  Corre o script com a ação desejada e com os nomes de utilizadores alvos (sem o `@`):

  - **Parar de seguir utilizadores**
    `python main.py unfollow utilizador1 utilizador2 utilizador3`

  - **Remover seguidores**
    `python main.py remove seguidor1 seguidor2 seguidor3`

  ### Exemplo de sessão

  ```bash
  $ python main.py unfollow alice bob
  Username Instagram: o_teu_nome_de_utilizador_aqui
  Password Instagram: a_tua_password_aqui (a password não vai ser guardada em nenhum sítio)
  Login successful.
  Unfollowed alice: OK
  Unfollowed bob: OK
  ```
</p>

## 🛠 Possíveis erros

<p>

  - **Erros de CSRF** ou respostas inesperadas: Espera uns segundos e tenta denovo--O Instagram pode bloquear ações iguais muito seguidas num curto espaço tempo;
  - **Falhas no Login**: Verifica se o teu nome de utilizador e password estão corretos;
  - **Temporariamente bloqueado**: Se o Instagram bloquear temporariamente o teu IP ou a tua conta, espera no mínimo 15 minutos antes de tentar denovo.

    <br>

---

> [!WARNING]
> Eu **NÃO SOU** responsável por nenhuma ação que o Instagram tenha para com a tua conta ou o teu IP, sejam elas temporárias ou permanentes. Este script foi desenvolvido para **testar o meu conhecimento**. Usa pela **tua conta** e **risco**.

---
</p>

## 📄 Licença

<p>
  
  Este projeto é distribuído ao abrigo da **Licença MIT**. Vê a [Licença](https://github.com/dev-ggomes/auto-unfollow-and-remove-follower4-instagram?tab=MIT-1-ov-file) para saberes os termos.

</p>
