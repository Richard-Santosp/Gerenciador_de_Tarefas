import customtkinter
from PIL import Image

class Painel:
    def __init__(self, root):
        self.root = root
        self.root.title('Dashboard - Set Order')
        self.root.configure(fg_color='#c3d7d4')
        width = 1000
        height = 600
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        self.root.geometry('%dx%d+%d+%d' % (width, height, x+50, y-20))
        self.root.resizable(False, False)

        # Painel lateral
        self.painel_lateral = customtkinter.CTkFrame(self.root, width=190, height=590,border_width=1, border_color='#95afc2', fg_color='#58acb2', corner_radius=50)
        self.painel_lateral.place(x=5, y=5)

        # Logo
        logo_imagem = customtkinter.CTkImage(light_image=Image.open("images/logo.jpg"), size=(190, 140))
        logo = customtkinter.CTkLabel(self.root, image=logo_imagem, text="")
        logo.place(x=5, y=5)

        # Calendario
        icone_calendario = customtkinter.CTkImage(light_image=Image.open("images/calendario.jpg"), size=(165,165))
        calendario = customtkinter.CTkButton(self.root, image=icone_calendario, text="", fg_color='#58acb2', hover_color='#417b7f', corner_radius=0, command= lambda: print('Interface do calendario'))
        calendario.place(x=15, y=150)

        # botão de adicionar tarefa
        self.botao_add = customtkinter.CTkButton(self.painel_lateral, text='Adicionar', font=("Courier New", 12, 'bold'), text_color='#000000', fg_color='#32a8dd', hover_color='#2c8db9', corner_radius=5, width=85, border_width=1,border_color='#000000')
        self.botao_add.place(x=5, y=455)

        # botão de agendar tarefa
        self.botao_agendar = customtkinter.CTkButton(self.painel_lateral, text='Agendar', font=("Courier New", 12, 'bold'), text_color='#000000', fg_color='#fdff63', hover_color='#dad757', corner_radius=5, width=85, border_width=1,border_color='#000000')
        self.botao_agendar.place(x=95, y=455)

        # botão de concluir tarefa
        self.botao_concluir = customtkinter.CTkButton(self.painel_lateral, text='Concluir', font=("Courier New", 12, 'bold'), text_color='#000000', fg_color='#5eb14c', hover_color='#3ea64b', corner_radius=5, width=85, border_width=1,border_color='#000000')
        self.botao_concluir.place(x=5, y=490)

        # botão de cancelar tarefa
        self.botao_cancelar = customtkinter.CTkButton(self.painel_lateral, text='Cancelar', font=("Courier New", 12, 'bold'), text_color='#000000', fg_color='#f64126', hover_color='#f32f18', corner_radius=5, width=85, border_width=1,border_color='#000000')
        self.botao_cancelar.place(x=95, y=490)

        # Botão logoff
        self.botao_logoff = customtkinter.CTkButton(self.painel_lateral, text='Logoff', width=170, height=45, font=("Courier New", 22, 'bold'), fg_color='#e15050', hover_color='#f23838', border_spacing=5, corner_radius=25)
        self.botao_logoff.place(x=10, y=525)

        # cotações
        self.cotacoes = customtkinter.CTkFrame(self.root, fg_color='#819787', width=1000, height=25, corner_radius=0)
        self.cotacoes.place(x=0, y=0)

        self.cotacoes_titulo = customtkinter.CTkLabel(self.cotacoes, font=("Courier New", 14, 'bold'), text='Cotações atualizadas',text_color="#ffffff", fg_color='#A10000', width=200, height=24, corner_radius=15)
        self.cotacoes_titulo.place(x=-10, y=0)

        # cabeçalho
        self.cabecalho = customtkinter.CTkFrame(self.root, fg_color='#5aabb3', width=795, height=118)
        self.cabecalho.place(x=200, y=25)

        # Em andamento
        self.cab_em_andamento = customtkinter.CTkLabel(self.cabecalho, width=192, height=105, fg_color='#9CD5FF', corner_radius=35, text='Em\nAndamento',text_color="#000000", font=("Comic Sans MS", 22, 'bold'))
        self.cab_em_andamento.place(x=5 , y=10)

        # Agendada
        self.cab_agendada = customtkinter.CTkLabel(self.cabecalho, width=192, height=105, fg_color='#FFFEA5', corner_radius=35, text='Agendada', text_color="#000000", font=("Comic Sans MS", 22, 'bold'))
        self.cab_agendada.place(x=202 , y=10)

        # Cancelada
        self.cab_cancelada = customtkinter.CTkLabel(self.cabecalho, width=192, height=105, fg_color='#FF7575', corner_radius=35, text='Cancelada', text_color="#000000", font=("Comic Sans MS", 22, 'bold'))
        self.cab_cancelada.place(x=399 , y=10)

        # Concluida
        self.cab_concluida = customtkinter.CTkLabel(self.cabecalho, width=192, height=105, fg_color='#C2FFC1', corner_radius=35, text="Concluida", text_color="#000000", font=("Comic Sans MS", 22, 'bold'))
        self.cab_concluida.place(x=595 , y=10)

        # body
        self.body = customtkinter.CTkFrame(self.root, fg_color='#5aabb3', width=795, height=450)
        self.body.place(x=200, y=145)
        
        # Em andamendo
        self.celula_1 = customtkinter.CTkLabel(self.body, width=192, height=105, fg_color='#ffffff', corner_radius=15)
        self.celula_1.place(x=5 , y=10)

        self.celula_2 = customtkinter.CTkLabel(self.body, width=192, height=105, fg_color='#ffffff', corner_radius=15)
        self.celula_2.place(x=5 , y=120)

        self.celula_3 = customtkinter.CTkLabel(self.body, width=192, height=105, fg_color='#ffffff', corner_radius=15)
        self.celula_3.place(x=5 , y=230)
        
        self.celula_4 = customtkinter.CTkLabel(self.body, width=192, height=105, fg_color='#ffffff', corner_radius=15)
        self.celula_4.place(x=5 , y=340)

        # agendada
        self.celula_5 = customtkinter.CTkLabel(self.body, width=192, height=105, fg_color='#ffffff', corner_radius=15)
        self.celula_5.place(x=202 , y=10)

        self.celula_6 = customtkinter.CTkLabel(self.body, width=192, height=105, fg_color='#ffffff', corner_radius=15)
        self.celula_6.place(x=202 , y=120)

        self.celula_7 = customtkinter.CTkLabel(self.body, width=192, height=105, fg_color='#ffffff', corner_radius=15)
        self.celula_7.place(x=202 , y=230)
        
        self.celula_8 = customtkinter.CTkLabel(self.body, width=192, height=105, fg_color='#ffffff', corner_radius=15)
        self.celula_8.place(x=202 , y=340)

        # Canceladas
        self.celula_9 = customtkinter.CTkLabel(self.body, width=192, height=105, fg_color='#ffffff', corner_radius=15)
        self.celula_9.place(x=399 , y=10)

        self.celula_10 = customtkinter.CTkLabel(self.body, width=192, height=105, fg_color='#ffffff', corner_radius=15)
        self.celula_10.place(x=399 , y=120)

        self.celula_11 = customtkinter.CTkLabel(self.body, width=192, height=105, fg_color='#ffffff', corner_radius=15)
        self.celula_11.place(x=399 , y=230)
        
        self.celula_12= customtkinter.CTkLabel(self.body, width=192, height=105, fg_color='#ffffff', corner_radius=15)
        self.celula_12.place(x=399 , y=340)

        # Concluidas
        self.celula_13 = customtkinter.CTkLabel(self.body, width=192, height=105, fg_color='#ffffff', corner_radius=15)
        self.celula_13.place(x=595 , y=10)

        self.celula_14 = customtkinter.CTkLabel(self.body, width=192, height=105, fg_color='#ffffff', corner_radius=15)
        self.celula_14.place(x=595 , y=120)

        self.celula_15 = customtkinter.CTkLabel(self.body, width=192, height=105, fg_color='#ffffff', corner_radius=15)
        self.celula_15.place(x=595 , y=230)
        
        self.celula_16 = customtkinter.CTkLabel(self.body, width=192, height=105, fg_color='#ffffff', corner_radius=15, )
        self.celula_16.place(x=595 , y=340)

    def teste(self):
        num = 0
        while num < 3:
            print('teste', num)
            num += 1

if __name__ == '__main__':
    root = customtkinter.CTk()
    app = Painel(root)
    root.mainloop()