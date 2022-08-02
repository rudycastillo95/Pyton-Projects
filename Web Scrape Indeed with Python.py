import requests
from bs4 import BeautifulSoup

def extract(page):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
    url = f'https://www.indeed.com/jobs?q=Business%20Analyst&l=Nashville%2C%20TN&start={page}'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):
    divs = soup.find_all('div', class_ = 'jobCard_mainContent')
    for item in divs:
        title = item.find('a').text.strip()
        company = item.find('span', class_ 'company').text.strip()
        try:
            salary = item.find('span', class_ = 'salaryText').text.strip()
        except:
            salary = ''
        summary = item.find('div', {'class' : 'summary'}).text.strip().replace('\n', '')

        job = {
            'title': title,
            'company': company,
            'salary': salary,
            'summary': summary
        }
        joblist.append(job)
    return

joblist = []
c = extract(0)
transform(c)
print(joblist)
