from redbot.core import VersionInfo, version_info
from .countdown import Countdown 


async def setup(bot):
    if version_info >= VersionInfo.from_str("3.5.0"):
        await bot.add_cog(Countdown())
    else:
        bot.add_cog(Countdown())
