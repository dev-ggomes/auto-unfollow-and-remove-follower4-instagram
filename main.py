import sys
import time
import re
import json
import getpass
from http import cookiejar
from urllib import request, parse

# --- CONFIGURAÇÃO ---
IG_USERNAME = input('Usuário Instagram: ').strip()
IG_PASSWORD = getpass.getpass('Senha Instagram: ')

# Endpoints
LOGIN_URL = 'https://www.instagram.com/accounts/login/ajax/'
PROFILE_URL = 'https://www.instagram.com/{}/'
UNFOLLOW_URL = 'https://www.instagram.com/web/friendships/{}/unfollow/'
REMOVE_FOLLOWER_URL = 'https://www.instagram.com/web/friendships/{}/remove_follower/'

# Headers padrão
HEADERS = {
    'User-Agent': 'Mozilla/5.0',
    'Referer': 'https://www.instagram.com/',
}

# Criar um gerenciador de cookies
cj = cookiejar.CookieJar()
opener = request.build_opener(
    request.HTTPCookieProcessor(cj)
)
opener.addheaders = list(HEADERS.items())


def fetch_csrf_token():
    '''Faz GET na página principal para obter CSRF token.'''
    req = opener.open('https://www.instagram.com/')
    html = req.read().decode('utf-8')
    m = re.search(r'"csrf_token":"(?P<token>[^"]+)"', html)
    return m.group('token') if m else None


def login(csrf_token):
    '''Faz login via AJAX.'''  
    data = parse.urlencode({
        'username': IG_USERNAME,
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{int(time.time())}:{IG_PASSWORD}'
    }).encode()
    headers = HEADERS.copy()
    headers.update({
        'X-CSRFToken': csrf_token,
        'X-Requested-With': 'XMLHttpRequest'
    })
    req = request.Request(LOGIN_URL, data=data, headers=headers)
    res = opener.open(req)
    resp = json.loads(res.read().decode())
    if not resp.get('authenticated'):
        print('Falha no login:', resp)
        sys.exit(1)
    print('Login bem-sucedido.')


def get_user_id(username):
    '''Recupera o user_id a partir da página de perfil do usuário.'''
    req = opener.open(PROFILE_URL.format(username))
    html = req.read().decode('utf-8')
    m = re.search(r'"profilePage_(?P<id>\d+)"', html)
    return m.group('id') if m else None


def do_action(user, action):
    '''Executa unfollow ou remove_follower para o usuário especificado.'''
    uid = get_user_id(user)
    if not uid:
        print(f'Não encontrou user_id para {user}')
        return
    url = (UNFOLLOW_URL if action == 'unfollow' else REMOVE_FOLLOWER_URL).format(uid)

    # Atualiza CSRF token para a ação
    token = fetch_csrf_token()
    if not token:
        print('Não conseguiu obter CSRF token para a ação.')
        return

    headers = HEADERS.copy()
    headers['X-CSRFToken'] = token
    headers['X-Requested-With'] = 'XMLHttpRequest'

    req = request.Request(url, method='POST', headers=headers)
    resp = opener.open(req)
    data = json.loads(resp.read().decode())
    status = 'OK' if data.get('status') == 'ok' else 'Erro'
    verb = 'Unfollowed' if action == 'unfollow' else 'Removed follower'
    print(f'{verb} {user}: {status}')


def main():
    if len(sys.argv) < 3 or sys.argv[1] not in ('unfollow', 'remove'):
        print('Uso: python main.py [unfollow|remove] user1 user2 ...')
        sys.exit(1)
    action = sys.argv[1]
    users = sys.argv[2:]

    # Primeiro, obtém token e faz login
    token = fetch_csrf_token()
    if not token:
        print('Não conseguiu obter CSRF token inicial.')
        sys.exit(1)

    login(token)

    # Executa ações para cada usuário
    for user in users:
        do_action(user, action)
        time.sleep(2)


if __name__ == '__main__':
    main()