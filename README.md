# OpenAI DALL-E 3 Image Generator in Python

This repository contains a simple Python script for generating images with OpenAI's DALL-E 3 model. The script shows how to generate one image, display it locally, and generate multiple images from a list of prompts.

## Project Structure

| File | Description |
| --- | --- |
| `main.py` | Main Python script for generating and saving images. |
| `requirements.txt` | Python dependencies for the project. |
| `.gitignore` | Ignores local project files. |

## Features

- Generate images from text prompts
- Use the OpenAI Python SDK
- Load the API key from a `.env` file
- Print the generated image URL
- Display the generated image locally
- Save multiple generated images as PNG files

## Requirements

- Python 3.8 or newer
- OpenAI API key
- Internet connection

Python packages:

```text
python-dotenv
openai
requests
pillow
```

## Getting Started

Clone the repository:

```bash
git clone https://github.com/Tech-Watt/OpenAI-Dall-3-image-generator-in-Python.git
cd OpenAI-Dall-3-image-generator-in-Python
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Activate it on macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## API Key Setup

Create a `.env` file in the project root:

```text
key=your_openai_api_key_here
```

The script loads the key with:

```python
load_dotenv()
key = os.getenv('key')
client = OpenAI(api_key=key)
```

Keep your `.env` file private and do not commit your API key to GitHub.

## Running the Script

Run:

```bash
python main.py
```

The script first generates a single image:

```python
response = client.images.generate(
    model="dall-e-3",
    prompt='Generate an image of a nice cat',
    size="1024x1024",
    quality="standard",
    n=1,
)
```

It prints the image URL, downloads the image, and opens it locally:

```python
img = response.data[0].url
print(img)

responses = requests.get(response.data[0].url)
image = Image.open(BytesIO(responses.content))
image.show()
```

## Generating Multiple Images

The script also includes a list of prompts:

```python
list_images = ['An image of a horse', 'image of a cat']
```

Each prompt is sent to the image generation API, downloaded, and saved as:

```text
Generated_image0.png
Generated_image1.png
```

## Customization

You can modify:

- The prompt text
- The list of image prompts
- The output image filenames
- The image size
- The image quality

Example prompt:

```python
prompt = "A futuristic city at sunset, cinematic lighting, highly detailed"
```

## Notes

- Generated image URLs are temporary, so save any images you want to keep.
- Image generation may use paid API credits.
- The current script stores the API key under the environment variable name `key`.
- For a larger app, consider renaming the variable to `OPENAI_API_KEY`.

## Author

Created by [Tech Watt](https://github.com/Tech-Watt).
