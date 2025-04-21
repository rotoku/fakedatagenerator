import asyncio
from ollama import AsyncClient

model_name = 'llama3.2:latest'
prompt = input("Enter your prompt: ")
async def chat():
  message = {'role': 'user', 'content': prompt}
  async for part in await AsyncClient().chat(model=model_name, messages=[message], stream=True):
    print(part['message']['content'], end='', flush=True)

asyncio.run(chat())