from discord.ext import tasks,commands
from colorama import init as coloinit
from colorama import Fore, Style
import discord
import os


client = commands.Bot(command_prefix=',',intents=discord.Intents.all())
coloinit(autoreset=True,wrap=True)

@client.event
async def on_ready():
    print(f'{Fore.GREEN}Bot is ready! {Style.RESET_ALL}User is {Fore.CYAN}{client.user}')

@client.command(name='ping',help='Tells the ping of the bot.',brief='Shows the bot\'s ping.')
async def ping_command(ctx):
    await ctx.send(f'Pong! My ping is {round(client.latency*1000,1)} ms.')

extensions = [
    'cogs.levels'
]

if __name__ == '__main__':
    for extension in extensions:
        client.load_extension(extension)

client.run(os.environ['TOKEN'])
