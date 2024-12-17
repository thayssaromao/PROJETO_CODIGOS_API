from dependencias_codigo.variaveis_constantes.map_status_conexao import status_map
import requests

# Classe para acessar a API
class ConectApi:
    # Captura todos os dados para acessar a API
    def __init__(self, url_base, rota, token):
        self.requisicao = f"{url_base}/{rota}"
        self.token = token
    
    # Configura os headers para a API
    def configurar_headers(self):
        return {'Authorization': f'Token {self.token}'}
    
    # Conecta na API E traz o Json
    def json_api(self):
        try:
            response = requests.get(self.requisicao, headers=self.configurar_headers())
            mensagem = status_map.get(response.status_code, f"Erro inesperado: {response.status_code}")
            print(mensagem)

            if response.status_code == 200:
                return response.json()
            return None
        
        except requests.exceptions.RequestException as e:
            print(f"Erro na conexão: {e}")
            return None
