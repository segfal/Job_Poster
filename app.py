

from discord.ext import commands,tasks
#discord env
import discord
import time
import asyncio
import os
from dotenv import load_dotenv
#import client
import json
load_dotenv()
token = os.environ.get('TOKEN')
import json
client = discord.Client(intents=discord.Intents.default())
bot = commands.Bot(command_prefix='!', intents=discord.Intents.default())

from jobspy import scrape_jobs







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

def filter_jobs(jobs):
    blacklist_companies = {
        'Team Remotely Inc',
        'HireMeFast LLC',
        'Get It Recruit - Information Technology',
    }

    return [job for job in jobs if job['company'] not in blacklist_companies]

def load_jobs(job_title):
    
    # if the job name contains a prohibited company skip it
    blacklist_companies = [
        'Team Remotely Inc',
        'HireMeFast LLC',
        'Get It Recruit - Information Technology',       
    ]
    
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
            'job_name': jobs['title'][i],
            'company': jobs['company'][i],
            'location': jobs['location'][i],
            'link': jobs['job_url'][i],
            "date_posted" : jobs['date_posted'][i]
        }
        if not job_exists(job):
            add_job(job)
            job_arr.append(job)
    

    return [job for job in job_arr if job['company'] not in blacklist_companies]








@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    send_backend_jobs.start()
    send_frontend_jobs.start()
    send_fullstack_jobs.start()




@tasks.loop(seconds=3600)
async def send_backend_jobs():
    channel = bot.get_channel(1257135450133500055)
    channel2 = bot.get_channel(1257137243483672608)
    #build the message
    #message = "```"
    jobs = load_jobs("backend engineer")
    n = len(jobs)
    for i in range(n):
        jerb = f""" ``` ```
>>> ## Job Title: {jobs[i]['job_name']}
**Company:** {jobs[i]['company']}
**Location:** {jobs[i]['location']}
**Link:** [Click here]({jobs[i]['link']})
""" 
        await channel.send(jerb)
        await channel2.send(jerb)


@tasks.loop(seconds=3800)
async def send_frontend_jobs():
    channel = bot.get_channel(1257135450133500055)
    channel2 = bot.get_channel(1257137243483672608)
    #build the message
    #message = "```"
    jobs = load_jobs("frontend engineer")
    n = len(jobs)
    for i in range(n):
        jerb = f""" ``` ```
>>> ## Job Title: {jobs[i]['job_name']}
**Company:** {jobs[i]['company']}
**Location:** {jobs[i]['location']}
**Link:** [Click here]({jobs[i]['link']})
""" 
        await channel.send(jerb)
        await channel2.send(jerb)




@tasks.loop(seconds=4100)
async def send_fullstack_jobs():
    channel = bot.get_channel(1257135450133500055)
    channel2 = bot.get_channel(1257137243483672608)
    #build the message
    #message = "```"
    jobs = load_jobs("fullstack engineer")
    n = len(jobs)
    for i in range(n):
        jerb = f""" ``` ```
>>> ## Job Title: {jobs[i]['job_name']}
**Company:** {jobs[i]['company']}
**Location:** {jobs[i]['location']}
**Link:** [Click here]({jobs[i]['link']})
""" 
        await channel.send(jerb)
        await channel2.send(jerb)



#clear jobs after 24 hours
@tasks.loop(seconds=86400)
async def clear_jobs():
    clear_json()




bot.run(token)