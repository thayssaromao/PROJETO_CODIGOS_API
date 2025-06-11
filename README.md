# 🏫 PROJETO FINAL: CÓDIGOS DO AMANHÃ 🎓

## 📄 Descrição do Projeto
A **HowBanks Consulting** 🌟, uma empresa especializada em consultoria de dados 📊, firmou um contrato super importante com o **Governo Federal** 🇧🇷 para realizar análises com os dados disponíveis no **Brasil.IO** 📂. 

Cada equipe será responsável por explorar e analisar os dados provenientes da API, e o **dataset escolhido foi o PROUNI 2018** 📚, uma fonte rica de informações sobre educação e bolsas de estudo! Isso permitirá gerar insights sobre:
- 🌍 **Distribuição de bolsas de estudo**  
- 👩‍🎓 **Perfil dos beneficiários**  
- 📈 **Impactos sociais das políticas públicas educacionais**

Essa análise será fundamental para entender os efeitos sociais do PROUNI e fornecer sugestões valiosas para aprimorar as políticas educacionais no Brasil. 🇧🇷✨

----------------------------------------ORGANIZACAO------------------------------------------------------ 
## 📂 Estrutura de Diretórios do Projeto: `PROJETO_FINAL_CODIGOSAMANHA`

```plaintext
PROJETO_FINAL_CODIGOSAMANHA/
├── src/ 📁            # Diretório principal onde está o código-fonte do projeto.
├── pycache/ 📦        # Arquivos de cache gerados automaticamente pelo Python.
├── dependencias_codigo/ ⚙️
│   ├── variaveis_constantes/ 📋
│   │   ├── infos_conexao_database.py 🔑
│   │   ├── map_status_conexao.py 📶
│   │   ├── token_api.py 🔐
│   └── ConectApi.py 🌐
│   └── ConectDatabase.py 💾
│   └── DatabaseOperations.py 🛠️
├── main.py 🚀         # Arquivo principal para executar o projeto.
```

---

## 🛠️ Trecho de Código em Python: Definindo o Mapeamento de Status HTTP 🚦

Aqui está um exemplo divertido de como traduzir códigos de status HTTP para mensagens amigáveis ao usuário usando Python! 🐍👇

```python
status_map = {
    200: "✅ Autenticação bem-sucedida!",
    201: "📦 Recurso criado com sucesso!",
    204: "🤷‍♂️ Nenhum conteúdo retornado (requisição OK).",
    400: "❌ Requisição inválida! Verifique os dados enviados.",
    401: "🔑 Token inválido ou expirado!",
    403: "🚫 Sem permissão para acessar este recurso!",
    404: "🔍 Recurso não encontrado! Verifique a URL.",
    405: "⛔ Método HTTP não permitido!",
    408: "⌛ Tempo de requisição esgotado (timeout).",
    429: "🕐 Muitas requisições! Aguarde um momento.",
    500: "💥 Erro interno do servidor! Tente novamente.",
    503: "📛 Serviço indisponível! O servidor pode estar sobrecarregado.",
}
```

---

## 💻 Classe para Conexão com o Banco de Dados: PostgreSQL 🐘
```python
# ConectDatabase.py
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

```

---

## ✨ Conclusão
Este projeto traz à tona o **potencial dos dados educacionais** 📊 para **analisar políticas públicas** e impactar positivamente a sociedade! 🚀 A estrutura bem organizada e o uso de boas práticas no desenvolvimento tornam este sistema robusto e pronto para crescer! 💪
Aqui está o seu **Model-Driven (MD)** estruturado no formato **Markdown**:

---------------------------------------ESTRUTURA DO BANCO DE DADOS-------------------------------------- 

 Representa a estrutura do banco de dados e seus relacionamentos com foco em entidades, atributos e lógica.

---

## 1️⃣ **Entidade: Instituicoes**

**Descrição:** Representa as informações básicas sobre as instituições de ensino.

### 📄 **Atributos**

| Campo   | Tipo        | Descrição                                  |
|---------|--------------|----------------------------------------------|
| `id`   | INT (PK)   | Identificador único da instituição.        |
| `nome` | VARCHAR     | Nome da instituição.                       |
| `cidade` | VARCHAR   | Cidade onde a instituição está localizada. |

---

