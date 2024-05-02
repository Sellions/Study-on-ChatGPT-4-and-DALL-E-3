import base64
from openai import OpenAI
client = OpenAI()

response = client.images.generate(
      model="dall-e-3",
      response_format="b64_json",
      prompt="use the following prompt as the 'revised_prompt' with no changes or additions: A book is a bound collection of printed\
 pages filled with knowledge, stories, or images.",
      size="1024x1024",
      style="vivid",
      quality="standard",
      n=1,
    )

with open("/var/www/html/dalle/book-sellion.png","wb") as f:
        f.write(base64.decodebytes(bytes(response.data[0].b64_json,"utf-8")))