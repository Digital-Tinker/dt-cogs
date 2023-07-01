from redbot.core import commands
import base64

class Crypto(commands.Cog):
    """Cryptography commands for CTF Challenges"""

    @commands.command()
    async def b64decode(self, ctx, arg):
        """Decode Base64 strings"""
        clrtext = base64.b64decode(arg)
        await ctx.send(clrtext.decode('UTF-8'))

    @commands.command()
    async def asciiToText(self, ctx, *args):
        """Decode ASCII to text"""
        await ctx.send(''.join(chr(int(i)) for i in args))

    @commands.command()
    async def reverseText(self, ctx, arg):
        """Reverses text. Primarily to reverse binary endianness"""
        rStr = arg[::-1]
        await ctx.send(rStr)

    @commands.command()
    async def binToDec(self, ctx, arg):
        """Converts Binary to Decimal"""
        await ctx.send(int(arg,2))

    @commands.command()
    async def numToLetters(self, ctx, *args):
        """Converts the numbers 1-26 to letters a-z (A1Z26)"""
        await ctx.send(''.join(chr(int(i)+96) for i in args))

    @commands.command()
    async def pNum(self, ctx, arg):
        """Calculates the prime numbers in a given integer"""
        i = 2
        f = []
        nr = int(arg)
        while i <= nr:
            if (nr % i) == 0:
                f.append(i)
                nr = nr / i
            else:
                i = i +1
        await ctx.send({i:f.count(i) for i in f})
