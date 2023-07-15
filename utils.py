import os

import openai
from PIL import Image
from urllib import request
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_image(prompt: str) -> str:
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512"
    )

    return response['data'][0]['url']

def handle_input(text: str) -> Image:
    url = generate_image(text)
    print(url)
    request.urlretrieve(
        url,
        "sample.png")
    image = Image.open('sample.png')
    return image
