from dotenv import load_dotenv
from openai import OpenAI
import cv2
import base64
import os

load_dotenv()

key = os.getenv("OPENAI_API_KEY")
# print("OPENAI_API_KEY   :   ", key)
client = OpenAI(api_key=key)
video = cv2.VideoCapture("data/sample_video.mp4")

# Extract frames from video
base64Frames = []
while video.isOpened():
    success, frame = video.read()
    if not success:
        break
    _, buffer = cv2.imencode(".jpg", frame)
    base64Frames.append(base64.b64encode(buffer).decode("utf-8"))

video.release()
print(len(base64Frames), "frames read.\n")

# Create chat prompt
PROMPT_MESSAGES = [
    {
        "role": "user",
        "content": [
            # "These are frames from a video that I want to depict. Explain what is in the video in a summary paragraph.",
            # "These are frames from a video that I want to analyse. Please explain what is in the video in a summary with 5 bullet points each not more than 15 words.",
            "These are frames from a video that I want to analyse. Please explain what is in the video in a summary in bullet points in 100 words.",
            *map(lambda x: {"image": x, "resize": 768}, base64Frames[0::150]),
        ],
    },
]

params = {
    "model": "gpt-4o",
    "messages": PROMPT_MESSAGES,
    "max_tokens": 300,
}

result = client.chat.completions.create(**params)
print(result.choices[0].message.content)
