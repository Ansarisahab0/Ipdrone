import openai

openai.api_key = "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"
system_message = {
  "role": "system",
  "content": "You are a helpful assistant that can assist me with any questions or tasks I have."
}

user_message = {
  "role": "user",
  "content": "What is the weather like today?"
}

messages = [system_message, user_message]
completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=messages
)

response = completion.choices[0].message.content
print(response)
