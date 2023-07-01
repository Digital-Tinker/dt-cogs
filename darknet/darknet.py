from redbot.core import commands
import json
import requests
from requests.auth import HTTPBasicAuth
from requests import Session
import numpy as np

import api_key

class Darknet(commands.Cog):
    """My custom cog"""

    @commands.command()
    async def whois(self, ctx):
        """Gives a brief description of TITS Holon"""
        tits = ("The TITS Holon is a virtual holon that participates in the DC Darknet contest at DEFCON\n" \
                "Our holon focuses on building the community and helping everyone learn. To learn more\n" \
                "about the DC Darknet contest, visit https://darknet-ng.network")
        await ctx.send(tits)

    @commands.command()
    async def Themis(self, ctx):
        """Scale of Themis"""
        themis =("The Scale of Themis is tipped towards distributed power at 31.95% based on 241 agents earning a minimum of 6 points to an average of 195.4 points")
        await ctx.send(themis)

    @commands.command()
    async def Leaderboard(self, ctx):
       leaderboard = "The current Top 10 Standings are:"
       response = requests.get("https://darknet-ng-continual.ctfd.io/api/v1/scoreboard")
       data = json.loads(response.text)
       players = data["data"]
       x = range(10)
       for i in x:
           leaderboard += "\n" + str(i+1) + ". " + players[i]["name"] + " (" + str(players[i]["score"]) + ")"
       await ctx.send(leaderboard)

    @commands.command()
    async def Scales(self, ctx):
       url = "https://darknet-ng-11.ctfd.io/api/v1/scoreboard"
       s = Session()
       s.headers.update({"Authorization": f"Token {API_KEY}"})
       response = s.get(url, json=True)
       if response:
           data = json.loads(response.text)
       else:
           await ctx.send("No data found")
       players = data["data"]
       scores = []
       numPlayers = 0

       for player in players:
           if player["score"] > 6:
               scores.append(player["score"])
               numPlayers += 1

       mad=np.abs(np.subtract.outer(scores, scores)).mean()
       rmad = mad/np.mean(scores)
       g = 0.5 * rmad
       gPercent = round((g*100), 2)
       if gPercent < 50:
           gText = "The Scales of Themis are tipped towards distributed power at " + str(gPercent) + "% based on " + str(numPlayers) + " agents earning a minimum of 6 points"
       elif gPercent > 50:
           gText = "The Scales of Themis are tipped towards centralized power at " + str(gPercent) + "% based on " + str(numPlayers) + " agents earning a minimum of 6 points"
       await ctx.send(gText)

    @commands.command() 
    async def LBTits(self, ctx):
       tits = ["fnord","MotoPsych0","feath3rz","En.V","Prox","hartaman"]
       url = "https://darknet-ng-11.ctfd.io/api/v1/scoreboard"
       s = Session()
       s.headers.update({"Authorization": f"Token {API_KEY}"})
       response = s.get(url, json=True)
       data = json.loads(response.text)
       players = data["data"]
       lbTITS = "TITS Leaderboard"

       for player in players:
           for tit in tits:
               if player["name"] == tit:
                   lbTITS += "\n" + str(player["pos"]) + ". " + player["name"] + " (" + str(player["score"]) + ")"
       
       await ctx.send(lbTITS)

    @commands.command()
    async def DTScore(self, ctx):
        data = json.loads(requests.get("https://darknet-ng-continual.ctfd.io/api/v1/users/15"))
        player = data["data"]
        await ctx.send(player["score"])
