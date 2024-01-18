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
            query = 'SELECT id_usuario FROM usuarios WHERE email = %s AND senha = %s'
            params = (email, senha)
            cursor.execute(query, params)
            resultado = cursor.fetchall()
            cursor.close()
            return resultado
        except mysql.connector.errors as err:
            print(f'Erro: {err}')

    def criar_cadastro(self):
        if not self.conn:
            if not self.conectar():
                return None
        try:
            cursor = self.conn.cursor()
            # Criação da tabela de usuário
            cursor.execute('''CREATE TABLE IN NOT EXIST set_order.usuarios (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        email VARCHAR(255) NOT NULL,
                        nome VARCHAR(255) NOT NULL,
                        senha VARCHAR(255) NOT NULL  
            )''')

            # Criação de tabela de agendamento
            cursor.execute('''CREATE TABLE IF NOT EXIST set_order.agendamentos (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        usuario_id INT,
                        data_inicio DATE NOT NULL,
                        data_limite DATE NOT NULL,
                        descricao VARCHAR(255) NOT NULL,
                        status VARCHAR(10) NOT NULL,
                        FOREIGN KEY (usuario_id) REFERENCES set_order.usuarios(id)
            )''')
            self.conn.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f'Erro ao criar tabelas: {e}')
            return False

    # Enviando os dados passados na aba de cadastro ao banco de dados
    def enviar_cadastro(self, email, nome, senha):
        envio = None
        if not self.conn:
            if not self.conectar():
                return None
        try:
            self.criar_cadastro()
            cursor = self.conn.cursor()
            operation = 'INSERT INTO set_order.usuarios (email, nome , senha) VALUES (%s, %s, %s)'
            params = (email, nome, senha)
            cursor.execute(operation, params)
            self.conn.commit()
            cursor.close()
            envio = True
            self.criar_cadastro(email, nome)
            return envio
        except Exception as err:
            print(f'Erro ao criar tabela: {err}')

    def agendar_tarefa(self, usuario_id, data_inicio, data_limite, descricao, status):
        cursor = self.conn.cursor()
        operation = 'INSERT INTO set_order.agendamentos (usuario_id, data_inicio, data_limite, descricao, status) VALUES (%s,%s,%s,%s,%s)'
        params = (usuario_id, data_inicio, data_limite, descricao, status)
        cursor.execute(operation, params)
        self.conn.commit()
        cursor.close()
        envio = True
        return envio
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