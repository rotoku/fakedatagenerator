from ollama import generate

model_name="llama3.2:latest"
prompt = "Why is the sky blue?"
while prompt != ":q!":
    # Read the prompt from the terminal
    prompt = input("Enter your prompt: ")

    response = generate(model_name, prompt=prompt)
    print(response['response'])

print("Exiting the program.")