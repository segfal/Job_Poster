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
print(channels)


def get_jobs(job_title):
    jobs = linkedin_jobs.get_jobs(job_title)
    return jobs


def get_backend_jobs():
    return get_jobs("backend engineer")


def get_frontend_jobs():
    return get_jobs("frontend engineer")


def get_fullstack_jobs():
    return get_jobs("fullstack engineer")


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    send_all_jobs.start()
    clear_jobs.start()

   

@tasks.loop(seconds=3600)
async def send_all_jobs():
    """
    send all jobs to channel,
    for each role wait 10 seconds before sending the next role

    """
    channels = [bot.get_channel(i) for i in get_channels()]
    
    jobs = linkedin_jobs.load_jobs("backend engineer")
    n = len(jobs)

    for i in range(n):
        embed = discord.Embed(
            title=f"{jobs[i]['title']}",
            description=f"**Company:** {jobs[i]['company']}\n**Location:** {jobs[i]['location']}\n**[Click here]({jobs[i]['job_url']})**",
            color=discord.Color.blue(),
        )

        for channel in channels:
            await channel.send(embed=embed)
        
    time.sleep(4)
    jobs = linkedin_jobs.load_jobs("frontend engineer")
    n = len(jobs)

    for i in range(n):
        embed = discord.Embed(
            title=f"{jobs[i]['title']}",
            description=f"**Company:** {jobs[i]['company']}\n**Location:** {jobs[i]['location']}\n**[Click here]({jobs[i]['job_url']})**",
            color=discord.Color.blue(),
        )

        for channel in channels:
            await channel.send(embed=embed)
    time.sleep(4)
    jobs = linkedin_jobs.load_jobs("fullstack engineer")
    n = len(jobs)

    for i in range(n):
        embed = discord.Embed(
            title=f"{jobs[i]['title']}",
            description=f"**Company:** {jobs[i]['company']}\n**Location:** {jobs[i]['location']}\n**[Click here]({jobs[i]['job_url']})**",
            color=discord.Color.blue(),
        )
        for channel in channels:
            await channel.send(embed=embed)
    time.sleep(4)



# clear jobs after 24 hours
@tasks.loop(seconds=86400)
async def clear_jobs():
    print("CLEARING JOBS")
    linkedin_jobs.clear_jobs()


bot.run(token)
