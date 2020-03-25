# 크롤러 : 웹에서 정보를 수집하는 프로그램
# 예시 : 공연 예매, 수강신청, 구글&네이버
"""
1. 원하는 정보가 있는 웹 페이지에 접속
2. 페이지 로딩
3. 페이지에서 원하는 정보를 눈으로 찾아서 본다.
"""
"""
HTML : 내용과 구조를 담당하는 
CSS : 꾸미기 - X 
JavaScript : 화면의 움직임, 추가 데이터 가져오기

- requests, beautifulsoup (기본 크롤러)
+ 모듈 사용법
+ 셀렉터 만드는 법

- selenium (고급 크롤러 JS 추가 내용이 불러와지는 경우)
+ 모듈 사용법
"""

# requests 설치
# pip install requests
# beautifulsoup
# pip install beautifulsoup4

import requests
# 원하는 웹 페이지에 접근해서 데이터를 받아온다.
from bs4 import BeautifulSoup
# 웹 페이지의 코드를 html형태로 해석해주고, 원하는 요소를 찾도록 도와준다.

url = "https://datalab.naver.com/keyword/realtimeList.naver?where=main"
# 크롤러가 아닌척을 해보자!
custom_header = {
    "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}
req = requests.get(url, headers=custom_header)
# 접속이 잘되었는지 확인하는 과정
if req.status_code != requests.codes.ok:
    print("접속실패")
    exit()

# 데이터를 잘 받아왔으니까 원하는걸 찾아보자!
# Todo : 네이버에서 크롤러 접근을 막았다. 우회하는 방법이 필요하다.
html = BeautifulSoup(req.text, "html.parser")
"""
selector 선택자
html 태그들도 구성이 되어있다.
1. container태그
<span>내용</span>
2. empty태그
<img src="https://www.naver.com/logo.png" width="100" height="100">

1) 단일 선택자
- 태그이름 : span
- id : #name
- class : .nickname
<img src="그림주소" id="name" class="nickname title title_bold">
2) 복합 선택자
- 속성 복합 : img.nickname.title
- 경로 복합
p span img.nickname
* 대한민국 서울시 삼성동
* 대한민국 > 서울시 > 삼성동 <---- 중간 경로 생략 불가능
"""
items = html.select('.ranking_item .item_title') # 원하는 그룹 요소들을 찾을 때

#html.select_one() # 특정 요소 하나 찾을 때
for item in items:
    print(item.text)

# Todo : 검색어를 날짜별로 엑셀 파일에 저장하기
# Todo : 검색어를 매일 나에게 메일로 보내기
# Todo : 검색어의 검색 결과 페이지 보여주기, 링크 첨부하기







