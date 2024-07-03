from backend.JobFinder import JobFinder
import sqlite3


class Linkedin(JobFinder):
    def __init__(self):
        super().__init__()
        self.site_name = 'linkedin'
        self.search_term = 'software engineer'
        self.location = 'New York, NY'
        self.results_wanted = 20
        self.hours_old = 24
        self.country_indeed = 'USA'
        self.conn = sqlite3.connect('linkedin.db')
        self.c = self.conn.cursor()
        self.create_table()

    
    def create_table(self):
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS jobs (
                id INTEGER PRIMARY KEY,
                job_url TEXT,
                title TEXT,
                company TEXT,
                location TEXT,
                date_posted TEXT
            )
        ''')
        self.conn.commit()
    
    
    

    
linkedin_jobs = Linkedin()