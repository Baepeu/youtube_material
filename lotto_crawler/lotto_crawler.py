# requests
# pip install requests
# beautifulsoup
# pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup

for index in range(1,904):
    url = f"https://search.daum.net/search?w=tot&rtmaxcoll=LOT&DA=LOT&q={index}회차%20로또"
    req = requests.get(url)
    if req.status_code != requests.codes.ok:
        print("접속 실패")
        continue
    html = BeautifulSoup(req.text, "html.parser")
    numbers = html.select("span.img_lotto")
    numbers_list = [int(number.text) for number in numbers]
    print(numbers_list)