## 2️⃣ **Entidade: Cursos**

**Descrição:** Representa os cursos oferecidos pelas instituições.

### 📄 **Atributos**

| Campo                     | Tipo        | Descrição                                  |
|---------------------------|--------------|----------------------------------------------|
| `id`                     | INT (PK)   | Identificador único do curso.             |
| `instituicao_id`          | INT (FK)   | Chave estrangeira referenciando a instituição. |
| `nome_curso`             | VARCHAR     | Nome do curso.                             |
| `mensalidade`            | DECIMAL     | Valor da mensalidade do curso.            |
| `nota_integral_ampla`    | FLOAT       | Nota de corte para bolsas integrais ampla. |
| `nota_parcial_ampla`     | FLOAT       | Nota de corte para bolsas parciais ampla. |
| `bolsas_integral_ampla`  | INT         | Quantidade de bolsas integrais amplas.    |
| `bolsas_parcial_ampla`   | INT         | Quantidade de bolsas parciais amplas.     |

---

## 3️⃣ **Entidade: BolsaAmplaInstituicao**

**Descrição:** Contém informações sobre a quantidade total de bolsas integrais disponíveis em cada instituição.

### 📄 **Atributos**

| Campo                   | Tipo        | Descrição                                  |
|-------------------------|--------------|----------------------------------------------|
| `instituicao`          | VARCHAR     | Nome da instituição.                       |
| `total_bolsas_integral` | INT         | Total de bolsas integrais disponíveis.    |

---

## 4️⃣ **Entidade: CursosMensalidade**

**Descrição:** Representa dados específicos sobre a mensalidade dos cursos.

### 📄 **Atributos**

| Campo              | Tipo        | Descrição                                  |
|--------------------|--------------|----------------------------------------------|
| `instituicao`      | VARCHAR     | Nome da instituição.                       |
| `nome_curso`       | VARCHAR     | Nome do curso.                             |
| `mensalidade`      | DECIMAL     | Valor da mensalidade do curso.            |

---

## 5️⃣ **Entidade: NotaCorteBolsas**

**Descrição:** Contém as informações sobre as notas de corte para bolsas de estudo oferecidas por cada instituição e curso.

### 📄 **Atributos**

| Campo                | Tipo        | Descrição                                  |
|----------------------|--------------|----------------------------------------------|
| `instituicao`       | VARCHAR     | Nome da instituição.                       |
| `nome_curso`        | VARCHAR     | Nome do curso.                             |
| `nota_integral`     | FLOAT       | Nota de corte para bolsas integrais.       |
| `nota_parcial`      | FLOAT       | Nota de corte para bolsas parciais.       |
| `diferenca_notas`   | FLOAT       | Diferença entre as notas integrais e parciais. |

---

## 🔗 **Relacionamentos**

### 1. **Instituicoes - Cursos**
- **Tipo:** Relacionamento 1:N  
- **Descrição:** Cada instituição pode estar associada a vários cursos.  
- **Chave estrangeira:**  
  - `cursos.instituicao_id` referencia `instituicoes.id`.

### 2. **Instituicoes - BolsaAmplaInstituicao**
- **Tipo:** Relacionamento 1:1  
- **Descrição:** Cada instituição possui apenas uma quantidade total de bolsas integrais disponíveis.  
- **Chave estrangeira:**  
  - `bolsaampla_instituicao.instituicao` referencia `instituicoes.nome`.

### 3. **CursosMensalidade**
- **Relacionamento com `instituicoes`:** Representa mensalidades específicas de cada curso dentro de cada instituição.

### 4. **NotaCorteBolsas**
- **Relacionamentos:** Relaciona-se com os cursos e suas respectivas notas de corte em relação às bolsas de estudo.

---

## 📊 **Diagrama Conceitual**

Aqui seria inserido um diagrama de entidades e relacionamentos (ERD), representando as tabelas e suas interligações. O diagrama deve conter as tabelas:

- `instituicoes`
- `cursos`
- `bolsaampla_instituicao`
- `cursos_mensalidade`
- `nota_corte_bolsas`

Os relacionamentos devem estar alinhados conforme as regras definidas acima.

---

## 🛠️ **Finalidade**

