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
  :octocat: Follow the step by step guide to run this code the proper way.
</p>

<p align="center">
  ⭐ If you liked this project, please give it a star
</p>

<!-- |||||||||||||||||||| SPONSORS & STARS |||||||||||||||||||| -->
<p align='center'>
  <a href="https://github.com/sponsors/dev-ggomes"><img alt="Sponsor" src="https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#white" /></a>
  &nbsp;
  <a href="#"><img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/dev-ggomes/auto-unfollow-and-remove-follower4-instagram?style=for-the-badge" /></a>
</p>

<br>

## ✔️ Prerequisites

<p>
  
  - **Python 3.8+** installed on your system;
  - A valid Instagram account with username and password;
  - Active internet connection.

</p>

---

## 🚀 Installation

<p>

  #### 1. Clone the repository:

  - `git clone https://github.com/dev-ggomes/auto-unfollow-and-remove-follower4-instagram.git` <br>
  - `cd auto-unfollow-and-remove-follower4-instagram`

  #### 2. Verify Python version:

  - `python --version`

  >[!IMPORTANT]
  > Ensure the output is **3.8** or higher.

  #### 3. Make the script executable on Unix-based systems:

  - `chmod +x main.py`
  
</p>

## ⚙️ Configuration

<p>
  The script will prompt you for your Instagram credentials at runtime.
</p>

>[!NOTE]
> No hardcoded credentials are stored in this repository.

## 🏃‍♂️ Usage

<p>
  
  Run the script with the desired action and target usernames (without the `@` symbol):

  - **Unfollow users**
    `python main.py unfollow username1 username2 username3`

  - **Remove followers**
    `python main.py remove follower1 follower2 follower3`

  ### Example Session

  ```bash
  $ python main.py unfollow alice bob
  Username Instagram: your_username_here
  Password Instagram: your_password_here (the password is not going to be stored at any place)
  Login successful.
  Unfollowed alice: OK
  Unfollowed bob: OK
  ```
</p>

## 🛠 Troubleshooting

<p>

  - **CSRF errors** or unexpected responses: Wait a few seconds and retry--Instagram may rate-limit rapid requests;
  - **Login failures**: Verify that your username and password are correct;
  - **Temporary blocks**: If Instagram temporarily blocks your IP or account, wait at least 15 minutes before retrying.

    <br>

---

> [!WARNING]
> I am **NOT** responsible for any taken actions by Instagram to your account or your IP, either they are temporarily or permantly. This script was developed to **test my knowledge**. Use it on **your own responsibily** and **risk**.

---
</p>

## 📄 License

<p>
  
  This project is distributed under the **MIT License**. Check [LICENSE](https://github.com/dev-ggomes/auto-unfollow-and-remove-follower4-instagram?tab=MIT-1-ov-file) for full terms.

</p>
