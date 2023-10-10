import asyncio
from globals import *
from time import sleep
from datetime import date, datetime

from discord.ext import commands
from cogs.calendar.academic_cal import events_from_webpage, getMonthAndDate
import calendar
from datetime import date, datetime, timedelta, timezone

class AcadCal(commands.Cog) :
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(description="Prints the current month's calendar and events.",
                             aliases=["cal"])
    async def print(self, ctx):
        
        dates = events_from_webpage()
        acadCalendar = getMonthAndDate(dates)

        # Create an emded for the message
        embedVar = discord.Embed(
            title=f"Upcoming Events for {calendar.month_name[datetime.now().month]}",
            description=f"```\n{acadCalendar[0]}\n```",
        )

        for event in acadCalendar[1]:
            embedVar.add_field(
                name = event['date'],
                value = event['event'],
                inline=False
            )

        await ctx.send(embed=embedVar)
    
    @print.error
    async def print_calendar_error(self, ctx, error):
        print(error)

    
async def setup(bot):
    await bot.add_cog(AcadCal(bot))
