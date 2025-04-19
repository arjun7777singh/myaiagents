import dotenv
from httpx import stream
from openai import OpenAI
import os

#Load environment variable from .env file.
dotenv.load_dotenv()
if not os.getenv("GITHUB_TOKEN"):
    raise ValueError("GITHUB_TOKEN is not set")

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o"

client = OpenAI(
    base_url=endpoint,
    api_key=token
)

response = client.chat.completions.create(
    messages=[
        {
            "role":"system",
            "content":"You are a Data Structure and Algorithms Teacher"
        },
        {
            "role":"user",
            "content":"Explain Depth First Search for Binary Tree Data Structure in detail."
        }
    ],
    temperature=1.0,
    top_p=1.0,
    max_tokens=1000,
    model=model_name,
    stream=True,
    stream_options={'include_usage':True}
)
usage = None
for update in response:
    if update.choices and update.choices[0].delta:
        print(update.choices[0].delta.content or "", end="")
    if update.usage:
        update = update.usage

if usage:
    print("\n")
    for k,v in usage.dict().items():
        print(f"{k}={v}")

