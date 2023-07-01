import asyncio
import datetime
import pytz
from redbot.core import commands

# old message:  I don't know why you bother, it is going to be cancelled again anyway...

class Countdown(commands.Cog):
    """Countdown to DEF CON"""

    @commands.command()
    async def cuntdown(self, ctx):
        """I was such a nice bot before -_-"""
        await ctx.send("En.v, Look what you have started....")
        utc_now = pytz.utc.localize(datetime.datetime.utcnow()) 
        pst_now = utc_now.astimezone(pytz.timezone("America/Los_Angeles"))
        defcon_start = pytz.timezone("America/Los_Angeles").localize(datetime.datetime(2023,8,10))
        delta = defcon_start - pst_now
        await ctx.send(str(delta) + " until DEF CON 31. Did that count as flood?") 

    @commands.command()
    async def countdown(self, ctx): 
        """Countdown to DEF CON"""
        utc_now = pytz.utc.localize(datetime.datetime.utcnow())
        pst_now = utc_now.astimezone(pytz.timezone("America/Los_Angeles"))
        defcon_start = pytz.timezone("America/Los_Angeles").localize(datetime.datetime(2023,8,10))
        delta = defcon_start - pst_now
        await ctx.send(str(delta) + " until DEF CON 31. Let's hope there is less plague next year.")
