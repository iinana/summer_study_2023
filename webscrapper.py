## 1주차) 파이썬으로 웹 스크래퍼 만들기 ##
from requests import get
from bs4 import BeautifulSoup


# job scarpping from weworkremotely
def extract_wwr_jobs(keyword):
    base_url = "https://weworkremotely.com/remote-jobs/search?search_uuid=&term="
    
    # response에 html 저장
    response = get(f"{base_url}{keyword}")
    
    if response.status_code != 200: #링크 정상 작동하지 않는 경우
        print("Can't request website")
    else: 
        result = []
        
        # html에 원하는 부분 찾기 (section 중 class가 job인 것)
        soup = BeautifulSoup(response.text, "html.parser")
        jobs = soup.find_all("section", class_="jobs")
        #print(len(jobs)) # how many jobs?
        
        # 각각의 section에서 각각의 job post에 접근
        for job_section in jobs:
            job_posts = job_section.find_all("li")  # list of job posts
            job_posts.pop(-1)  #마지막요소가 job이 아니라 view all 버튼이므로 제거
            
            # job_posts 내 각각의 job post는 단순 string이 아니라 beautiful soup entity -> 다시 내부 html에 접근 가능
            # 각각의 job post의 feature들에 접근
            for post in job_posts:
                anchors = post.find_all("a")
                anchor = anchors[1]  #anchors 중 두번째 것만 필요함 (두번째 link가 유효한 링크)
                link = anchor['href']
                
                # anchor 내 span에 접근 (job feature)
                company, kind, region = anchor.find_all("span", class_="company")
                title = anchor.find("span", class_="title")
                
                # .string : html에서 정보 text만 추출
                job_data = {'link': f"https://weworkremotely.com{link}",
                            'company': company.string,
                            'full/part': kind.string,
                            'region': region.string,
                            'position': title.string}
                result.append(job_data)
                
        return result
        
def save_to_file(file_name, jobs):
    file = open(f"{file_name}.csv", "w")
    file.write("Position, Company, Location, URL\n")
    
    for job in jobs:
        file.write(
            f"{job['position']}, {job['company']}, {job['region']}, {job['link']}\n")
    
    file.close()
        

keyword = "python"
save_to_file(keyword, extract_wwr_jobs(keyword))

