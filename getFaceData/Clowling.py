# coding: utf-8
# testY2.py

import os
import sys
import traceback
from mimetypes import guess_extension
from time import time, sleep
from urllib.request import urlopen, Request
from urllib.parse import quote
from bs4 import BeautifulSoup

#任意のメールアドレス
#ツールを使ってダウンロードするときのマナーみたい
MY_EMAIL_ADDR = 'kamiyabi7777＠gmail.com'

class Fetcher:
    def __init__(self, ua=''):
        self.ua = ua

    def fetch(self, url):
        req = Request(url, headers={'User-Agent': self.ua})
        try:
            with urlopen(req, timeout=3) as p:
                b_content = p.read()
                mime = p.getheader('Content-Type')
        except:
            sys.stderr.write('Error in fetching {}\n'.format(url))
            sys.stderr.write(traceback.format_exc())
            return None, None
        return b_content, mime

fetcher = Fetcher(MY_EMAIL_ADDR)

def fetch_and_save_img(num):
    num_self = num
    #dataというディレクトリが作られる
    data_dir = 'data/'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    img_urls = img_url_list(num_self)[0]
    num_self2 = img_url_list(num_self)[1]
    s = num_self2 - 21

    for i, img_url in enumerate(img_urls):
        sleep(0.1)
        img, mime = fetcher.fetch(img_url)
        if not mime or not img:
            continue
        ext = guess_extension(mime.split(';')[0])
        if ext in ('.jpe', '.jpeg'):
            ext = '.jpg'
        if not ext:
            continue
        result_file = os.path.join(data_dir, str(s) + ext)
        with open(result_file, mode='wb') as f:
            f.write(img)
        s += 1
        print('fetched', img_url)

    if len(img_url) != 0:
        fetch_and_save_img(num_self2)

def img_url_list(num):
    """
    using yahoo (this script can't use at google)
    """
    num_self = num
    #このURL適宜変更
    #具体的には簡易検索の２ページ目のURL
    url = 'https://search.yahoo.co.jp/image/search?p=%E3%82%B7%E3%83%9E%E3%82%A8%E3%83%8A%E3%82%AC&oq=&ei=UTF-8&xargs=2&b={}&ktot=15'.format(num_self)
    byte_content, _ = fetcher.fetch(url)
    structured_page = BeautifulSoup(byte_content.decode('UTF-8'), 'html.parser')
    img_link_elems = structured_page.find_all('a', attrs={'target': 'imagewin'})
    img_urls = [e.get('href') for e in img_link_elems if e.get('href').startswith('http')]
    img_urls = list(set(img_urls))
    num_self += 20
    return img_urls,num_self

if __name__ == '__main__':
    # word = sys.argv[1]
    # fetch_and_save_img(word)
    num = 3
    fetch_and_save_img(num)