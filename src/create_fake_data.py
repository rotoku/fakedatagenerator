import requests
import json
import csv
import time
from typing import List, Dict, Any


def create_ollama_prompt() -> str:
    """
    Create a prompt for the Ollama API.
    """
    return """Generate fake data for 5 people in CSV format with these columns:
    first_name, last_name, email_address, age, city, occupation
    Please only return the raw CSV data without any additional text or explanation."""

def call_ollama_api(prompt: str) -> List[str]:
    """
    Call the Ollama API with the given prompt and return the response.
    """
    url = "http://localhost:11434/api/generate"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    data = {
        "model": "llama3.2:latest",
        "prompt": prompt,
        "temperature": 0.5,
        "stream": False,
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response.raise_for_status()
    return response.json()

def main():
    """
    Main function to create fake data and save it to a CSV file.
    """
    prompt = create_ollama_prompt()
    response = call_ollama_api(prompt)
    
    if response and 'response' in response:
        output_file = "fake_data.csv"
        with open(output_file, "a", newline="") as f:
            f.write(f"{response['response']}\n")
        print(f"Fake data has been saved to {output_file}")
    else:
        print("Failed to generate fake data.")

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"\n\n{end - start:.2f} segundos para gerar a resposta.")