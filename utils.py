import os
import tempfile
import uuid

import openai
from PIL import Image
from urllib import request
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_image(prompt: str, n: int, size: str) -> str:
    response = openai.Image.create(
        prompt=prompt,
        n=n,
        size=size
    )

    return response['data']

def handle_input(text: str, n: float, size: str) -> Image:
    urls = generate_image(text, int(n), size)
    image_paths = []
    for url in urls:
        image_path = os.path.join(
            tempfile.gettempdir(),
            f'{uuid.uuid1()}.png'
        )
        request.urlretrieve(
            url['url'],
            image_path)
        image_paths.append(image_path)
    return image_paths
