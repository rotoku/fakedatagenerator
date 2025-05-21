import requests
import os

class GitHubClient:
    """Classe para interagir com a API do GitHub."""
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    BASE_URL = "https://api.github.com"

    def __init__(self):
        """Inicializa o cliente do GitHub."""
        pass

    def get_repository(self, owner: str, repo: str) -> dict:
        """Obtém os detalhes de um repositório do GitHub.

        Args:
            owner (str): O proprietário do repositório.
            repo (str): O nome do repositório.

        Returns:
            dict: Detalhes do repositório.

        Raises:
            ValueError: Se o proprietário ou o repositório estiver vazio.
            Exception: Se ocorrer um erro ao fazer a requisição.
        """
        if not owner or not repo:
            raise ValueError("O proprietário e o repositório devem ser fornecidos.")

        url = f"{self.BASE_URL}/repos/{owner}/{repo}"
        headers = {
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "Python-GitHub-Client",
            "Authorization": f"Bearer {GITHUB_TOKEN}"  # Substitua pelo seu token de acesso pessoal
        }
        payload = {}
        try:
            response = requests.request("GET", url, data=payload, headers=headers) 
            return response.json()
        except Exception as e:
            raise Exception(f"Erro ao fazer a requisição: {str(e)}")