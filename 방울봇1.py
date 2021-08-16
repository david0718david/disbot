import discord
from discord import message
from discord.ext import commands
import random
import asyncio
import datetime
import sqlite3
import json
import youtube_dl
import re
import urllib
from bs4 import BeautifulSoup
from discord.ext import commands
from discord.ext.commands import bot
from discord.ext.commands import has_permissions
from discord.ext import commands
import asyncio
from discord.ext import commands
import asyncio
from youtube_search import YoutubeSearch
import youtube_dl
import urllib
import re
from discord.ext import commands, tasks
from discord.ext import commands
from youtube_dl import YoutubeDL
import bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from discord.utils import get
from discord import FFmpegPCMAudio
import time



bot = commands.Bot(command_prefix='ㅂ')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_ready() :
    print(f'방울봇 준비완료 : {bot.user.name}!')
    game = discord.Game("ㅂ도움말") #
    await bot.change_presence(status = discord.Status.online, activity = game)

@bot.event
async def on_member_join(member):
    channel = get(member.server.channels, name="general")
    await bot.send_message(channel,"우리서버에 잘왔다 멍!")


@bot.command(name="따라해")
async def repeat(ctx, *, txt):
    await ctx.send(txt)

@bot.command() 
async def 봇정보(ctx) :
         embed = discord.Embed(title="이름", description="방울이", color=0x62c1cc) 
         embed.add_field(name= "아이디", value ="865419608667455498",inline = False) 
         embed.add_field(name="개발자", value="ㅎㅎ#5909",inline = False)
         embed.add_field(name="생일",value="7월 19일",inline = False)
         embed.add_field(name="활동하는 서버의 수",value=f"{len(bot.guilds)}",inline = False)
         embed.add_field(name="사용언어",value="파이썬",inline = False)
         embed.add_field(name="접두사",value="ㅂ",inline = False)
         embed.add_field(name="초대링크",value="https://discord.com/api/oauth2/authorize?client_id=865419608667455498&permissions=8&scope=bot ",inline = False)
         embed.add_field(name="방울봇 공식서버",value="https://discord.gg/DZWwGNEW9C",inline = False)
         embed.set_footer(text = f"{ctx.message.author.name} | 님이 명령어를 사용했습니다.", icon_url = ctx.message.author.avatar_url)
         await ctx.send(embed=embed)
    
@bot.command()
async def 내정보(ctx):
     embed = discord.Embed(title = f"{ctx.message.author.name}님의 유저정보입니다",color = 0x62c1cc)
     embed.add_field(name= "이름", value =f"{ctx.message.author.name}",inline = False)
     embed.add_field(name= "아이디", value =f"{ctx.author.id}",inline = False)
     embed.set_image(url=ctx.author.avatar_url)
     embed.set_footer(text = f"{ctx.message.author.name} | 님이 명령어를 사용했습니다.", icon_url = ctx.message.author.avatar_url)
     
     await ctx.send(embed=embed)













@bot.command()
async def 투표(ctx, title, *choice):
    '''
    투표
    :param title: 투표 제목
    :param choice: 선택지 (최대 9개)
    '''
    if title is None and choice == ():
        embed = discord.Embed(title= "투표 도움말", description= f"{ctx.message.author.name}님이 요청함")
        embed.add_field(name="좋아요/싫어요", value= "!투표 제목")
        embed.add_field(name="복수응답(1-9)", value= "!투표 제목 내용1 내용2 ...")
        await ctx.send(embed=embed)

    

    else:
        embed = discord.Embed(title=title,color=0x62c1cc)
        if choice == ():
            
            message = await ctx.send(embed=embed)
            await message.add_reaction('👍')
            await message.add_reaction('👎')
         
        else:
            
            emoji_list = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣']  

            s = ''
            emoji = iter(emoji_list)
            for cont in choice:
                try:
                    s += f'{next(emoji)} {cont}\n'
                except ValueError:
                    await ctx.sent('두표 항목은 9개까지만 있다멍!')
                    return

          
            embed.add_field(name=s, value='여러분의 의견을 투표로 알려줘라 멍!')
            message = await ctx.send(embed=embed)
           

          
            for i in range(len(choice)):
                await message.add_reaction(emoji_list[i])
    
@bot.command()
async def 투표도움말(ctx):
    embed = discord.Embed(description = "투표 (항목)으로 투표해봐요 항목이 여러개인 경우는 투표 (제목) (항목) (항목) 등으로 이용하실수있습니다",color=0x62c1cc)
    await ctx.send(embed=embed)
    
    






@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command(name="서버수")
async def guild_count(ctx):
      await ctx.send(f"{len(bot.guilds)}개의 서버참여 중이다 멍!")

@bot.event
async def on_meber_join(meber):
    await meber.send("어서와라 멍!")