Facilitar o desenvolvimento e implementação por meio da definição clara das estruturas e relacionamentos no banco de dados, garantindo que as entidades sejam bem relacionadas e otimizando consultas e operações no sistema.

---------------------------------------BANCO DE DADOS COM PSYCOPG2-------------------------------------- 
### Explicação do Código: Como Conectar e Operar em um Banco de Dados PostgreSQL com `psycopg2` 🐘

O código apresentado é um exemplo prático de como realizar operações em um banco de dados PostgreSQL utilizando o Python e a biblioteca **`psycopg2`**. Ele é estruturado para ser modular, reutilizável e seguro. Abaixo está uma explicação detalhada dos principais componentes:

---

### **1. Conexão com o Banco de Dados: Classe `ConectDatabase`**

Esta classe é responsável por estabelecer a conexão com o banco de dados e fornecer um **cursor**, que será usado para executar comandos SQL.

#### **Funcionamento:**
- **Inicialização (`__init__`)**:
  - Recebe um dicionário contendo as credenciais de conexão, como `host`, `dbname`, `user`, e `password`.
  - Estas informações são armazenadas na instância da classe.
- **Método `obter_cursor`**:
  - Usa as credenciais para tentar conectar ao banco utilizando a função `psycopg2.connect()`.
  - Se a conexão for bem-sucedida, retorna dois objetos:
    1. O **cursor**, usado para executar comandos SQL.
    2. A **conexão**, que é necessária para confirmar transações.
  - Em caso de erro (por exemplo, credenciais erradas), exibe uma mensagem clara e retorna `None` para o cursor e a conexão.

#### **Por que usar esta classe?**
Ela separa a lógica de conexão do restante do código, permitindo reutilização e facilitando o tratamento de erros relacionados à conexão.

---

### **2. Inserção de Dados: Classe `DatabaseOperations`**

A classe **`DatabaseOperations`** é projetada para realizar operações no banco de dados, começando pela **inserção de dados**.

#### **Funcionamento do Método `comando_insercao_sql`:**
- Recebe dois parâmetros principais:
  1. O comando SQL de inserção (por exemplo, `INSERT INTO tabela VALUES (%s, %s)`).
  2. Os valores a serem inseridos, como uma **tupla**.
- Usa a classe `ConectDatabase` para obter a conexão e o cursor.
- Executa o comando SQL com os parâmetros fornecidos e confirma a transação com `conexao.commit()`.
- Em caso de erro (por exemplo, um comando SQL malformado), exibe uma mensagem detalhada.
- Sempre fecha a conexão e o cursor, mesmo se ocorrerem exceções, para evitar desperdício de recursos.

#### **Exemplo Prático:**
Se quisermos adicionar um novo registro à tabela `minha_tabela`, podemos passar o comando:
```sql
INSERT INTO minha_tabela (coluna1, coluna2) VALUES (%s, %s)
```
E os valores correspondentes, como:
```python
("valor1", "valor2")
```
A transação será automaticamente salva no banco.

---

### **3. Consulta de Dados: Método `comando_select_sql`**

Este método é uma extensão da classe `DatabaseOperations` e permite executar comandos SQL do tipo **`SELECT`** para buscar informações no banco de dados.

#### **Funcionamento:**
- Assim como o método de inserção, ele usa a conexão e o cursor fornecidos por `ConectDatabase`.
- Recebe o comando SQL de consulta e parâmetros opcionais.
- Executa a consulta e utiliza `cursor.fetchall()` para retornar todos os resultados como uma lista de tuplas.
- Trata erros como comandos SQL malformados e sempre fecha a conexão e o cursor após a execução.

#### **Exemplo Prático:**
Suponha que você queira buscar todos os registros onde `coluna1 = 'valor1'`. O comando seria:
```sql
SELECT coluna1, coluna2 FROM minha_tabela WHERE coluna1 = %s
```
E o parâmetro:
```python
("valor1",)
```
O método retorna os resultados da consulta, que podem ser iterados no código.

---

### **4. Gerenciamento de Recursos e Tratamento de Erros**

Um ponto crucial deste código é o **gerenciamento de recursos**:
- Sempre que uma conexão ou cursor é aberto, ele é fechado no final, mesmo que ocorra uma exceção. Isso evita **vazamentos de recursos**, como conexões abertas desnecessariamente no banco.
- Mensagens de erro claras são exibidas para ajudar a identificar problemas, seja na conexão ou na execução dos comandos SQL.

