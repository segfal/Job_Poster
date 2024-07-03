import sqlite3
from jobspy import scrape_jobs



class JobFinder:
    def __init__(self):
        self.conn = sqlite3.connect('jobs.db')
        self.c = self.conn.cursor()
        self.blacklist_companies = {
            'Team Remotely Inc',
            'HireMeFast LLC',
            'Get It Recruit - Information Technology',
            "Offered.ai",
            "4 Staffing Corp"
        }
        self.bad_roles = {
            "unpaid",
            "senior",
            "lead",
            "manager",
            "director",
            "principal",
            "vp",
            "Sr.",
            "Sr",
            "Senior",
            "Lead",
            "Manager",
            "Director",
            "Principal",
            "VP",
            "sr.",
            "Snr",

        }

        self.create_table()

    def create_table(self):
        # create table if it doesn't exist
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

    def bad_role_substring(self, title):
        for bad_role in self.bad_roles:
            if bad_role in title:
                return True
        return False
    

    def job_exists(self, job):

        self.c.execute('SELECT * FROM jobs WHERE job_url = ?', (job['job_url'],))
        data = self.c.fetchall()
        return len(data) > 0
    

    def clear_jobs(self):
        self.c.execute('DELETE FROM jobs')
        self.conn.commit()

    def add_job(self, job):
        self.c.execute('''
            INSERT INTO jobs (job_url, title, company, location, date_posted)
            VALUES (?, ?, ?, ?, ?)
        ''', (job['job_url'], job['title'], job['company'], job['location'], job['date_posted']))
        self.conn.commit()

    def load_jobs(self, job_title):
        jobs = scrape_jobs(
            site_name=["linkedin"],
            search_term=job_title,
            location="New York, NY",
            results_wanted=20,
            hours_old=24, # (only Linkedin/Indeed is hour specific, others round up to days old)
            country_indeed='USA',  # only needed for indeed / glassdoor
        )

        job_arr = []
        for i in range(len(jobs)):
            job = {
                'job_url': jobs['job_url'][i],
                'title': jobs['title'][i],
                'company': jobs['company'][i],
                'location': jobs['location'][i],
                'date_posted': jobs['date_posted'][i]
            }
            
            if not self.job_exists(job):
                self.add_job(job)
                job_arr.append(job)

        return self.filter_jobs(self.filter_roles(job_arr))

    def filter_jobs(self, jobs):
        blacklist_companies = {
            'Team Remotely Inc',
            'HireMeFast LLC',
            'Get It Recruit - Information Technology',
        }

        return [job for job in jobs if job['company'] not in blacklist_companies]
    def filter_roles(self, jobs):
        return [job for job in jobs if not self.bad_role_substring(job['title'])]
    def get_jobs(self, job_title):
        jobs = self.load_jobs(job_title)
        jobs = self.filter_jobs(jobs)
        return jobs
    
    def clear(self):
        self.clear_jobs()
        self.conn.close()
        self.conn = sqlite3.connect('jobs.db')
        self.c = self.conn.cursor()
        self.create_table()





