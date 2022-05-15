# import os
# import sendgrid
# from sendgrid import SendGridAPIClient
# import sendgrid.helpers.mail *

import asyncio
from datetime import *
import datetime
from nextcord.ext import commands
from nextcord import Intents, SlashOption, ButtonStyle, Interaction, ui, Client, ClientUser, guild
from discordtoken import token
from Talons import Talons

from twilio.rest import Client
import keys


talon = None
discordInstances = {}
talon = None

intents = Intents.all()
bot = commands.Bot(command_prefix="$", intents = intents)

@bot.command()
async def prompts(ctx: commands.Context):
    await ctx.send("Here are the different commands that you can use:")
    await ctx.send("(Please replace <field> with its corresponding value that is expected - (Please follow format)")
    await ctx.send("```$setup <phonenumber(e.g. +16477238263)> <emailAddress(e.g. talons.mlh@gmail.com)>```")
    await ctx.send("```$replaceNumber <phonenumber(e.g. +16477238263)>```")
    await ctx.send("```$replaceEmail <emailAddress(e.g. talons.mlh@gmail.com)>```")
    await ctx.send("```$addReminder <message(e.g.\"walk your dog\")> <message(e.g.\"20:12:33\")>```")
    await ctx.send("```$addEvent <message(e.g.\"join zoom\")> <message(e.g.\"20:12:33\")> <link(e.g.\"zoom.com\")>```")
    await ctx.send("```$deleteEvent <message(e.g.\"join\")> <message(e.g.\"20:12:33\")> <link(e.g.\"hopin.com\")>```")
    await ctx.send("```$deleteReminder <message(e.g.\"walk your dog\")> <message(e.g. \"20:12:33\")>```")
    await ctx.send("```$showReminders```")
    await ctx.send("```$pomodoro <workTime(e.g.\"00:50:00\")> <breakTime(e.g. \"00:10:00\")>``` ")
    await ctx.send("```$startWorkTime```")
    await ctx.send("```$startBreakTime```")

@bot.command()
async def setup(ctx: commands.Context, phoneNumber, emailAddress):
    discordID = str(ctx.message.author.id)
    if discordID in discordInstances.keys():
        talon = discordInstances.get(discordID)
    else:
        discordInstances[discordID] = Talons(phoneNumber, emailAddress)
        talon = discordInstances.get(discordID)
    # print(discordInstances)
    await ctx.send(talon)

@bot.command()
async def replaceNumber(ctx: commands.Context, phoneNumber):
    discordID = str(ctx.message.author.id)
    if discordID in discordInstances.keys():
        talon = discordInstances.get(discordID)
        talon.numberSet = phoneNumber
        await ctx.send("If the phone number exists, then you will receive your text notifications through SMS")
    # print(discordInstances)
    await ctx.send(talon)

@bot.command()
async def replaceEmail(ctx: commands.Context, emailAddress):
    discordID = str(ctx.message.author.id)
    if discordID in discordInstances.keys():
            talon = discordInstances.get(discordID)
            talon.emailSet = emailAddress
            await ctx.send("If the email exists, then you will find your notifications here")
    # print(discordInstances)
    await ctx.send(talon)

@bot.command()
async def addReminder(ctx: commands.Context, message, hourminsec):
    discordID = str(ctx.message.author.id)
    if discordID in discordInstances.keys():
        talon = discordInstances.get(discordID)
        returned = talon.appendReminder((message, hourminsec))
        if returned == -1:
            await ctx.send("This reminder already exists")
        timeLeft = calcTimeDiff(int(hourminsec[0:2]),int(hourminsec[3:5]), int(hourminsec[6:8]))
        if(timeLeft<0):
            await ctx.send("Pick a time in the future")
        else:
            await timer(ctx,message,f"{int(timeLeft)}s", hourminsec, 0, "")
    # print(talon.listOfReminders)

@bot.command()
async def deleteReminder(ctx: commands.Context, message, time):
    discordID = str(ctx.message.author.id)
    if discordID in discordInstances.keys():
        talon = discordInstances.get(discordID)
        talon.removeReminder((message, time))
    # print(talon.listOfReminders)

@bot.command()
async def addEvent(ctx: commands.Context, message, hourminsec, link):
    discordID = str(ctx.message.author.id)
    if discordID in discordInstances.keys():
        talon = discordInstances.get(discordID)
        returned = talon.appendEvent((message, time, link))
        if returned == -1:
            await ctx.send("This event already exists")
        timeLeft = calcTimeDiff(int(hourminsec[0:2]), int(hourminsec[3:5]), int(hourminsec[6:8]))
        if (timeLeft < 0):
            await ctx.send("Pick a time in the future")
        else:
            await timer(ctx, message, f"{int(timeLeft)}s", hourminsec, 2, link)
    # print(talon.listOfEvents)

