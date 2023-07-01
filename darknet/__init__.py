from .darknet import Darknet


async def setup(bot):
    await bot.add_cog(Darknet())
