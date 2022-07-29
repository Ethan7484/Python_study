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

# from urllib.request import urlopen
# from urllib.request import HTTPError

# try:
#     html = urlopen('http://www.pythonscraping.com/pages/error.html')
# except HTTPError as e:
#     print(e)
#     #   null을 반환하거나, break 문을 실행하거나, 기타 다른 방법을 사용
# else:
#     # 프로그램을 계속 실행합니다. except 절에서 return이나 break를 사용했다면 이 else 절은 필요 없습니다.
    
    
# #URLError도 캐치하는 방법
# from urllib.request import urlopen
# from urllib.error import HTTPError
# from urllib.error import URLError

# try:
#     html = urlopen('http://pythonscrapingthisurldoesnotexist.com')  # 잘못된 URL를 입력한 상태
# except HTTPError as e:
#     print(e)
# except URLError as e:
#     print('This Server could not be found!')
# else:
#     print('It Worked!')




# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# html = urlopen('http://pythonscraping.com/pages/page1.html')
# bs = BeautifulSoup(html.read(), 'html.parser')
# bs = BeautifulSoup(html, 'html.parser')
# bs = BeautifulSoup(html, 'lxml')    # 구문분석기 lxml 사용


# print(bs.nonExistientTag)
# print(bs.head)

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://www.data.ai/intelligence/top-apps/store-rank/gp?date=%272022-07-13%27&country_code=KR&category_id=400001&product_id_meta=!(product_id.category_id)&chart.event_bubble.event_types=!(artwork_url_change,app_description,name_change,new_version,price_change,screenshot_change,app_company_id_change)&granularity=daily&store_rank_gp_chart_grossing$previous_range$chart_compare_facets=!(store_product_rank_free__aggr)&store-rank.gp.view=grossing&store-rank.gp.rank-type=leaderboard&store_rank.gp.chart_range=30&table_display=table')

bs = BeautifulSoup(html.read(), 'html.parser')


print(bs.div)