@bot.command()
async def deleteEvent(ctx: commands.Context, message, time, link):
    discordID = str(ctx.message.author.id)
    if discordID in discordInstances.keys():
        talon = discordInstances.get(discordID)
        talon.removeEvent((message, time, link))
    # print(talon.listOfEvents)

@bot.command()
async def showReminders(ctx: commands.Context):
    discordID = str(ctx.message.author.id)
    if discordID in discordInstances.keys():
        talon = discordInstances.get(discordID)
    if len(talon.listOfReminders) > 0:
        await ctx.send("These are your reminders:")
        for msgReminder, hourminsec in talon.listOfReminders:
            await ctx.send(f"> {msgReminder} @ {hourminsec}")
    else:
        await ctx.send("There are no reminders set")

@bot.command()
async def showEvents(ctx: commands.Context):
    discordID = str(ctx.message.author.id)
    if discordID in discordInstances.keys():
        talon = discordInstances.get(discordID)
    if len(talon.listOfEvents) > 0:
        await ctx.send("These are your upcoming events:")
        for msgEvent, timeEvent, linkEvent in talon.listOfEvents:
            await ctx.send("> " + msgEvent + " @ " + timeEvent + ", Join:" + linkEvent)
    else:
        await ctx.send("There are no events set")

def calcTimeDiff(hour, min, sec):
    currentHour = datetime.datetime.now().hour
    currentMin = datetime.datetime.now().minute
    currentSec = datetime.datetime.now().second
    currentTime = datetime.timedelta(hours = currentHour, minutes = currentMin, seconds = currentSec)
    timeForReminder = datetime.timedelta(hours = hour, minutes = min, seconds = sec)
    timeInterval = timeForReminder - currentTime
    return timeInterval.total_seconds()

async def timer(ctx: commands.Context, message2, timeInput, stringTime, signal, link):
    discordID = str(ctx.message.author.id)
    if discordID in discordInstances.keys():
        talon = discordInstances.get(discordID)
    try:
        try:
            time = int(timeInput)
        except:
            convertTimeList = {'s':1, 'm':60, 'h':3600, 'd':86400, 'S':1, 'M':60, 'H':3600, 'D':86400}
            time = int(timeInput[:-1]) * convertTimeList[timeInput[-1]]
        if time > 86400:
            await ctx.send("I can\'t do timers over a day long")
            return
        if time <= 0:
            await ctx.send("Timers don\'t go into negatives :/")
            return
        while True:
            try:
                await asyncio.sleep(1)
                time -= 1
                if time <= 0:
                    await ctx.send(f"{ctx.author.mention}, Time to {message2}!")
                    if signal == 0:
                        talon.removeReminder((message2, stringTime))
                        client = Client(keys.account_sid, keys.auth_token)
                        message = client.messages.create(
                            body=message2.upper(),
                            from_=keys.twilio_number,
                            to=talon.numberSet
                        )
                    # elif signal == 1:
                    #     talon.removeEvent((message2, stringTime, link))
                    #     message = Mail(from_email = keys.from_email,
                    #                    to_emails = talon.emailSet,
                    #                    subject = 'Message from you discord bot',
                    #                    plain_text_content = message2,
                    #                    html_content = '<strong>and here it is</strong>'
                    #                    )
                    #     try:
                    #         sg = SendGridAPIClient(os.environ['SENDGRID_API_KEY'])
                    #         response = sg.send(message)
                    #         print(response.status_code)
                    #         print(response.body)
                    #         print(response.headers)
                    #     except Exception as e:
                    #         print(e.message)
                    elif signal == 2 or signal == 3:
                        break
                    break
            except:
                break
    except:
        await ctx.send(f"I don't know what to do with this :grimacing: **{timeInput}**....")

@bot.command()
async def pomodoro(ctx: commands.Context, sworkTime, sbreakTime):
    discordID = str(ctx.message.author.id)
    if discordID in discordInstances.keys():
        talon = discordInstances.get(discordID)
        talon.setBreakAndWorkTime(sworkTime,sbreakTime)

@bot.command()
async def startWorkTime(ctx: commands.Context):
    discordID = str(ctx.message.author.id)
    if discordID in discordInstances.keys():
        talon = discordInstances.get(discordID)
    await timer(ctx, "take a break", get_sec(talon.workTime), talon.workTime, 2, "")

@bot.command()
async def startBreakTime(ctx: commands.Context):
    discordID = str(ctx.message.author.id)
    if discordID in discordInstances.keys():
        talon = discordInstances.get(discordID)
    await timer(ctx, "get back to work", get_sec(talon.breakTime), talon.breakTime, 3, "")

def get_sec(time_str):
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

@bot.command()
async def saythnx(ctx: commands.Context):
    await ctx.send("Thank You HawkHacks2022 - by Gaurav Divecha, Vikram Prashar, Mohammad Al-Shalabi, Hanana Gohir")

bot.run(token)