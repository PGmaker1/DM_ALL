import discord
from discord.ext import commands
import asyncio
import googletrans
import time
import json
from discord.utils import get

with open('Setting.json','r',encoding='utF8') as Sfile:
    Sdata = json.load(Sfile)

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='''pg.''', intents=intents)

# 起動時呼叫
@bot.event
async def on_ready():
    print('''✔ I'm ready''')
    game = discord.Game('ANO遊戲社群')
    await bot.change_presence(status=discord.Status.online, activity=game)

@bot.command()
async def great(ctx):
    await ctx.send("謝謝誇獎❤❤")

@bot.command()
async def dm_all1(ctx,*, args=None):
    if args != None:
        members = ctx.guild.members
        for member in members :
            try:
                await member.send(args)
            except:
                print("noooo")
    else:
        await ctx.send("pls provide!")

@bot.command()
async def dm_all2(ctx,*, A):
    if A == "":
        await ctx.send(
        '''錯誤:請輸入要嵌入內容
        格式:
            pg.dm_all2 小標///內容
        如有任何疑問請通知豬世代#8478''')
        return
    B = A.split('///')
    print(B)
    print(len(B))
    C = (B[0])
    F = len(B)
    if F == 2:
        D = (B[1])
    if F == 1:
        D = ("** **")

    if A != None:
        members = ctx.guild.members
        for member in members :
            try:
                embed=discord.Embed(title="ANO廣播!", url="https://discord.gg/anopg", color=0x602e2e)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/926271057986482277/983564181108293682/c33e56442f8f91a8.gif")
                embed.add_field(name=C, value=D, inline=False)
                embed.add_field(name="伺服器連結", value="https://discord.gg/anopg", inline=True)
                embed.set_footer(text="from 𝓐𝓝𝓞遊戲社群|Taiwan 交友聊天", icon_url="https://cdn.discordapp.com/attachments/926271057986482277/983564181108293682/c33e56442f8f91a8.gif")
                await member.send(embed=embed)
            except:
                print("?")
    else:
        await ctx.send("請輸入 pls provide!")
    await ctx.send(embed=embed)

bot.run(Sdata['TOKEN'])