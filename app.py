

from backend.LinkedIn import job_finder
from discord.ext import commands
#discord env
import discord
import time
import asyncio

import os

from dotenv import load_dotenv
#import client

load_dotenv()
token = os.environ.get('TOKEN')

client = discord.Client(intents=discord.Intents.default())

job_finder.setjob("backend engineer")
jobs = job_finder.get_jobs()
#get rid of the spaces and newlines but not between words


#make the data readable
for table in jobs:
    for key in table:
        #find first letter of the string
        for i in range(0, len(table[key])):
            if table[key][i] != " ":
                table[key] = table[key][i:]
                break
        #find last letter of the string
        for i in range(len(table[key]) - 1, 0, -1):
            if table[key][i] != " ":
                table[key] = table[key][:i + 1]
                break
        #print(table[key])
        print(key + ": " + table[key])
        

    





@client.event
async def on_ready():
    #print(f'{client.user} has connected to Discord!')
    channel = client.get_channel(1071975520385904720)
    #build the message
    #message = "```"
    
    jerb = f'''Job Title: {jobs[0]['job_name']}\nCompany: {jobs[0]['company']}\nLocation: {jobs[0]['location']}\nLink: {jobs[0]['link']}\n'''
    await channel.send(jerb)


    #send a message to the channel


  


client.run(token)