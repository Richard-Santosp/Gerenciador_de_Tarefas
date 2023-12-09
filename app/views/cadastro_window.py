import customtkinter
from CTkMessagebox import CTkMessagebox

class Cadastro:
    def __init__(self, root, toplevel):
        self.root = root
        self.root.title("Área de cadastro")
        width = 450
        height = 270
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        self.root.geometry('%dx%d+%d+%d' % (width, height, x, y))
        self.root.resizable(False, False)
        self.toplevel = toplevel

        # Campo de Email
        email_label = customtkinter.CTkLabel(self.root, text="Email", font=("Courier New", 22))
        email_label.place(x=75, y=89)
        self.email_entry = customtkinter.CTkEntry(self.root, width=210)
        self.email_entry.place(x=150, y=89)

        # Campo de nome do usuário
        nome_label = customtkinter.CTkLabel(self.root, text="Nome", font=("Courier New", 22))
        nome_label.place(x=75, y=141)
        self.nome_entry = customtkinter.CTkEntry(self.root, width=210)
        self.nome_entry.place(x=150, y=141)

        # Campo de senha
        senha_label = customtkinter.CTkLabel(self.root, text="Senha", font=("Courier New", 22))
        senha_label.place(x=75, y=193)
        self.senha_entry = customtkinter.CTkEntry(self.root, width=210, show="*")
        self.senha_entry.place(x=150, y=193)

        # Botão para destrui a janela de cadastro e voltar ao login
        botao_voltar = customtkinter.CTkButton(self.root, text="Voltar", font=("Courier New", 20, "bold"), command=self.voltar)
        botao_voltar.place(x=75, y=235)

        # Botão para enviar os dados prenchedos ao banco de dados
        botao_cadastrar = customtkinter.CTkButton(self.root, text="Cadastrar", font=("Courier New", 20, "bold"), command=self.realizar_cadastro)
        botao_cadastrar.place(x=220, y=235)
        
    # Função que destroy a janela cadastro e retorna a janela login
    def voltar(self):
        self.root.destroy()
        self.toplevel.deiconify()

    # Função de envio dos dados ao banco de dados
    def realizar_cadastro(self):
        try:
            from database.conn_mysql import Database_connector
            # Resgatando os valores dos formularios
            email = self.email_entry.get()
            nome = self.nome_entry.get()
            senha = self.senha_entry.get()
            # Caso algum campo não seja preenchido
            if not email or not nome or not senha:
                return CTkMessagebox(title="Atenção", message="Preencha os campos corretamente", icon="warning")
            # Realizando a conexão ao banco de dados
            conn = Database_connector("host", "password", "user", "database")
            conn.conectar()
            # verifica se o usuario ja existe
            if conn.verificacao_de_usuario(email):
                return CTkMessagebox(title="Atenção", message="Usuários já existe!", icon="warning")
            # Envia os dados ao banco de dados
            enviar_dados = conn.enviar_cadastro(email, nome, senha)
            conn.close_connection()
            # Se o envio foi bem sucedido, chama a função voltar para que o usuário retorne ao login e mostra uma mensagem de cadastro bem sucedido
            if enviar_dados:
                CTkMessagebox(title="Cadastro bem sucedido", message="O seu cadastro foi realizado com sucesso", icon="check", option_1="Ok")
                return self.voltar()
        except ImportError as e:
            print(f'Erro:{e}')