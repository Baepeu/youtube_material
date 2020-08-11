import csv
import requests
from bs4 import BeautifulSoup

f = open("movie_list.csv","w", encoding="utf-8-sig", newline="")
writer = csv.DictWriter(f,
                        fieldnames=["제목", "평점", "개봉", "연간","누적"])
writer.writeheader()

for year in range(2019, 2010, -1):
    url = f"https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q={year}년영화순위"

    data = requests.get(url)

    if data.status_code != requests.codes.ok:
        print("접속실패")
        exit()

    html = BeautifulSoup(data.text, "html.parser")

    movies = html.select('ol.movie_list > li')
    for movie in movies:
        data_dict = {}
        title = movie.select_one('.info_tit').text.strip()
        score = movie.select_one('.score .rate').text.strip()

        data_dict["제목"] = title
        data_dict["평점"] = score
        cont_data = movie.select('.dl_comm')[1:]
        for cont in cont_data:
            tit = cont.select_one('.tit_base').text.strip().replace("재","")
            number = cont.select_one('.cont').text.strip("명").replace(",","")
            data_dict[tit] = number

        writer.writerow(data_dict)

f.close()