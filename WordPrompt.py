from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-4-0613",
  temperature=0,
  max_tokens=500,
  messages=[
    {"role": "system", "content": "Respond with the requested d\
escription using one sentence of 15-20 words."},
    {"role": "user", "content": "Describe a vivid image of the \
word 'book'."}
  ]
)

print(completion.choices[0].message.content)