from os import name
import discord
from discord.ext import commands
import asyncio
from discord.ext.commands.errors import CommandInvokeError
import random
import datetime
import time

class Listeners(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        pass
    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"?help | Version: {self.bot.VERSION}"))

def setup(bot):
    bot.add_cog(Listeners(bot))