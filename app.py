from discord.ext import commands, tasks

# discord env
import discord
import time
import asyncio
import os
from dotenv import load_dotenv
import json
from RankingSystem.dbase import create_table, insert_data,update_data

load_dotenv()
token = os.environ.get("TOKEN")
import json
import time
from is_prod import get_channels
from backend.Linkedin import linkedin_jobs

client = discord.Client(intents=discord.Intents.default())
bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())
channels = [bot.get_channel(i) for i in get_channels()]
sleep_schedule = 4

def get_jobs_from_linkedin(job_title):
    jobs = linkedin_jobs.get_jobs(job_title)
    return jobs


def get_backend_jobs():
    return get_jobs_from_linkedin("backend engineer")


def get_frontend_jobs():
    return get_jobs_from_linkedin("frontend engineer")


def get_fullstack_jobs():
    return get_jobs_from_linkedin("fullstack engineer")

def get_intern_jobs():
    return get_jobs_from_linkedin("software engineer intern")



@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    send_all_jobs.start()
    send_all_intern_jobs.start()
    clear_jobs_from_database.start()

   

@tasks.loop(seconds=3600)
async def send_all_jobs():
    """
    send all jobs to channel,
    for each role wait 10 seconds before sending the next role

    """
    channels = [bot.get_channel(i) for i in get_channels()]
    
    jobs = linkedin_jobs.load_jobs_from_jobspy("backend engineer")
    n = len(jobs)

    for i in range(n):
        embed = discord.Embed(
            title=f"{jobs[i]['title']}",
            description=f"**Company:** {jobs[i]['company']}\n**Location:** {jobs[i]['location']}\n**[Click here]({jobs[i]['job_url']})**",
            color=discord.Color.blue(),
        )

    for channel in channels:
        await channel.send(embed=embed)
        
    time.sleep(sleep_schedule)
    jobs = linkedin_jobs.load_jobs_from_jobspy("frontend engineer")
    n = len(jobs)

    for i in range(n):
        embed = discord.Embed(
            title=f"{jobs[i]['title']}",
            description=f"**Company:** {jobs[i]['company']}\n**Location:** {jobs[i]['location']}\n**[Click here]({jobs[i]['job_url']})**",
            color=discord.Color.blue(),
        )

    for channel in channels:
        await channel.send(embed=embed)
    time.sleep(sleep_schedule)
    jobs = linkedin_jobs.load_jobs_from_jobspy("fullstack engineer")
    n = len(jobs)

    for i in range(n):
        embed = discord.Embed(
            title=f" **NEW ROLE**",
            description=f" # **Role:** {jobs[i]['title']}\n # **Company:** {jobs[i]['company']}\n ## **Location:** {jobs[i]['location']}\n ## **[Click here]({jobs[i]['job_url']})**",
            color=discord.Color.blue(),
        )
        for channel in channels:
            await channel.send(embed=embed)
    time.sleep(sleep_schedule)


@tasks.loop(seconds=3600)
async def send_all_intern_jobs():
    """
    send all jobs to channel,
    for each role wait 10 seconds before sending the next role

    """
    channels = [bot.get_channel(i) for i in get_channels()]
    jobs = linkedin_jobs.load_jobs_from_jobspy("software engineer intern")
    n = len(jobs)

    for i in range(n):
        embed = discord.Embed(
            title=f"{jobs[i]['title']}",
            description=f"**Company:** {jobs[i]['company']}\n**Location:** {jobs[i]['location']}\n**[Click here]({jobs[i]['job_url']})**",
            color=discord.Color.blue(),
        )
        channel = bot.get_channel(1264048265268166696)
        await channel.send(embed=embed)
        time.sleep(sleep_schedule)


# clear jobs after 24 hours
@tasks.loop(seconds=86400)
async def clear_jobs_from_database():
    print("CLEARING JOBS")
    linkedin_jobs.clear_jobs_from_database()


bot.run(token)
