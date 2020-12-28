import discord
import time
from bs4 import BeautifulSoup
import requests

def gotest(list1):
    j = ""
    for i in range(len(list1)):
        j = j + list1[i]
    return j
client = discord.Client()
token="your_bot_token"

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("today check")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    check = 1
    week = ["월요일","화요일","수요일","목요일","금요일","토요일","일요일"]
    if message.content.startswith("!hello"):
        f = open('discord data/hello.txt','r')
        h = f.readlines()
        now = time.localtime()
        n = time.localtime().tm_wday
        await message.channel.send(gotest(h)+"\n"
                                   +"```"
                                   +"```"+"cs"+"\n"
                                   +"'Today is "+("%04d/%02d/%02d" % (now.tm_year, now.tm_mon, now.tm_mday))+ " " +week[n] + "'"+"\n"
                                   +"'This time is "+("%02d:%02d:%02d" % (now.tm_hour, now.tm_min, now.tm_sec))
                                   +"'```")
    if message.content.startswith("!help"):
        f = open('discord data/help.txt','r')
        h = f.readlines()
        await message.channel.send(gotest(h) + "(!미세먼지)\n```")
    if message.content.startswith("!time"):
        now = time.localtime()
        await message.channel.send("```cs"+"\n"+"'"+("%02d:%02d:%02d" % (now.tm_hour, now.tm_min, now.tm_sec))+"'```")
    if message.content.startswith("!day"):
        now = time.localtime()
        n = time.localtime().tm_wday
        await message.channel.send("```cs"+"\n"+"'"+(("%04d/%02d/%02d" % (now.tm_year, now.tm_mon, now.tm_mday))+ " " +week[n])+"'```")
    if message.content.startswith("!now"):
         now = time.localtime()
         n = time.localtime().tm_wday
         await message.channel.send("```cs"+"\n"+"'"+(("%04d/%02d/%02d" % (now.tm_year, now.tm_mon, now.tm_mday))+ " " +week[n])+"'"+"\n"
                                    +"'"+("%02d:%02d:%02d" % (now.tm_hour, now.tm_min, now.tm_sec))
                                    +"'```")
    if message.content.startswith("!fine dust") or message.content.startswith("!미세먼지") or message.content.startswith("!ozone index") or message.content.startswith("!오존지수") :
        html = requests.get("https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=0&acr=1&acq=%EB%82%A0%EC%94%A8&qdt=0&ie=utf8&query=%EB%82%A0%EC%94%A8")
        soup = BeautifulSoup(html.text, 'html.parser')
        cut = soup.find("div",{"class":"weather_box"})
        cut1 = cut.find("div",{"class":"today_area"})
        cut2 = cut1.find("dl",{"class":"indicator"})
        data = cut2.findAll("dd")
        data1 = cut2.findAll("dt")
        finaldata, finaldata1= [], ""
        for i in data:
            finaldata.append(i.text)
        for i in range(len(data1)):
            finaldata1 += '"' + (data1[i].text + " " + finaldata[i]) + '"\n'
        await message.channel.send('```cs\n' + finaldata1 + "```")
    if message.content.startswith("!weather") or message.content.startswith("!날씨"):
        html = requests.get("https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=0&acr=1&acq=%EB%82%A0%EC%94%A8&qdt=0&ie=utf8&query=%EB%82%A0%EC%94%A8")
        soup = BeautifulSoup(html.text, 'html.parser')
        cut = soup.find("div",{"class":"weather_box"})
        cut1 = cut.find("div",{"class":"today_area"})
        cut2 = cut1.find("dl",{"class":"indicator"})
        finaldata2 = '```cs\n"'
        finaldata2 += cut1.find("span",{"class":"todaytemp"}).text + cut1.find("p",{"class":"cast_txt"}).text +'"\n"' +  cut1.find("span",{"class":"merge"}).text +'"\n"' + cut1.find("p",{"class":"cast_txt"}).text
        await message.channel.send(finaldata2+'"```');


client.run(token)
f.close()
