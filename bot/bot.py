from pathlib import Path 
import discord
from discord.ext import commands
import sqlite3
class GiveawayBot(commands.Bot):
    def __init__(self):
        self._cogs=[p.stem for p in Path(".").glob("./bot/cogs/*.py")]
        super().__init__(command_prefix=self.prefix, case_insensitive=True, intents=discord.Intents.all())
    def setup(self):
        print("Running Setup.....")
        for cog in self._cogs:
            self.load_extension(f"bot.cogs.{cog}")
            print(f"Loaded {cog} cog.")
        print("Setup Complete.")
    
    def run(self,version):
        self.setup()

        with open("./data/token.0", "r", encoding="utf-8") as f:
            TOKEN = f.read() 
        
        self.VERSION = version
        print("Running the bot")
        super().run(TOKEN,reconnect=True)
        
    async def on_ready(self):
        print(f"Bot ready.")
    async def prefix(self,bot,msg):
        db = sqlite3.connect("Config.db")
        cursor = db.cursor()
        x = cursor.execute(f"SELECT prefix FROM config WHERE guild_id = {msg.guild.id}")
        y = x.fetchone()
        if y == None:
            return commands.when_mentioned_or("g!")(bot,msg)
        else:
            return commands.when_mentioned_or(y[0],"g!")(bot,msg)