import requests
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=2019년영화순위"

data = requests.get(url)

if data.status_code != requests.codes.ok:
    print("접속실패")
    exit()

html = BeautifulSoup(data.text, "html.parser")

movies = html.select('ol.movie_list > li')
for movie in movies:
    title = movie.select_one('.info_tit').text.strip()
    score = movie.select_one('.score .rate').text.strip()
    cont_data = movie.select('.dl_comm > .cont')
    date = cont_data[0].text.strip()
    year_score = cont_data[1].text.strip("명").replace(",","")
    total_socre = cont_data[2].text.strip("명").replace(",","")
    print(title, score, date, year_score, total_socre)