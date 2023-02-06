from backend.JobFinder import JobFinder
from bs4 import BeautifulSoup
import requests




class LinkedIn(JobFinder):
    def __init__(self):
        super().__init__()
        self.url = "https://www.linkedin.com/jobs/search/"
        

    
    def get_html(self,job_title):
        response = requests.get(self.url, params = {'keywords': job_title})
        soup = BeautifulSoup(response.text, 'lxml')
        return soup
    
    def job_design(self,job_name,company,location,link):
        job = {
            'job_name': job_name,
            'company': company,
            'location': location,
            'link': link,
        }
        return job

    def get_jobs(self):
        #clean up the jobs list
        self.jobs = []
      
        soup = self.get_html(self.jobput)
       
        job_cards = soup.find_all('div', class_ = 'base-card')
        #base-card__full-link this will be the link to the job get the href
        job_links = soup.find_all('a', class_ = 'base-card__full-link')
        x = str(job_links[0])
        #look for the href
        href = x.find('href')
        joblink = x[href+6:]
        #find the end of the link using semicolon
        end = joblink.find(';')
        joblink = joblink[:end]

        #do a for loop to get all the jobs
        for job in job_cards:
            job_name = job.find('h3', class_ = 'base-search-card__title').text
            company = job.find('a', class_ = 'hidden-nested-link').text
            location = job.find('span', class_ = 'job-search-card__location').text
            job_links = job.find('a', class_ = 'base-card__full-link')
            #get rid of the newlines
            job_name = job_name.replace('\n','')
            company = company.replace('\n','')
            location = location.replace('\n','')
            #find the first alphabet in the job name
            
            link = joblink
            x = str(job_links)
            href = x.find('href')
            joblink = x[href+6:]
            end = joblink.find(';')
            joblink = joblink[:end]

            job = self.job_design(job_name,company,location,link)
            self.jobs.append(job)
        
        return self.jobs



job_finder = LinkedIn()



