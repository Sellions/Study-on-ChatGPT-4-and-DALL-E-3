from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
      model="gpt-4-vision-preview",
      temperature=0,
      messages=[
              {
                        "role": "user",
                        "content": [
                                    {"type": "text", "text": "Single word that depicts what the image is."},
                                    {
                                                  "type": "image_url",
                                                  "image_url": {
                                                                  "url": "http://cogmech.ucmerced.edu/dalle/book-sellion.png",
                                                                },
                                                },
                                  ],
                      }
            ],
      max_tokens=300,
    )

print(response.choices[0].message.content)