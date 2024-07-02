from backend.JobFinder import JobFinder
from bs4 import BeautifulSoup
import requests




class LinkedIn(JobFinder):
    def __init__(self):
        super().__init__()
        self.url = "https://www.linkedin.com/jobs/search/"
        """
            https://www.linkedin.com/jobs/search?keywords=software%20engineer&location=United%20States&geoId=103644278&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0
        
        
        """

    
    def get_html(self,job_title):
        #posts jobs from linkedin that has been posted within the last 24 hours
        params = {
    "keywords": job_title,  # Specific job keywords can be added here if needed
    "location": "New York, United States",
    "geoId": "105080838",  # Geographic ID for New York
    "f_TPR": "r86400",      # Time period for jobs in the past hour
    "position": "1",       # Result position
    "pageNum": "0"         # Page number
    }

        response = requests.get(self.url, params = params)
        
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
        if len(job_links) == 0:
            return []
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

            if "senior" not in job_name.lower():
                job = self.job_design(job_name,company,location,link)
                self.jobs.append(job)
        
        return self.jobs



job_finder = LinkedIn()



