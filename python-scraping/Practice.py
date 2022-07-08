"""
from socketserver import BaseRequestHandler
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html.parser')
bs = BeautifulSoup(html, 'html.parser')
bs = BeautifulSoup(html, 'lxml')    # 구문분석기 lxml 사용
print(bs.h1)
print(bs.head)
print(bs.title)
print(bs.body)
print(bs.div)
"""

from urllib.request import urlopen
from urllib.request import HTTPError

try:
    html = urlopen('http://www.pythonscraping.com/pages/error.html')
except HTTPError as e:
    print(e)
    #   null을 반환하거나, break 문을 실행하거나, 기타 다른 방법을 사용
else:
    # 프로그램을 계속 실행합니다. except 절에서 return이나 break를 사용했다면 이 else 절은 필요 없습니다.