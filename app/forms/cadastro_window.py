import customtkinter

class Cadastro:
    def __init__(self, root):
        self.root = root
        self.root.title("Área de cadastro")
        self.root.geometry("450x270")

        email_label = customtkinter.CTkLabel(self.root, text="Email", font=("Courier New", 22))
        email_label.place(x=75, y=89)
        self.email_entry = customtkinter.CTkEntry(self.root, width=210)
        self.email_entry.place(x=150, y=89)

        nome_label = customtkinter.CTkLabel(self.root, text="Nome", font=("Courier New", 22))
        nome_label.place(x=75, y=141)
        self.nome_entry = customtkinter.CTkEntry(self.root, width=210)
        self.nome_entry.place(x=150, y=141)

        senha_label = customtkinter.CTkLabel(self.root, text="Senha", font=("Courier New", 22))
        senha_label.place(x=75, y=193)
        self.senha_entry = customtkinter.CTkEntry(self.root, width=210, show="*")
        self.senha_entry.place(x=150, y=193)

        botao_voltar = customtkinter.CTkButton(self.root, text="Voltar", font=("Courier New", 20, "bold"), command=self.voltar)
        botao_voltar.place(x=75, y=235)

        botao_cadastrar = customtkinter.CTkButton(self.root, text="Cadastrar", font=("Courier New", 20, "bold"), command=self.realizar_cadastro)
        botao_cadastrar.place(x=220, y=235)
        
    def voltar(self):
        self.root.destroy()
        from login_window import Login
        login = customtkinter.CTk()
        app_login = Login(login)
        login.mainloop()

    def realizar_cadastro(self):
        try:
            from db.database import Database_connector
            email = self.email_entry.get()
            nome = self.nome_entry.get()
            senha = self.senha_entry.get()
            conn = Database_connector("host", "password", "user", "database")
            conn.conectar()
            enviar_dados = conn.enviar_cadastro(email, nome, senha)
        except Exception as e:
            print(e)