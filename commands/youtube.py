import json, os
import urllib.request as ur
from datetime import datetime

#Help vars

#base call
call = "youtube"
#Help text
helpText = "Don't be stupid"

#You need to make youtubeToken.txt and paste a youtube api token in it.
#using a .txt file, not a .py file to keep setup simple
with open('youtubeToken.txt', 'r') as f:
    TOKEN = f.read().strip("\n")

ChannelID = 'UC0YagOInbZxj10gaWwb1Nag'

target = 'https://www.googleapis.com/youtube/v3/search?part=snippet&channelId={0}&maxResults=1&order=date&key={1}'.format(ChannelID, TOKEN)

def getJson(url):

    return json.loads((ur.urlopen(url).read()).decode('utf-8'))

def _youtube():
    json = getJson(target)

    videoid = json['items'][0]['id']['videoId']
    title = json['items'][0]['snippet']['title']
    publishedDate = json['items'][0]['snippet']['publishedAt'].split('T')[0]
    publishedTime = json['items'][0]['snippet']['publishedAt'].split('T')[1]

    year, month, day = publishedDate.split('-')
    date = datetime(int(year), int(month), int(day))
    date = date.strftime("%B %d, %Y")
    time = publishedTime.split('.')[0]

    return "Latest Video: **{0}**\nPublished on **{1}** at {2}\nLink: https://www.youtube.com/watch?v={3}".format(title, date, time, videoid)
