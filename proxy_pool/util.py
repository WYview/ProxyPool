import requests

HEADERS={
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'}


def get_page(url,encoding='utf-8'):

    r=requests.get(url,headers=HEADERS)
    r.encoding=encoding
    return r.text
