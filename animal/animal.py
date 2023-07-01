# Post animal pics by Eslyium#1949 & Yukirin#0048
# Modified by DigitalTinker

# Discord
import discord

# Red
from redbot.core import commands

# Libs
import aiohttp

catapi = "https://shibe.online/api/cats"
dogapi = "https://dog.ceo/api/breeds/image/random"
foxapi = "http://wohlsoft.ru/images/foxybot/randomfox.php"
pugapi = "http://pugme.herokuapp.com/random"
gsdapi = "https://dog.ceo/api/breed/germanshepherd/images/random"
bunnyapi = "https://api.bunnies.io/v2/loop/random/?media=gif,png"
shibaapi = "https://dog.ceo/api/breed/shiba/images/random"

BaseCog = getattr(commands, "Cog", object)


class Animal(BaseCog):
    """Animal commands."""

    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession()
        self.catapi = catapi
        self.dogapi = dogapi
        self.foxapi = foxapi
        self.pugapi = pugapi
        self.gsdapi = gsdapi
        self.bunnyapi = bunnyapi
        self.shibaapi = shibaapi

    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.guild)
    async def cat(self, ctx):
        """Shows a cat"""
        try:
            async with self.session.get(self.catapi) as r:
                result = await r.json()
            await ctx.send(result[0])
        except:
            await ctx.send("API Error. Probably just a hiccup.\nIf this error persist for several days, please report it")

    @commands.command()
    @commands.cooldown(1, 120, commands.BucketType.guild)
    async def cats(self, ctx, amount : int = 5):
        """Throws a cat bomb!

        Defaults to 5, max is 10"""
        results = []
        if amount > 10 or amount < 1:
            amount = 5
        try:
            for x in range(0,amount):
                async with self.session.get(self.catapi) as r:
                    api_result = await r.json()
                    results.append(api_result[0])
            await ctx.send("\n".join(results))
        except:
            await ctx.send("API Error. Probably just a hiccup.\nIf this error persist for several days, please report it")

    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.guild)
    async def dog(self, ctx):
        """Shows a dog"""
        try:
            async with self.session.get(self.dogapi) as r:
                result = await r.json()
            await ctx.send(result['message'])
        except:
            await ctx.send("API Error. Probably just a hiccup.\nIf this error persist for several days, please report it")

    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.guild)
    async def gsd(self, ctx):
        """Shows a German Shepherd"""
        try:
            async with self.session.get(self.gsdapi) as r:
                result = await r.json()
            await ctx.send(result['message'])
        except:
            await ctx.send("API Error. Probably just a hiccup.\nIf this error persist for several days, please report it")

    @commands.command()
    @commands.cooldown(1, 120, commands.BucketType.guild)
    async def dogs(self, ctx, amount : int = 5):
        """Throws a dog bomb!

        Defaults to 5, max is 10"""
        results = []
        if amount > 10 or amount < 1:
            amount = 5
        try:
            for x in range(0,amount):
                async with self.session.get(self.dogapi) as r:
                    api_result = await r.json()
                    results.append(api_result['message'])
            await ctx.send("\n".join(results))
        except:
            await ctx.send("API Error. Probably just a hiccup.\nIf this error persist for several days, please report it")

    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.guild)
    async def fox(self, ctx):
        """Shows a fox"""
        try:
            async with self.session.get(self.foxapi) as r:
                result = await r.json()
            await ctx.send(result['file'])
        except:
            await ctx.send("API Error. Probably just a hiccup.\nIf this error persist for several days, please report it")

    @commands.command()
    @commands.cooldown(1, 120, commands.BucketType.guild)
    async def foxes(self, ctx, amount : int = 5):
        """Throws a fox bomb!

        Defaults to 5, max is 10"""
        results = []
        if amount > 10 or amount < 1:
            amount = 5
        try:
            for x in range(0,amount):
                async with self.session.get(self.foxapi) as r:
                    api_result = await r.json()
                    results.append(api_result['file'])
            await ctx.send("\n".join(results))
        except:
            await ctx.send("API Error. Probably just a hiccup.\nIf this error persist for several days, please report it")

    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.guild)
    async def shiba(self, ctx):
        """Shows a Shiba"""
        try:
            async with self.session.get(self.shibaapi) as r:
                result = await r.json()
            await ctx.send(result['message'])
        except:
            await ctx.send("API Error. Probably just a hiccup.\nIf this error persist for several days, please report it")

    @commands.command()
    @commands.cooldown(1, 120, commands.BucketType.guild)
    async def shibas(self, ctx, amount : int = 5):
        """Throws a shiba bomb!

        Defaults to 5, max is 10"""
        results = []
        if amount > 10 or amount < 1:
            amount = 5
        try:
            for x in range(0,amount):
                async with self.session.get(self.shibaapi) as r:
                    api_result = await r.json()
                    results.append(api_result['message'])
            await ctx.send("\n".join(results))
        except:
            await ctx.send("API Error. Probably just a hiccup.\nIf this error persist for several days, please report it")

    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.guild)
    async def bunny(self, ctx):
        """Shows a bunny"""
        try:
            async with self.session.get(self.bunnyapi) as r:
                result = await r.json()
            await ctx.send(result['media']['poster'])
        except:
            await ctx.send("API Error. Probably just a hiccup.\nIf this error persist for several days, please report it")

    @commands.command()
    @commands.cooldown(1, 120, commands.BucketType.guild)
    async def bunnies(self, ctx, amount : int = 5):
        """Throws a bunny bomb!

        Defaults to 5, max is 10"""
        results = []
        if amount > 10 or amount < 1:
            amount = 5
        try:
            for x in range(0,amount):
                async with self.session.get(self.bunnyapi) as r:
                    api_result = await r.json()
                    results.append(api_result['media']['poster'])
            await ctx.send("\n".join(results))
        except:
            await ctx.send("API Error. Probably just a hiccup.\nIf this error persist for several days, please report it")

    @commands.command()
    @commands.cooldown(1, 120, commands.BucketType.guild)
    async def gulo(self, ctx):
        """Shows a Gulo"""
        try:
            await ctx.send("<:gulootchi:742478339389915166>".format(""))
        except:
            await ctx.send("Tinker broke it again")

    def cog_unload(self):
        self.bot.loop.create_task(self.session.close())

    __del__ = cog_unload

