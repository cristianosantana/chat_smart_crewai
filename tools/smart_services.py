import requests, os, ast, json

class SmartServices:
    """
    Gerenciador de interações com a API Smart.
    """
    user_token = ""

    def __init__(self):
        self.auth()

    def run_external_api(self, base_url, method, route, payload):
        """
            Monta e executa requisições para o backend smart
            Args:
                base_url (str): https://smart.*
                method (str): POST, GET
                route (str): rota que chama o metodo
                payload (str): dados a serem enviados em caso de method POST
            Returns:
                Dados num formato JSON
        """
        try:
            raw = ast.literal_eval(payload) # converte string em json
            results = {}
            api_url = base_url + route # monta url
            headers = {
                "Authorization": f"Bearer " + self.user_token,
                "Content-Type": "application/json"
            }

            if method == 'GET': # Converter para maiúsculas para comparação case-insensitive
                response = requests.get(api_url, headers=headers) # Fazendo a requisição GET usando requests
                response.raise_for_status() # Levanta um erro para status codes ruins (4xx ou 5xx)
                results = response.json() # Armazenando os dados da API no dicionário de resultados
            elif method == 'POST':
                response = requests.post(api_url, json=raw, headers=headers)
                response.raise_for_status()        
                results = response.json()
            else:
                results['error'] = f"Método HTTP '{method}' não suportado para API_URL: '{api_url}'"
        except requests.exceptions.RequestException as e: # Capturando erros de requisição (conexão, timeout, etc.)
            results['error'] = f"Erro ao acessar a API_URL: '{api_url}', PAYLOAD: {payload} e EXCEPTION: {e}."
        except json.decoder.JSONDecodeError as e: # Catch JSONDecodeError specifically
            results['error'] = f"JSON Decode Error: {e}. Response Text was: '{response.text}'" # Include response text in error
        except ValueError: # Capturando erro se a resposta não for JSON válida
            results['error'] = f"Erro ao decodificar JSON da API_URL: '{api_url}': Resposta não é JSON válida."

        return results # Retorna um dicionário contendo os resultados de todas as APIs

    def auth(self):
        """
        Logar no Smart para obter token
        """
        response = self.run_external_api(os.getenv('BASE_URL'), "POST", "auth", """{"login": "cristiano.santana","password": "29102018"}""")
        self.user_token = response.get("token")
        user_name = response.get("usuario")['login']
        print(f"Usuário logado: {user_name}")
