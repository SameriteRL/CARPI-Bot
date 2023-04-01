import discord
from discord import app_commands
from discord.ext import commands

class Course(commands.cog):

    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @app_commands.command(name="courses", description="Displays department fall courses during a given year")
    async def courses(self, interaction:discord.Interaction, year:int, code:str):
        await interaction.response.send_message(f"{year} {code}")
    
async def setup(bot:commands.Bot):
    await bot.add_cog(Course(bot))