## 1주차) 파이썬으로 웹 스크래퍼 만들기 ##
from requests import get
from bs4 import BeutifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?search_uuid=&term="
search_term = "python"

response = get(f"{base_url}{search_term}")

if response.status_code != 200:
    print("Can't request website")
else:
    print(response.text) #html