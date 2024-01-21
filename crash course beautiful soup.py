import requests
from bs4 import BeautifulSoup
import time
import csv
import os

print('Type your filter boss')
filter = input('>')
print(f'Filtering out {filter}')

def findjobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=Home_Search&from=submit&asKey=OFF&txtKeywords=&cboPresFuncArea=35').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    # File path for the CSV file
    file_path = 'jobs.csv'

    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write the headers
        writer.writerow(['Company Name', 'Skills Required', 'More Info'])

        for job in jobs:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '').strip()
            skill_set = job.find('span', class_='srp-skills').text.replace(' ', '').strip()
            more_info = job.header.h2.a['href']
            if filter.lower() not in skill_set.lower():
                # Write the job details into the CSV file
                writer.writerow([company_name, skill_set, more_info.strip()])
    
    print(f'Jobs saved to {file_path}')

if __name__ == '__main__':
    while True:
        findjobs()
        print("Waiting 10 minutes...")
        time.sleep(600)  # Waits for 10 minutes before the next run
