import csv
from jobspy import scrape_jobs


import json




def job_exists(job):
    with open('jobs.json') as f:
        data = json.load(f)
        for i in data:
            if job == i:
                return True
        return False
def clear_json():
    with open('jobs.json', 'w') as f:
        json.dump([], f)
    
def add_job(job):
    with open('jobs.json') as f:
        data = json.load(f)
        data.append(job)
    with open('jobs.json', 'w') as f:
        json.dump(data, f)















def load_jobs(job_title):
    jobs = scrape_jobs(
        site_name=["linkedin"],
        search_term=job_title,
        location="New York, NY",
        results_wanted=20,
        hours_old=24, # (only Linkedin/Indeed is hour specific, others round up to days old)
        country_indeed='USA',  # only needed for indeed / glassdoor
    )

   
    columns = {
        "id",
        "job_url",
        "title",
        "company",
        "location",
        "date_posted",
    }
    job_arr = []
    for i in range(len(jobs)):
        job = {
            'job_name': jobs['title'][i],
            'company': jobs['company'][i],
            'location': jobs['location'][i],
            'link': jobs['job_url'][i],
            "date_posted" : jobs['date_posted'][i]
        }

        job_arr.append(job)

    return job_arr


jobs = load_jobs("software engineer")


arr = []
temp = {}
for i in range(len(jobs)):
    x = f""" >>> 
Job Title: {jobs[i]['job_name']}
Company: {jobs[i]['company']}
Location: {jobs[i]['location']}
Link: [Click here]({jobs[i]['link']})
""" 
    if not job_exists(jobs[i]):
        add_job(jobs[i])

        arr.append({
            "Job Title": jobs[i]['job_name'],
            "Company": jobs[i]['company'],
            "Location": jobs[i]['location'],
            "Link": jobs[i]['link']
        })
    else:
        print("Job already exists") 

null = None
a = [{"job_name": "Software Engineer", "company": "Middesk", "location": "New York, NY", "link": "https://www.linkedin.com/jobs/view/3963490995", "date_posted": null}, {"job_name": "Software Engineer, New Grad", "company": "Palantir Technologies", "location": "New York, NY", "link": "https://www.linkedin.com/jobs/view/3962792610", "date_posted": null}, {"job_name": "Software Engineer", "company": "Peloton Interactive", "location": "New York, NY", "link": "https://www.linkedin.com/jobs/view/3964830628", "date_posted": null}, {"job_name": "Software Engineer", "company": "iHeartMedia", "location": "New York, NY", "link": "https://www.linkedin.com/jobs/view/3961933173", "date_posted": null}, {"job_name": "Junior Node.JS Developer", "company": "Team Remotely Inc", "location": "New York, NY", "link": "https://www.linkedin.com/jobs/view/3964194982", "date_posted": null}, {"job_name": "Software Engineer", "company": "Traba", "location": "New York, NY", "link": "https://www.linkedin.com/jobs/view/3964707103", "date_posted": null}, {"job_name": "Junior Backend Engineer", "company": "Team Remotely Inc", "location": "New York, NY", "link": "https://www.linkedin.com/jobs/view/3964197793", "date_posted": null}, {"job_name": "Software Engineer", "company": "Traba", "location": "New York, NY", "link": "https://www.linkedin.com/jobs/view/3964706075", "date_posted": null}, {"job_name": "Associate, Software Engineer", "company": "Publicis Media", "location": "New York, NY", "link": "https://www.linkedin.com/jobs/view/3940377631", "date_posted": null}, {"job_name": "Software Engineer, Internship", "company": "Palantir Technologies", "location": "New York, NY", "link": "https://www.linkedin.com/jobs/view/3962791768", "date_posted": null}, {"job_name": "Software Engineer - Full Stack", "company": "Modern Treasury", "location": "New York, NY", "link": "https://www.linkedin.com/jobs/view/3963479920", "date_posted": null}, {"job_name": "Software Engineer, Frontend", "company": "Opal Security", "location": "New York, NY", "link": "https://www.linkedin.com/jobs/view/3961904167", "date_posted": null}, {"job_name": "Software Engineer", "company": "Beyond Identity", "location": "New York, NY", "link": "https://www.linkedin.com/jobs/view/3963466081", "date_posted": null}, {"job_name": "Software Engineer", "company": "ZAP Surgical Systems, Inc.", "location": "New York, NY", "link": "https://www.linkedin.com/jobs/view/3963493884", "date_posted": null}, {"job_name": "Junior Python Django Developer", "company": "Team Remotely Inc", "location": "New York, NY", "link": "https://www.linkedin.com/jobs/view/3964194995", "date_posted": null}, {"job_name": "Full Stack Developer I (Rome, New York) - Remote | WFH", "company": "Get It Recruit - Information Technology", "location": "New York, NY", "link": "https://www.linkedin.com/jobs/view/3961809383", "date_posted": null}, {"job_name": "Python Developer - Remote", "company": "NAVA Software Solutions", "location": "Jersey City, NJ", "link": "https://www.linkedin.com/jobs/view/3961894757", "date_posted": null}, {"job_name": "Software Engineer, Backend", "company": "Betterment", "location": "New York, NY", "link": "https://www.linkedin.com/jobs/view/3947096965", "date_posted": null}, {"job_name": "Staff Backend Software Engineer", "company": "Candy Digital", "location": "New York, NY", "link": "https://www.linkedin.com/jobs/view/3963194276", "date_posted": null}, {"job_name": "Software Engineer - Full Stack", "company": "Dripos", "location": "", "link": "https://www.linkedin.com/jobs/view/3963442513", "date_posted": null}, {"job_name": "Junior Java AWS Developer", "company": "Team Remotely Inc", "location": "New York, NY", "link": "https://www.linkedin.com/jobs/view/3964195848", "date_posted": null}, {"job_name": "Full Stack Engineer", "company": "Harbor.ai", "location": "New York, NY", "link": "https://www.linkedin.com/jobs/view/3964506492", "date_posted": null}, {"job_name": "Junior Android Engineer", "company": "Team Remotely Inc", "location": "New York, NY", "link": "https://www.linkedin.com/jobs/view/3964199489", "date_posted": null}, {"job_name": "Javascript/React Developer", "company": "TekSalt Solutions", "location": "New York, NY", "link": "https://www.linkedin.com/jobs/view/3963444574", "date_posted": null}, {"job_name": "Software Engineer || Full-Time", "company": "DKMRBH Inc", "location": "New York, NY", "link": "https://www.linkedin.com/jobs/view/3963453211", "date_posted": null}, {"job_name": "Software Engineer", "company": "Replit", "location": "New York, NY", "link": "https://www.linkedin.com/jobs/view/3963479218", "date_posted": null}, {"job_name": "Java Software Engineer", "company": "Rearc", "location": "New York, NY", "link": "https://www.linkedin.com/jobs/view/3962770192", "date_posted": null}, {"job_name": "Software Engineering AMTS/MTS (New Grad)", "company": "Salesforce", "location": "New York, NY", "link": "https://www.linkedin.com/jobs/view/3964811627", "date_posted": null}]


'''
 if company in blacklist companies, skip it

'''


def filter_jobs(jobs):
    blacklist_companies = {
        'Team Remotely Inc',
        'HireMeFast LLC',
        'Get It Recruit - Information Technology',
    }

    return [job for job in jobs if job['company'] not in blacklist_companies]

filtered_jobs = filter_jobs(jobs)

print(filtered_jobs)