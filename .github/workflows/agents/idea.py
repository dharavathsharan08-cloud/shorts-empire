import google.generativeai as genai, os, datetime
genai.configure(api_key=os.getenv("GEMINI_KEY"))
hook = open("live_hook.txt").read().strip()
prompt = f"""Create a 12-second optical-illusion concept for YouTube Shorts.
Rules:
- Visual only, no voice
- Impossible 3-D shape rotating
- Must loop seamlessly
- End with 1-frame white flash
Output only the shape description (≤25 words)."""
idea = genai.GenerativeModel("gemini-1.5-flash").generate_content(prompt).text.strip()
with open("idea.txt","w") as f: f.write(idea)
print("idea:",idea)
