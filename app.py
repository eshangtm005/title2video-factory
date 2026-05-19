from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import os
from openai import OpenAI

app = FastAPI()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <head>
        <title>Title2Video Factory</title>
    </head>
    <body style="font-family:Arial; padding:30px; text-align:center;">
        <h1>🎬 Title2Video Hindi Factory</h1>
        <form method="post" action="/create">
            <input name="title" placeholder="वीडियो टाइटल डालो"
                   style="padding:10px; width:80%;" />
            <br><br>
            <button type="submit" style="padding:12px 20px;">
                Create Video
            </button>
        </form>
    </body>
    </html>
    """

@app.post("/create")
def create_video(title: str = Form(...)):
    prompt = f"Write a 60-second viral Hindi YouTube Shorts story script for: {title}"

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    script = response.choices[0].message.content

    return {
        "title": title,
        "script": script,
        "status": "MVP working"
  }
