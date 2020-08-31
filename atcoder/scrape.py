import requests
from bs4 import BeautifulSoup

def gen_json(contest):
    loginurl = f'https://atcoder.jp/login'
    ranklist = f'https://atcoder.jp/contests/{contest}/standings/json'
    s = requests.Session()
    r = s.get(loginurl)
    soup = BeautifulSoup(r.content, 'html.parser')
    csrf = soup.find('input', attrs={'name':'csrf_token'})['value']

    # Supply an AtCoder account details
    user = 'username'
    password = 'password'

    r = s.post(loginurl, data={'username':user, 'password':password, 'csrf_token':csrf})
    r = s.get(ranklist)

    data = r.text
    with open('ranklist.json', 'w') as f:
        f.write(data)
    s.close()
