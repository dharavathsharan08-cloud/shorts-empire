import os, requests, datetime, google.generativeai as genai
NICHE = "optical illusion"
YT_KEY = os.getenv("YT_API_KEY")
GEMINI_KEY = os.getenv("GEMINI_KEY")

# grab today’s top Shorts titles
search = "https://www.googleapis.com/youtube/v3/search"
params = {"part":"snippet","q":NICHE,"type":"video","videoDuration":"short","maxResults":15,
          "publishedAfter":(datetime.datetime.utcnow()-datetime.timedelta(hours=24)).isoformat("T")+"Z","key":YT_KEY}
titles = [i["snippet"]["title"] for i in requests.get(search,params=params).json().get("items",[])]
genai.configure(api_key=GEMINI_KEY)
best = genai.GenerativeModel("gemini-1.5-flash").generate_content(
        f"Pick the highest-CTR hook from these titles (return only 1):\n{titles}").text.strip()
with open("live_hook.txt","w") as f: f.write(best)
print("hook:",best)
