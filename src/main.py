from fake_data_generator import CreateDataFake
import time


class Main:
    """Classe principal da aplicação."""

    def run(self, model_name: str, prompt: str) -> None:
        """Método principal que executa a aplicação."""
        start = time.time()
        print("Aplicação em execução...")
        create_data_fake = CreateDataFake(model_name)
        response = create_data_fake.generate_data(prompt)
        end = time.time()
        print(f"{response}\n\n")
        print(f"{end - start:.2f} segundos para gerar a resposta.")


if __name__ == "__main__":
    # Instancia e executa a aplicação
    model_name="llama3.2:latest"
    prompt = input("Faça sua pergunta: ")
    app = Main()
    app.run(model_name, prompt)