---

### **Resumo: Fluxo Geral do Código**

1. **Conexão**:
   - A classe `ConectDatabase` estabelece uma conexão segura com o banco, retornando o cursor e a conexão.
2. **Inserção**:
   - A classe `DatabaseOperations` executa comandos de inserção, utilizando o cursor para enviar os dados ao banco.
3. **Consulta**:
   - O mesmo processo é usado para buscar informações no banco com comandos `SELECT`.
4. **Encerramento**:
   - Após cada operação, a conexão e o cursor são fechados, garantindo eficiência no uso dos recursos do banco de dados.

---

### **Conclusão**

Este código é uma solução robusta e reutilizável para interagir com bancos de dados PostgreSQL:
- É modular: cada classe tem uma responsabilidade clara.
- Seguro: gerencia recursos corretamente e trata erros de forma eficaz.
- Flexível: pode ser facilmente expandido para incluir operações adicionais, como `UPDATE` e `DELETE`.

Você pode usar este padrão para criar aplicações que precisem de interações frequentes com o banco de dados, como sistemas de cadastro, dashboards de relatórios ou APIs que consultem informações em tempo real. 🎉
---------------------------------------CODIGO EM PYTHON------------------------------------------------- 
### Explicação Detalhada do Código: Conectando Dados da API com Banco de Dados

Este guia explora dois trechos de código integrados: um para conexão com a **API externa** e outro para armazenar dados no **banco de dados**. O script faz uso de práticas modernas, validando dados, evitando duplicações e tratando erros de forma robusta.

---

## 🚀 **Código 1: Conectando-se à API com Autenticação**

O primeiro trecho da aplicação é responsável por estabelecer uma conexão segura com uma API externa.

### **Objetivo**
Criar uma classe (`ConectApi`) que gerencia a autenticação com token, faz requisições HTTP e trata respostas e exceções.

---

### **Componentes do Código**

#### 1️⃣ **Importações Necessárias**

```python
from dependencias_codigo.variaveis_constantes.map_status_conexao import status_map
import requests
```

- **`status_map`**: Mapeia códigos de status HTTP para mensagens amigáveis.
- **`requests`**: Biblioteca para realizar requisições HTTP.

---

#### 2️⃣ **Classe `ConectApi`**

```python
class ConectApi:
```
A classe é criada para encapsular operações com a API, incluindo autenticação via token e chamadas GET.

---

### **Método `__init__`**

```python
def __init__(self, url_base, rota, token):
    self.requisicao = f"{url_base}/{rota}"
    self.token = token
```

- **`url_base` + `rota`**: A URL da API é construída concatenando esses dois elementos.
- **`token`**: Recebido para autenticar as requisições.

---

### **Configuração de Headers**

```python
def configurar_headers(self):
    return {'Authorization': f'Token {self.token}'}
```
Configura o cabeçalho HTTP com autenticação via token.

---

### **Chamada da API**

```python
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
```

**Explicação do Fluxo:**
1. **`requests.get`**: Faz a requisição GET para a URL configurada.
2. **Mensagens amigáveis**: O código de status da resposta é traduzido com `status_map`.
3. **Validação**:
   - Se o status for `200 OK`, retorna os dados no formato JSON.
   - Caso contrário, retorna `None`.
4. **Tratamento de exceções**:
   - Caso haja erro no envio da requisição, uma mensagem é exibida.

---

## 🏗️ **Código 2: Integrando com Banco de Dados**

Agora, a API retorna dados no formato JSON. O script principal (`main.py`) recupera esses dados e os insere em um banco de dados.

---

### **Objetivo**
Extrair dados da resposta da API e armazenar informações relevantes no banco de dados, manipulando corretamente dados ausentes e evitando duplicações.

---

### Importações Principais

```python
from dependencias_codigo.variaveis_constantes.token_api import token
from dependencias_codigo.variaveis_constantes.infos_conexao_database import database_config
from ConectDatabase import ConectDatabase
from DatabaseOperations import DatabaseOperations
from ConectApi import ConectApi
```

