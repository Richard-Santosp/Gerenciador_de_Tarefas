from login_window import Login
from cadastro_window import Cadastro
from main.dashboard import Painel
from database.conn_mysql import Database_connector
from PIL import Image
import customtkinter


if __name__ == "__main__":
    root_login = customtkinter.CTk()

    def on_login_success(id_usuario):
        root_login.withdraw()
        open_dashboard = customtkinter.CTkToplevel(root_login)
        app_dashboard = Painel(open_dashboard, id_usuario)
        app_dashboard.protocol("WM_DELETE_WINDOW", lambda:root_login.destroy())
        open_dashboard.mainloop()

    app = Login(root_login, on_login_success=on_login_success)
    root_login.mainloop()


    