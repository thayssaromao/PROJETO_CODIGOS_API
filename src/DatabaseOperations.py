# Classe para inserir dados ao banco de dados
class DatabaseOperations:
    # Cria uma instância da conexão com o banco de dados
    def __init__(self, instancia_ConectDatabase):
        self.instancia_ConectDatabase = instancia_ConectDatabase

    # Método para executar inserção SQL
    def comando_insercao_sql(self, comando, parametros=None):
        # Usando o with para obter o cursor e a conexão
        cursor, conexao = self.instancia_ConectDatabase.obter_cursor()

        if conexao and cursor:
            try:
                # Se houver parâmetros, passamos para a execução
                if parametros:
                    cursor.execute(comando, parametros)
                else:
                    cursor.execute(comando)  # Caso não haja parâmetros
                conexao.commit()  # Garantir que a inserção seja salva no banco
                print("Dados inseridos com sucesso!")
            except Exception as e:
                print(f"Erro ao inserir dados: {str(e)}")
            finally:
                # Fechar o cursor e a conexão manualmente
                cursor.close()
                conexao.close()
        else:
            print("Falha ao obter cursor ou conexão.")

    # Permite passar um comando de query
    def comando_select_sql(self, comando, parametros=None):
        # Obtém o cursor e a conexão manualmente
        cursor, conexao = self.instancia_ConectDatabase.obter_cursor()

        if conexao and cursor:
            try:
                # Se houver parâmetros, passamos para a execução
                if parametros:
                    cursor.execute(comando, parametros)
                else:
                    cursor.execute(comando)  # Caso não haja parâmetros

                # Obtém todos os resultados da consulta
                resultados = cursor.fetchall()
                return resultados  # Retorna os dados obtidos
            except Exception as e:
                print(f"Erro ao executar consulta SELECT: {str(e)}")
                return None
            finally:
                # Fechar o cursor e a conexão manualmente
                cursor.close()
                conexao.close()
        else:
            print("Falha ao obter cursor.")
            return None
