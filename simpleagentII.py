import dotenv
import os
from httpx import stream
from openai import OpenAI
import json

#Load environment variables from .env file
dotenv.load_dotenv()
if not os.getenv("GITHUB_TOKEN"):
    raise ValueError("GITHUB_TOKEN is not set.")

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o"
client = OpenAI(
    base_url=endpoint,
    api_key=token
)

