from openai import OpenAI
import os 
from dotenv import load_dotenv
from PIL import Image
from io import BytesIO
import requests

load_dotenv()
key = os.getenv('key')

client = OpenAI(api_key=key)


# Generate and show a single image
response = client.images.generate(
        model="dall-e-3",
        prompt='Generate an image of a nice cat',
        size="1024x1024",
        quality="standard",
        n=1,
)

img = response.data[0].url
print(img)

responses = requests.get(response.data[0].url)
image = Image.open(BytesIO(responses.content))
image.show()


# Generate and save multiple images

list_images = ['An image of a horse','image of a cat']       #List containg images to generate

for i in range(len(list_images)):

    response = client.images.generate(
            model="dall-e-3",
            prompt=list_images[i],
            size="1024x1024",
            quality="standard",
            n=1,
    )
    
    responses = requests.get(response.data[0].url)
    image = Image.open(BytesIO(responses.content))
    image.save(f'Generated_image{i}.png')
