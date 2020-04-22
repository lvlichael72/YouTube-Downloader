from pytube import YouTube
import wget
#li =[]
#try:
yt = YouTube('https://www.youtube.com/watch?v=0Risn3mfyTc')
title = yt.title
thumb = wget.download (yt.thumbnail_url)
print(thumb)
#print (yt.title)
#li = yt.streams.filter(progressive=True).all()
#print(li)
#except OSError as err:
#print("Network Error!")

