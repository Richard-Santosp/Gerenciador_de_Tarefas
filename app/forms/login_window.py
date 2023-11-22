import customtkinter
from CTkMessagebox import CTkMessagebox

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Tarefas")
        self.root.geometry("450x250")

        email_label = customtkinter.CTkLabel(self.root, text='Label', font=("Courier New", 22))
        email_label.place(x=75, y=100)
        self.email_entry = customtkinter.CTkEntry(self.root, width=210)
        self.email_entry.place(x=150, y=100)

        senha_label = customtkinter.CTkLabel(self.root, text='Senha', font=("Courier New", 22))
        senha_label.place(x=75, y=135)
        self.senha_entry = customtkinter.CTkEntry(self.root, width=210, show="*")
        self.senha_entry.place(x=150, y=135)

        botao_cadastrar = customtkinter.CTkButton(root, text="Cadastrar", font=("Helvetica", 22, "bold"), command=self.cadastrar)
        botao_cadastrar.place(x=75, y=170)

        botao_login = customtkinter.CTkButton(root, text="Login", font=("Helvetica", 22, "bold"), command=self.realizar_login)
        botao_login.place(x=220, y=170)

    def cadastrar(self):
        try:
            self.root.destroy()
            from cadastro_window import Cadastro
            self.root = customtkinter.CTk()
            app_cadastro = Cadastro(self.root)
            self.root.mainloop()
        except Exception as e:
            print(f'Erro de importação: {e}')

    def realizar_login(self):
        try:
            from db.database import Database_connector
            email = self.email_entry.get()
            senha = self.senha_entry.get()
            if senha:
                print("foi")
            else:
                print("não foi")
            conn = Database_connector("Localhost", "Fmztgmgresr1@", "root", "set_order")
            conn.conectar()
            resultado = conn.pesquisar_usuario(email, senha)
            if not email or not senha:
                return CTkMessagebox(title="Atenção", message="Preencha os campos", icon="warning")
            elif not resultado:
                CTkMessagebox(title="Atenção", message="Email ou senha invalidos", icon="warning")
            print("Bem sucedido")
        except ImportError as e:
            print(f'Erro de importação: {e}')

if __name__ == "__main__":
    root_login = customtkinter.CTk()
    app = Login(root_login)
    root_login.mainloop()