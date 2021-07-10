from discord.ext import tasks,commands
from colorama import init as coloinit
from colorama import Fore, Style
import discord
import sys,os
import json


coloinit(autoreset=True,wrap=True)


class Levels(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command(name='rank',
    aliases=['lvl','level'],
    help='Checks your level. If you ping someone, it checks their level! Uses embeds.',
    brief='Checks your level.')
    async def check_level(self,ctx,member=None):

        with open('levels.json','r') as f:
            levels = json.load(f)

        if member == None:
            member = ctx.author
        
        embed = discord.Embed(
            title=f'{member.display_name}\'s {ctx.guild.name} Leveling Statistics',
            color=0x663399
        )

        level = levels['dudes'][str(member.id)]['level']
        exp = levels['dudes'][str(member.id)]['exp']
        needed_exp = ((level ** 0.77) * 30) + 10
        percent_done = round((exp/needed_exp)*100,1)

        embed.add_field(name='Level',value=str(level))
        embed.add_field(name='EXP', value=str(exp)+'/'+str(needed_exp)+' ['+str(percent_done)+']')

        await ctx.send(embed=embed)
    