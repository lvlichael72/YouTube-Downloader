from pytube import YouTube
li =[]
#try:
yt = YouTube('https://www.youtube.com/watch?v=0Risn3mfyTc')
print (yt.title)
li = yt.streams.filter(progressive=True).all()
print(li)
#except OSError as err:
print("Network Error!")

