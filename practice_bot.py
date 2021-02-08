import discord
import asyncio
import datetime

from discord import user

client = discord.Client()

token = "ODA3OTM2MTczODc1MDAzNDMy.YB_PMg.0hedvzINSI1GGBwzfFmLYeHHxD8"

@client.event
async def on_ready():

    print(client.user.name)
    print("성공적으로 봇이 시작되었습니다.")
    game = discord.Game("나도 같이 개발")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content == "!PFinnifer":
        await message.channel.send("잘생김!!!!!!!!!!!!!")

    if message.content == "!H8UN":
        await message.channel.send("잘생김?")

    if message.content == "!rlatodms":
        await message.channel.send("김세은(엿)")

    if message.content == "!임베드":
        embed = discord.Embed(title="피스 구독하기", description="좋아요도 누르기", color=0x00ff00)
        embed.add_field(name="안누르면 김태읍읍", value="싫으면 읍읍읍", inline=True)
        embed.set_footer(text="구독자 1억명을 원합니다")
        await message.channel.send(embed=embed)

    if message.content.startswith("!청소"):
        number = int(message.content.split(" ")[1])
        await message.delete()
        await message.channel.purge(limit=number)
        await message.channel.send(f"{number}개의 메세지 삭제 완료함!")

    if message.content == "!내정보":
        user = message.author
        date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
        await message.channel.send(f"{message.author.mention}의 가입일 : {date.year}/{date.month}/{date.day} 임!")
        await message.channel.send(message.author.avatar_url)
        await message.channel.send(f"{message.author.mention}의 이름 : {user.name}, 아이디 : {user.id}, 닉네임 : {user.display_name} 임!")

client.run(token)