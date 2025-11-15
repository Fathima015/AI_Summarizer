from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
from youtube_transcript_api import YouTubeTranscriptApi
import fitz
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
print("Loaded key:", os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


def get_summary(prompt):
    response = client.responses.create(
        model="gpt-3.5-turbo",
        input=prompt,
        max_output_tokens=300
    )

    # FIXED: correct way to extract text
    return response.output[0].content[0].text


@app.route("/summarize/text", methods=["POST"])
def summarize_text():
    data = request.json
    text = data['text']
    prompt = f"Summarize the following text:\n{text}"
    summary = get_summary(prompt)
    return jsonify({"summary": summary})


@app.route("/summarize/pdf", methods=["POST"])
def summarize_pdf():
    file = request.files['file']
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""

    for page in doc:
        text += page.get_text()

    prompt = f"Summarize the following PDF content:\n{text}"
    summary = get_summary(prompt)
    return jsonify({"summary": summary})


@app.route("/summarize/youtube", methods=["POST"])
def summarize_youtube():
    data = request.get_json()
    url = data['url']
    
    video_id = url.split("v=")[-1]

    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    text = " ".join([item['text'] for item in transcript])

    prompt = f"Summarize the following YouTube video transcript:\n{text}"
    summary = get_summary(prompt)
    return jsonify({"summary": summary})


if __name__ == "__main__":
    app.run(debug=True)
