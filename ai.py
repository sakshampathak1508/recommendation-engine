import openai

# Set up your OpenAI API credentials
openai.api_key = 'YOUR_API_KEY'

# Function to generate image caption using OpenAI API
def generate_image_caption(image_path):
    # Read and encode the image
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()
    encoded_image = base64.b64encode(image_data).decode('utf-8')
    
    # Generate the caption using the OpenAI API
    response = openai.Completion.create(
        engine='davinci',
        prompt='Caption this image: ' + encoded_image,
        max_tokens=50,  # Adjust the number of tokens as per your preference
        temperature=0.7  # Adjust the temperature parameter for diversity of outputs
    )
    
    # Extract the caption from the API response
    caption = response.choices[0].text.strip()
    
    return caption

# Example usage
image_path = 'path_to_image_file'
caption = generate_image_caption(image_path)
print(f"Generated caption: {caption}")

import requests
from PIL import Image
import torch

# Function to generate image from text using DALL-E
def generate_image_from_text(text):
    # Encode text into a numerical representation
    input_text = torch.tensor(tokenizer.encode(text)).unsqueeze(0)
    
    # Send a request to the DALL-E model API
    response = requests.post(
        'https://api.openai.com/v1/engines/davinci-codex/completions',
        headers={'Authorization': 'Bearer YOUR_API_KEY'},
        json={
            'prompt': input_text.tolist(),
            'max_tokens': 512,
        }
    )
    
    # Extract the image data from the API response
    image_data = response.json()['choices'][0]['image']
    
    # Decode the image data and return the generated image
    image = Image.open(BytesIO(base64.b64decode(image_data)))
    return image

# Example usage
text = "A yellow cat with blue eyes"
generated_image = generate_image_from_text(text)
generated_image.show()
