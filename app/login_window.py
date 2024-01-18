import customtkinter
from CTkMessagebox import CTkMessagebox
from main.dashboard import Painel
from main.api_cotacoes import cambio_acoes

class Login:
    def __init__(self, root, cadastramento=None, on_login_success=None):
        self.root = root
        self.root.title("Gerenciador de Tarefas")
        self.root.geometry("450x250")
        self.root.resizable(False, False)
        self.cadastramento = cadastramento
        self.on_login_success = on_login_success

        # Formulario email
        self.email_label = customtkinter.CTkLabel(self.root, text='Email', font=("Courier New", 22))
        self.email_label.place(x=75, y=100)
        self.email_entry = customtkinter.CTkEntry(self.root, width=210)
        self.email_entry.place(x=150, y=100)

        # Formulario senha
        self.senha_label = customtkinter.CTkLabel(self.root, text='Senha', font=("Courier New", 22))
        self.senha_label.place(x=75, y=135)
        self.senha_entry = customtkinter.CTkEntry(self.root, width=210, show="*")
        self.senha_entry.place(x=150, y=135)

        # Botão que gera a janela de cadastro
        self.botao_cadastrar = customtkinter.CTkButton(self.root, text="Cadastrar", font=("Helvetica", 22, "bold"), command=self.cadastrar)
        self.botao_cadastrar.place(x=75, y=170)

        # Botão que que faz a consulta ao banco de dados para realizar o login 
        self.botao_login = customtkinter.CTkButton(self.root, text="Login", font=("Helvetica", 22, "bold"), command=self.realizar_login)
        self.botao_login.place(x=220, y=170)

    # Função que gerar a janela de cadastro
    def cadastrar(self):
        try:
            # A janela do login é oculta durante o cadastro
            self.root.withdraw()
            from cadastro_window import Cadastro
            self.cadastramento = customtkinter.CTkToplevel(self.root)
            app_cadastro = Cadastro(self.cadastramento, self.root)
            # Funcionalidade para destruir a janela de login caso o cadastro seja fechado com o login oculto
            self.cadastramento.protocol("WM_DELETE_WINDOW", lambda:self.root.destroy())
            self.cadastramento.mainloop()
        except Exception as e:
            print(e)

    # Verificação dos dados no banco de dados
    def realizar_login(self):
        try:
            from database.conn_mysql import Database_connector
            # Resgatando os dados dos campos de login
            email = self.email_entry.get()
            senha = self.senha_entry.get()
            # Caso algum campo na seja preenchido
            if not email or not senha:
                return CTkMessagebox(title="Atenção", message="Preencha os campos", icon="warning")
            # Realizando a conexão com o banco de dados MySQL
            conn = Database_connector("host", "password", "user", "database")
            conn.conectar()
            # Consulta no banco da dados e resposta do resultado
            resultado = conn.pesquisar_usuario(email, senha)
            conn.close_connection()
            # Caso os dados não constem no banco de dados
            if not resultado:
                return CTkMessagebox(title="Atenção", message="Email ou senha invalidos", icon="warning")
            # Login bem sucedido
            if self.on_login_success:
                self.on_login_success(resultado)

            # Feche a janela de login
            self.root.destroy()
        except ImportError as e:
            print(f'Erro de importação: {e}')

if __name__ == "__main__":
    root_login = customtkinter.CTk()

    def on_login_success():
        # Crie uma instância do Painel (dashboard) aqui
        painel_root = customtkinter.CTk()
        painel = Painel(painel_root)
        painel_root.mainloop()

    app = Login(root_login, on_login_success=on_login_success)
    root_login.mainloop()