@bot.command()
async def 핑(ctx) :
         embed = discord.Embed(title = ':ping_pong: 퐁!', description = f"{str(round(bot.latency*1000))} ms",color=0x62c1cc)
         embed.set_footer(text = f"{ctx.message.author.name} | 님이 명령어를 사용했습니다.", icon_url = ctx.message.author.avatar_url)
         await ctx.send(embed=embed)

@bot.command()
async def 초대(ctx) :
         embed = discord.Embed(title = "https://discord.com/api/oauth2/authorize?client_id=865419608667455498&permissions=8&scope=bot \n초대 부탁 드린다 멍!!! ",color=0x62c1cc)
         embed.set_footer(text = f"{ctx.message.author.name} | 님이 명령어를 사용했습니다.", icon_url = ctx.message.author.avatar_url)
         await ctx.send(embed=embed)

@bot.command()
async def 랜덤(ctx) :
      await ctx.send("1부터 100가지 수중에서 아무수나 부릅니다.")
      await asyncio.sleep(1)
      await ctx.send(random.randint(1,100)) 


@bot.command()
async def 방울이1(ctx) :
     embed = discord.Embed(title = "방울이1 사진입니다",color = 0x62c1cc)
     embed.set_image(url='https://cdn.discordapp.com/attachments/862574218485956638/867886698121527316/KakaoTalk_20210716_112859108.jpg' )
     await  ctx.send(embed=embed)

@bot.command()
async def 방울이2(ctx) :
     embed = discord.Embed(title = "방울이2 사진입니다",color = 0x62c1cc)
     embed.set_image(url='https://cdn.discordapp.com/attachments/841507635672776725/871711175782588436/KakaoTalk_20210627_194716657.jpg' )
     await  ctx.send(embed=embed)

@bot.command()
async def 방울이3(ctx) :
     embed = discord.Embed(title = "방울이3 사진입니다",color = 0x62c1cc)
     embed.set_image(url='https://cdn.discordapp.com/attachments/841507635672776725/871711202693234718/KakaoTalk_20210423_211238396.jpg' )
     await  ctx.send(embed=embed)

@bot.command()
async def 방울이4(ctx) :
     embed = discord.Embed(title = "방울이4 사진입니다",color = 0x62c1cc)
     embed.set_image(url='https://cdn.discordapp.com/attachments/841507635672776725/871718234750078986/KakaoTalk_20210802_203506386.jpg' )
     await  ctx.send(embed=embed)
@bot.command()
async def 방울이5(ctx) :
     embed = discord.Embed(title = "방울이5 사진입니다",color = 0x62c1cc)
     embed.set_image(url='https://cdn.discordapp.com/attachments/841507635672776725/871718258196246558/KakaoTalk_20210802_203506123.jpg' )
     await  ctx.send(embed=embed)

@bot.command()
async def 방울이6(ctx) :
     embed = discord.Embed(title = "방울이6 사진입니다",color = 0x62c1cc)
     embed.set_image(url='https://cdn.discordapp.com/attachments/841507635672776725/871718264118579251/KakaoTalk_20210802_203505357.jpg' )
     await  ctx.send(embed=embed)
@bot.command()
async def 방울이7(ctx) :
     embed = discord.Embed(title = "방울이7 사진입니다",color = 0x62c1cc)
     embed.set_image(url='https://cdn.discordapp.com/attachments/841507635672776725/871718269495672882/KakaoTalk_20210802_203505833.jpg' )
     await  ctx.send(embed=embed)


@bot.command()
async def 프사(ctx) :
     embed = discord.Embed(title =  f"{ctx.message.author.name}" + "님의 프사", color=0x62c1cc)
     embed.set_image(url=ctx.author.avatar_url)
     await ctx.send(embed=embed)

@bot.command()
async def  방울봇공식서버(ctx) :
         embed = discord.Embed(title = "https://discord.gg/DZWwGNEW9C \n들어와 달라멍!!! ",color=0x62c1cc)
         embed.set_footer(text = f"{ctx.message.author.name} | 님이 명령어를 사용했습니다.", icon_url = ctx.message.author.avatar_url)
         await ctx.send(embed=embed)
     
@bot.command()
async def hellothisisverification(ctx) :
        embed = discord.Embed(title = "ㅎㅎ#5909 ",color = 0x62c1cc)
        embed.set_footer(text = f"{ctx.message.author.name} | 님이 명령어를 사용했습니다.", icon_url = ctx.message.author.avatar_url)
        await ctx.send(embed=embed)

@bot.command(name="청소", pass_context=True)
async def _clear(ctx, *, amount=5):
    await ctx.channel.purge(limit=amount)
    embed = discord.Embed(description = " 정상적으로 청소가되었다 멍!",color=0x62c1cc)
    embed.set_footer(text = f"{ctx.message.author.name} | 님이 명령어를 사용했습니다.", icon_url = ctx.message.author.avatar_url)
    await ctx.send(embed=embed)
   


@bot.command()
async def 사이트(ctx):
    await ctx.send('https://discord.com/developers/docs/intro')

