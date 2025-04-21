from ollama import generate


class CreateDataFake():
    def __init__(self, model_name):
        self.model_name = model_name

    def generate_data(self, prompt: str):
        """Gera dados falsos para teste."""
        response = generate(self.model_name, prompt=prompt)
        return response['response']