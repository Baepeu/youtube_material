# pip install requests
import requests
# pip install beautifulsoup4
from bs4 import BeautifulSoup

# 사이트에 접속해서 내용 받아오기
url = "https://www.naver.com"
req = requests.get(url)
# 받아온 내용을 html로 파싱
html = BeautifulSoup(req.text, "html.parser")
# 원하는 내용을 html에서 찾아낸다.
elements = html.select("span")

for el in elements:
    print(el)
