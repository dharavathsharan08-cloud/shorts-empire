import sys, os, googleapiclient.discovery, googleapiclient.http, telegram
youtube = googleapiclient.discovery.build("youtube","v3",developerKey=sys.argv[1])
with open("live_hook.txt") as f: title = f.read().strip()+" 😱 #Shorts"
body={"snippet":{"title":title,"description":"#illusion #Shorts","tags":["illusion","Shorts"]},"status":{"privacyStatus":"public"}}
media = googleapiclient.http.MediaFileUpload("short.mp4")
r = youtube.videos().insert(part="snippet,status",body=body,media_body=media).execute()
url = "https://youtu.be/"+r["id"]
print("UPLOADED:",url)
bot = telegram.Bot(sys.argv[2])
bot.send_message(chat_id=sys.argv[3],text="Live: "+url)