@bot.command()
async def 도움말(ctx) :
         embed = discord.Embed(title="기본설명", description="봇개발자는 ㅎㅎ#5909 이고 접두사는 ㅂ 입니다.", color=0x62c1cc) 
         embed.add_field(name="ㅂ초대",value="방울봇에 초대링크를 보냅니다",inline = False)
         embed.add_field(name="ㅂ서버수",value="방울이가 활동중인 서버수를 임배드로 출력합니다",inline = False)
         embed.add_field(name="ㅂ초대",value="방울봇에 초대링크를 보냅니다",inline = False)
         embed.add_field(name="ㅂ방울이1,2,3,4,5,6,7",value="귀여운 방울이의 사진을 보여줍니다",inline = False)
         embed.add_field(name="ㅂ핑",value="컴퓨터의 핑을 측정합니다.",inline = False)
         embed.add_field(name="ㅂhellothisisverification ",value="개발자 확인 명령어 입니다",inline = False)
         embed.add_field(name="ㅂ봇정보",value="봇의 정보를 임배드로 출력합니다",inline = False)
         embed.add_field(name="ㅂ따라해", value="방울이가 말을 따라합니다",inline = False)
         embed.add_field(name="ㅂ랜덤",value="1부터 100까지 수중에서 랜덤한 숫자를 부릅니다",inline = False)
         embed.add_field(name="ㅂ투표 ",value="ㅂ투표도움말을 입력해보세요",inline = False)
         embed.add_field(name="ㅂ프사",value="당신의 프사를 임배드로 출력합니다.",inline = False)
         embed.add_field(name="ㅂ방울봇공식서버",value="공식서버링크를 출력합니다.",inline = False)
         embed.add_field(name="ㅂ내정보",value="유저의 정보를 임배드로 출력합니다.",inline = False)
         embed.add_field(name="ㅂ나가",value="방울이가 음성채널에서 나갑니다",inline = False)
         embed.add_field(name="ㅂ재생 (링크)",value="방울이가 링크를 통해 노래를 재생합니다",inline = False)
         embed.add_field(name="ㅂ정지",value="음악을 끝냄니다",inline = False)
         embed.add_field(name="ㅂ청소(원하는숫자)",value="원하는 숫자만큼 청소를 합니다",inline = False)
         embed.add_field(name="도움을 주신분",value="Army\njin^^*~\nTanat#5542",inline = False)
         embed.set_footer(text = f"{ctx.message.author.name} | 님이 명령어를 사용했습니다.", icon_url = ctx.message.author.avatar_url)
         await ctx.send(embed=embed)


@bot.command()
async def 나가(msg):
    await msg.voice_client.disconnect()

@bot.command()
async def 들어와(msg,*,channel:discord.VoiceChannel = None):
    if channel == None:
        channel = msg.author.voice.channel
    if msg.voice_client is not None:
        await msg.voice_client.move_to(channel)
    else:
        await channel.connect()


        
        
@bot.command()
async def 정지(ctx):
    if bot.voice_clients[0].is_playing():
    	bot.voice_clients[0].stop()
    else:
    	await ctx.send("노래가 재생되지않고 있어요")



@bot.command()
async def 경로(ctx, url):
    channel = ctx.author.voice.channel
    if bot.voice_clients == []:
    	await channel.connect()
    	await ctx.send("재생할채널: " + str(bot.voice_clients[0].channel))

    ydl_opts = {'format': 'bestaudio'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
    voice = bot.voice_clients[0]
    voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS)) 
    embed = discord.Embed(title = "노래가 재생 된다 멍!",color = 0x62c1cc)
    embed.add_field(name= "노래링크", value ="현재" + url + "을(를) 재생하고 있습니다.") 
    await  ctx.send(embed=embed)


@bot.command()
async def 재생(ctx, *, msg):
 
    vc = ctx.voice_client
    if not vc.is_playing():
        global entireText
        YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
            
        chromedriver_dir = r"C:\Users\hohoy\OneDrive\바탕 화면\노래"
        driver = webdriver.Chrome(chromedriver_dir)
        driver.get("https://www.youtube.com/results?search_query="+msg+"+lyrics")
        source = driver.page_source
        bs = bs4.BeautifulSoup(source, 'lxml')
        entire = bs.find_all('a', {'id': 'video-title'})
        entireNum = entire[0]
        entireText = entireNum.text.strip()
        musicurl = entireNum.get('href')
        url = 'https://www.youtube.com'+musicurl 

        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        await ctx.send(embed = discord.Embed(title= "노래 재생", description = "현재 " + entireText + "을(를) 재생하고 있습니다.", color = 0x00ff00))
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
    else:
        await ctx.send("이미 노래가 재생 중이라 노래를 재생할 수 없어요!")






bot.run('ODY1NDE5NjA4NjY3NDU1NDk4.YPDu0Q.a4EPHdeFy9DiX4RW6LP_Sthl1tA')