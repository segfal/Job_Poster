from bs4 import BeautifulSoup



class JobFinder:
    def __init__(self):
        self.jobs = []
        self.jobput = ""
        self.jobtitle = ""
    
    def get_jobs(self):
        return self.jobs
    
    def get_job(self, job_id):
        return self.jobs[job_id]
    def setjob(self, job):
        self.jobput = job