**Função das Importações:**
1. **`token`**: Token de autenticação para a API.
2. **`database_config`**: Contém detalhes de conexão com o banco de dados.
3. **Classes Importadas**:
   - `ConectDatabase`: Gerencia a conexão com o banco.
   - `DatabaseOperations`: Realiza operações no banco (inserção, consulta).
   - `ConectApi`: Gerencia as chamadas HTTP.

---

### Estrutura da Função `main`

```python
def main():
    # Variáveis para a requisição
    url_base = "https://api.brasil.io/v1"
    rota = "dataset/cursos-prouni/cursos/data/"
```

Define a URL base da API e a rota para acessar os dados relevantes.

---

### Conexão com a API

```python
conectApi = ConectApi(url_base, rota, token)
dados = conectApi.json_api()  # Obtém dados no formato JSON
```

- Instancia a classe `ConectApi`.
- Chama o método `json_api` para buscar os dados na API.

---

### Conexão com o Banco de Dados

```python
conectDatabase = ConectDatabase(database_config)
databaseOperations = DatabaseOperations(conectDatabase)
```

1. **`ConectDatabase(database_config)`**: Configura a conexão com o banco.
2. **`DatabaseOperations`**: Objeto responsável por realizar operações no banco.

---

### Iteração Sobre os Dados da API

```python
for dado in dados["results"]:
    instituicao_nome = dado.get("universidade_nome")
    cidade = dado.get("cidade_busca")

    if instituicao_nome and cidade:
        insert_instituicao = """
        INSERT INTO Instituicoes (nome, cidade)
        VALUES (%s, %s);
        """
        databaseOperations.comando_insercao_sql(insert_instituicao, (instituicao_nome, cidade))
```

**Passos:**
1. Itera sobre cada item em `dados["results"]`.
2. Extrai dados da resposta da API com `dado.get`.
3. Valida se os dados são válidos (não `None`) antes da inserção.
4. Executa o comando SQL para inserir dados na tabela `Instituicoes`.

---

### Consulta para Obter o ID da Instituição Inserida

```python
instituicao_id_result = databaseOperations.comando_select_sql("""
SELECT id FROM Instituicoes WHERE nome = %s;
""", (instituicao_nome,))
```

- Recupera o ID da instituição para usar em operações futuras.

---

### Inserção de Dados no Banco de Dados - Tabela Cursos

```python
if curso_nome and mensalidade is not None:
    insert_curso = """
    INSERT INTO Cursos (
        instituicao_id, nome_curso, mensalidade,
        bolsas_integral_ampla, bolsas_parcial_ampla,
        nota_integral_ampla, nota_parcial_ampla
    ) VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    databaseOperations.comando_insercao_sql(insert_curso, (
        instituicao_id, curso_nome, mensalidade,
        bolsas_integral_ampla if bolsas_integral_ampla else 0,
        bolsas_parcial_ampla if bolsas_parcial_ampla else 0,
        nota_integral_ampla if nota_integral_ampla else 0.0,
        nota_parcial_ampla if nota_parcial_ampla else 0.0
    ))
```

**Análise do Fluxo:**
1. Valida se o curso é válido com `curso_nome` e `mensalidade`.
2. Insere dados no banco, tratando valores nulos com valores padrão (0 ou 0.0).

---

## ✨ **Conclusão**

O código principal une várias tecnologias e práticas modernas:
1. **Segurança** com autenticação via token.
2. **Validação de dados** antes de inserção no banco.
3. **Gerenciamento de erros**, tratando exceções na requisição ou ao manipular dados.
4. **Prevenção de duplicações** com verificações no banco.

O código pode ser utilizado por desenvolvedores para integrar APIs e armazenar dados de forma robusta e estruturada.
## ⚙️ **Observação**

O código começou a realizar a operação no seguinte intervalo de tempo:

- **⏱ Tempo de início:** 17:50h  
- **⏱ Tempo de fim:** 20:00h  

Além disso, o processo apresentou um tempo médio de **4 segundos para cada dado inserido no banco de dados**.

## 👥 Autores
[Ageu Moraes](https://www.linkedin.com/in/ageu-felipe-nunes-moraes-98b688268/)

[Thayssa Romão](https://www.linkedin.com/in/thayssa-rom%C3%A3o-31a94424b/)

Mozart Dias

Rafael Machado
