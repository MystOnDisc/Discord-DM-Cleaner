token = ""

print("Loading...")

print("Loading discord...")
import discord
from discord.ext import commands
import asyncio

print("Loading colors...")
import colorama
from colorama import Fore, Style

import os
os.system('clear')
print(f"""
{Fore.YELLOW}
=================================================
=============EPIC DISCORD DM CLEANER=============
=================================================
{Style.RESET_ALL}           
                 Made By Myst                                                                                                                       
""")

print("Epicly Logging in...")
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_connect():
    await asyncio.sleep(1)
    print(
        f"{Fore.GREEN}Epicly Logged Into {Style.RESET_ALL}{bot.user.name}#{bot.user.discriminator}\n \n"
    )
    print(f"""
{Style.RESET_ALL}
COMMANDS:
{Fore.GREEN}clear      {Fore.BLACK}- {Style.RESET_ALL}Epicly Deletes Your Messages
{Fore.GREEN}LogDm      {Fore.BLACK}- {Style.RESET_ALL}Epicly Logs DMs
{Fore.GREEN}LogGroupDm {Fore.BLACK}- {Style.RESET_ALL}Epicly Logs Group DMs
{Fore.GREEN}LogGuild   {Fore.BLACK}- {Style.RESET_ALL}Epicly Logs All Of A Server's Info  
    
{Fore.YELLOW}
=================================================
======================Myst=======================
=================================================
{Style.RESET_ALL}
""")

#########################################################

@bot.event
async def on_message_delete(message):
    if message.author == bot.user:
        pass
    else:
        if isinstance(message.channel, discord.DMChannel):
            print(
                f"{message.author} deleted a message.\n{Fore.GREEN}DM CHANNEL: {Style.RESET_ALL}@{message.channel.recipient}\nCONTENT:\n{Style.RESET_ALL}{message.content}\n \n"
            )
        else:
            print(
                f"{message.author} deleted a message.\n{Fore.GREEN}GUILD: {Style.RESET_ALL}{message.guild.name}\n{Fore.GREEN}CHANNEL: {Style.RESET_ALL}#{message.channel}\n{Fore.GREEN}CONTENT:\n{Style.RESET_ALL}{message.content}\n \n"
            )

#########################################################

@bot.event
async def on_message(message):
  if message.author.id == bot.user.id:
    if message.content == 'clear':
      async for msg in message.channel.history(limit=None):
        if msg.author == bot.user:
          try:
            await msg.delete()
          except:
            pass
         

        if message.content == "LogDm":
            await message.delete()
            channel = message.channel
            f = open(f"MESSAGE HISTORY - {channel.recipient}.txt", 'w')
            channelname = channel.recipient 
            f.write(
                f"-DM indexed with {ver}-\n \nMESSAGE HISTORY - {channelname}\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n"
            )
            messages = await channel.history(
                limit=None, oldest_first=True).flatten()
            print(f"Logging messages with {channel.recipient}...")
            for message in messages:
                f.write(f"""
{message.author.name}#{message.author.discriminator} [{message.created_at}] [{message.id}]
{message.content}
""")
            print(
                f"{Fore.GREEN}Finished logging messages with {Style.RESET_ALL}{channel.recipient}!\n"
            )
            f.close()

        if message.content == "LogGroup":
            await message.delete()
            channel = message.channel
            f = open(f"MESSAGE HISTORY - {channel.name}.txt", 'w')
            channelname = channel.name
            f.write(
                f"-DM indexed with {ver}-\n \nMESSAGE HISTORY - {channelname}\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n"
            )
            messages = await channel.history(
                limit=None, oldest_first=True).flatten()
            print(f"Logging messages in {channel.name}...")
            for message in messages:
                f.write(f"""
{message.author.name}#{message.author.discriminator} [{message.created_at}]
{message.content}
""")
            print(
                f"{Fore.GREEN}Finished logging messages in {Style.RESET_ALL}{channelname}!\n"
            )
            f.close()

        if message.content == "LogGuild":
            await message.delete()
            guild = message.guild
            print(f"Logging {guild.name}.")
            f = open(f"GUILD INFO - {guild.name}.txt", 'w')
            f.write(f"-Info grabbed with {ver}-\n")
            f.write(f"""
GUILD INFO - {guild.name}
-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
Member Count - {guild.member_count}
Guild Owner  - {guild.owner}
Guild ID     - {guild.id}
      """)
            f.write(
                "\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\nCHANNELS\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n"
            )
            for channel in message.guild.channels:
                print(channel.name)
                f.write(f"{channel.name} ({channel.id})\n")
            f.write(
                "\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\nMEMBERS\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n"
            )
            for member in guild.members:
                print(member.name)
                f.write(
                    f"{member.name}#{member.discriminator} ({member.id})\n")
            print(
                f"{Fore.GREEN}Finished logging {Style.RESET_ALL}{guild.name}!\n")
            f.close()

#########################################################

bot.run(token, bot=False)
