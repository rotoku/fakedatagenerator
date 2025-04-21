from ollama import chat
from ollama import ChatResponse



prompt = input("Enter your prompt: ")
response: ChatResponse = chat(model='llama3.2', messages=[
  {
    'role': 'user',
    'content': prompt,
  },
])

print(response.message.content)