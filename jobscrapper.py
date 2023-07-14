from requests import get
from bs4 import BeautifulSoup

keyword = "python"
def scrapper(keyword):
    base_url = "https://www.jobkorea.co.kr/Search/?stext="
    
    # response에 html 저장
    response = get(f"{base_url}{keyword}")
    
    if response.status_code != 200: #링크 정상 작동하지 않는 경우
        print("Can't request website")
    else: 
        result = []
        soup = BeautifulSoup(response.text, "html.parser")  
        companies = soup.find_all("li", class_="list-post")
        
        for company in companies:
            inner = company.find("div")
            
            for_title = inner.find("div", class_="post-list-corp")
            title = for_title.find("a").text
            
            option = inner.find("p", class_="option")
            edu = option.find("span", class_="edu").text
            exp = option.find("span", class_="exp").text
            due = option.find("span", class_="date").text
            job_data = {"company": title.string,
                        "education": edu.string,
                        "experience": exp.string,
                        "due": due.string}
            
            result.append(job_data)
    
        return result

def save_to_file(file_name, jobs):
    file = open(f"{file_name}.csv", "w")
    file.write("company, education, experience, due\n")
    
    for job in jobs:
        file.write(
            f"{job['company']}, {job['education']}, {job['experience']}, {job['due']}\n")
    
    file.close()