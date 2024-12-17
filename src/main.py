from dependencias_codigo.variaveis_constantes.token_api import token
from dependencias_codigo.variaveis_constantes.infos_conexao_database import database_config
from ConectDatabase import ConectDatabase
from DatabaseOperations import DatabaseOperations
from ConectApi import ConectApi

def main():
    # Variáveis para a requisição
    url_base = "https://api.brasil.io/v1"
    rota = "dataset/cursos-prouni/cursos/data/"

    # Acessa a API
    conectApi = ConectApi(url_base, rota, token)
    dados = conectApi.json_api()  # Obtém os dados no formato JSON

    # Conecta ao banco de dados
    conectDatabase = ConectDatabase(database_config)
    databaseOperations = DatabaseOperations(conectDatabase)

    # Itera sobre os dados recebidos da API para inserir nas tabelas
    for dado in dados["results"]:  # Considerando que 'results' contém os registros
        # Desestruturação dos dados da API
        instituicao_nome = dado.get("universidade_nome")
        cidade = dado.get("cidade_busca")
        
        # Somente inserimos dados válidos para a tabela Instituicoes
        if instituicao_nome and cidade:
            # Inserção na tabela Instituicoes (verifica duplicidade com UPSERT)
            insert_instituicao = """
                INSERT INTO Instituicoes (nome, cidade)
                VALUES (%s, %s);
            """
            databaseOperations.comando_insercao_sql(insert_instituicao, (instituicao_nome, cidade))

            # Recupera o ID da instituição recém-inserida ou existente
            instituicao_id_result = databaseOperations.comando_select_sql("""
                SELECT id FROM Instituicoes WHERE nome = %s;
            """, (instituicao_nome,))

            if instituicao_id_result:
                instituicao_id = instituicao_id_result[0][0]

                # Desestruturação dos dados do curso
                curso_nome = dado.get("nome")
                mensalidade = dado.get("mensalidade")
                bolsas_integral_ampla = dado.get("bolsa_integral_ampla")
                bolsas_parcial_ampla = dado.get("bolsa_parcial_ampla")
                nota_integral_ampla = dado.get("nota_integral_ampla")
                nota_parcial_ampla = dado.get("nota_parcial_ampla")

                # Verifica se os dados do curso são válidos
                if curso_nome and mensalidade is not None:
                    # Inserção na tabela Cursos
                    insert_curso = """
                        INSERT INTO Cursos (
                            instituicao_id, nome_curso, mensalidade,
                            bolsas_integral_ampla, bolsas_parcial_ampla,
                            nota_integral_ampla, nota_parcial_ampla
                        ) VALUES (%s, %s, %s, %s, %s, %s, %s);
                    """
                    # Passando os parâmetros para inserção, tratando valores nulos adequadamente
                    databaseOperations.comando_insercao_sql(insert_curso, (
                        instituicao_id, curso_nome, mensalidade,
                        bolsas_integral_ampla if bolsas_integral_ampla is not None else 0,
                        bolsas_parcial_ampla if bolsas_parcial_ampla is not None else 0,
                        nota_integral_ampla if nota_integral_ampla is not None else 0.0,
                        nota_parcial_ampla if nota_parcial_ampla is not None else 0.0
                    ))

if __name__ == "__main__":
    main()
