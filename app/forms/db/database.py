import mysql.connector

class Database_connector:
    def __init__(self, host, password, user, database):
        self.host = host
        self.password = password
        self.user = user
        self.database = database
        self.conn = None

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
            # self.conn.close()
            return resultado
        except mysql.connector.errors as err:
            print(err)

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
            # self.conn.close()
            envio = True
            return envio
        except Exception as err:
            print('erro!: ', err)

    def close_connection(self):
        return self.conn.close()