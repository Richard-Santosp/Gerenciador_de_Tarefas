import mysql.connector

class Database_connector:
    def __init__(self, host, password, user, database):
        self.host = host
        self.password = password
        self.user = user
        self.database = database
        self.conn = None

    # Realizando a conexão com o banco de dados
    def conectar(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                password=self.password,
                user=self.user,
                database=self.database,
            )
            return self.conn
        except mysql.connector.Error as e:
            print(f'Erro de conexão com o banco de dados: {e}')
            return None

    # Realizando a pesquisa de email e senha no banco de dados 
    def pesquisar_usuario(self, email, senha):
        if not self.conn:
            if not self.conectar():
                return None
        try:
            cursor =  self.conn.cursor()
            query = 'SELECT * FROM usuarios WHERE email = %s AND senha = %s'
            params = (email, senha)
            cursor.execute(query, params)
            resultado = cursor.fetchall()
            cursor.close()
            return resultado
        except mysql.connector.errors as err:
            print(err)

    # Enviando os dados passados na aba de cadastro ao banco de dados
    def enviar_cadastro(self, email, nome, senha):
        envio = None
        if not self.conn:
            if not self.conectar():
                return None
        try:
            cursor = self.conn.cursor()
            operation = 'INSERT INTO set_order.usuarios (email, nome , senha) VALUES (%s, %s, %s)'
            params = (email, nome, senha)
            cursor.execute(operation, params)
            self.conn.commit()
            cursor.close()
            envio = True
            return envio
        except Exception as err:
            print('erro!: ', err)

    # realizar o fechamento da conexão
    def close_connection(self):
        self.conn.close()
    
    # Verifica se o email que o usuário colocou no cadastro ja consta no banco de dados 
    def verificacao_de_usuario(self, email):
        if not self.conn:
            if not self.conectar():
                return None
        try:
            cursor =  self.conn.cursor()
            query = f'SELECT * FROM usuarios WHERE email = "{email}"'
            cursor.execute(query)
            resultado = cursor.fetchall()
            cursor.close()
            return resultado
        except Exception as e:
            print(f'Erro:{e}')