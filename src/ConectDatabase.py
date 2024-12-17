import psycopg2

# Classe para conectar com o banco de dados
class ConectDatabase:
    # Informações para a conexão com o banco de dados
    def __init__(self, conexao_database):
        self.conexao_database = conexao_database

    # Retorna o cursor
    def obter_cursor(self):
        try:
            # Estabelece a conexão e retorna o cursor dentro do contexto
            conexao = psycopg2.connect(**self.conexao_database)
            return conexao.cursor(), conexao
        except Exception as e:
            print(f"Erro ao tentar conectar: {str(e)}")
            return None, None
        