import discord
import random
from discord.ext import commands

'''user must use prefix ! when typing in command. i.e. !trackergg ____'''
client = commands.Bot(command_prefix = '!')



'''determines if bot is online'''
@client.event
async def on_ready():
    print("Bots online!")



'''determines if bot is offline'''
@client.event
async def on_disconnect():
    print("bots offline!")



'''user types valorant/general type of question in form 'valrng' or with '8ball'/'valgods'; returns a random answer in the response array'''
@client.command(aliases = ['8ball', 'valgods'])
async def valrng(ctx, *, question):
    response = ['As I see it, yes', 'Ask again later', 'Better not tell you now','Cannot predict now','Concentrate and ask again',' Don’t count on it','It is certain', 'It is decidedly so', 'Most likely',
'My reply is no', 'My sources say no', 'Outlook good', 'Outlook not so good', 'Reply hazy try again', 'Signs point to yes', 'Very doubtful', 'Without a doubt', 'Yes', 'Yes, definitely', 'You may rely on it']
    await ctx.send(f'Question: {question} \n Answer: {random.choice(response)}')



'''user gives a losses number in form of int and gives user a random amount of time given in minutes as to how long they should aimtrain given the amount of losses they have from their career page'''
@client.command(aliases = ["train"])
async def aimtrain(ctx, losses):
    if int(losses) >= 5 and int(losses) <= 10:
        response = random.randint(15,30)
    elif int(losses) <= 5 and int(losses) > 0:
        response = random.randint(0,15)
    elif int(losses) <0 or int(losses) > 11:
        await ctx.send("Type the right amount of losses you have in your career!")
    await ctx.send(f'Aim train for {response} minutes today.')



'''user is able to type in any riot id in the form of username#riot_tag (if name has spaces, just type in name without spaces) and bot returns an embedded link to the tracker.gg accoun'''
@client.command(aliases = ["track", "stats"])
async def trackergg(ctx, id):
    username = ''
    for letter in id:
        username += letter
        if letter == '#':
            break
    final = username[:-1]

    riot = id[-6:]
    if riot[2] == "#":
        riot_tag = riot[-3:]
    elif riot[1] == "#":
        riot_tag = riot[-4:]
    else:
        riot_tag = riot[-5:]
    embed = discord.Embed(title = id + "'s Valorant stats from Tracker.gg", url = "https://tracker.gg/valorant/profile/riot/{final}%23{riot_tag}/overview".format(final = final, riot_tag = riot_tag), color = discord.Color.blue())
    await ctx.send(embed=embed)
    
'''runs bot client given bot token obtained from discord website'''
client.run("insert_token_from_discord")