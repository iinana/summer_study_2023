from requests import get
from bs4 import BeautifulSoup


def extract_info_startup(keyword):
    base_url = "https://www.ycombinator.com/companies?query="

    # response에 html 위치 저장
    response = get(f"{base_url}{keyword}")

    print(response.status_code)


extract_info_startup(health)
