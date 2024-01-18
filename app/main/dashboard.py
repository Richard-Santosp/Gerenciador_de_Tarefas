import customtkinter
from PIL import Image
from api_cotacoes import cambio_acoes

modificador = 0

class Painel:
    def __init__(self, root, id_usuario):
        self.root = root
        self.root.title('Dashboard - Set Order')
        self.root.configure(fg_color='#c3d7d4')
        width = 1000
        height = 620
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        self.root.geometry('%dx%d+%d+%d' % (width, height, x+50, y-20))
        self.root.resizable(False, False)
        

        # Painel lateral ------------------------------------------------------------
        self.painel_lateral = customtkinter.CTkFrame(self.root, width=190, height=590,border_width=1, border_color='#95afc2', fg_color='#58acb2', corner_radius=50)
        self.painel_lateral.place(x=5, y=5)

        # Logo
        self.logo_imagem = customtkinter.CTkImage(light_image=Image.open('images/logo.jpg'), size=(190, 140))
        self.logo = customtkinter.CTkLabel(self.root, image=self.logo_imagem, text="")
        self.logo.place(x=5, y=5)

        # Calendario
        self.icone_calendario = customtkinter.CTkImage(light_image=Image.open('images/calendario.jpg'), size=(165,165))
        self.calendario = customtkinter.CTkButton(self.root, image=self.icone_calendario, text="", fg_color='#58acb2', hover_color='#417b7f', corner_radius=0, command= lambda: self.abrir_calendario())
        self.calendario.place(x=15, y=150)

        ######### dia e hora
        from datetime import date
        data = date.today()
        self.dia = customtkinter.CTkLabel(self.painel_lateral,text=f'{data.day}/{data.month}/{data.year} -', font=("Comic Sans MS", 12), text_color='#ffffff')
        self.dia.place(x=20, y=430)

        self.horario_atual = customtkinter.CTkLabel(self.painel_lateral,text='', font=("Comic Sans MS", 12), text_color='#ffffff')
        self.horario_atual.place(x=97, y=430)
        self.horario()

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
        self.botao_logoff = customtkinter.CTkButton(self.painel_lateral, text='Logoff', width=170, height=45, font=("Courier New", 22, 'bold'), fg_color='#e15050', hover_color='#f23838', border_spacing=5, corner_radius=25, border_width=1, border_color='#000000', command= lambda: self.root.destroy())
        self.botao_logoff.place(x=10, y=525)

        # cotações------------------------------------------------------------------------------------
        self.cotacoes = customtkinter.CTkFrame(self.root, fg_color='#000000', width=1000, height=25, corner_radius=0)
        self.cotacoes.place(x=0, y=0)

        self.cotacoes_titulo = customtkinter.CTkLabel(self.cotacoes, font=("Courier New", 14, 'bold'), text='Cotações atualizadas',text_color="#ffffff", fg_color='#A10000', width=200, height=24, corner_radius=15)
        self.cotacoes_titulo.place(x=-10, y=0)
        
        # Dolar
        self.dolar = customtkinter.CTkLabel(self.cotacoes, text='', width=10, height=10, font=("Courier New", 14, 'bold'))
        self.dolar.place(x=230, y=5)
        self.dolar_variacao = customtkinter.CTkLabel(self.cotacoes, text='-----', width=10, height=10, font=("Courier New", 14, 'bold'))
        self.dolar_variacao.place(x=340, y=5)
        self.cotacoes_moedas(self.dolar,self.dolar_variacao, 'dolar')

        # Euro
        self.euro = customtkinter.CTkLabel(self.cotacoes, text='', width=10, height=10, font=("Courier New", 14, 'bold'))
        self.euro.place(x=440, y=5)
        self.euro_variacao = customtkinter.CTkLabel(self.cotacoes, text='-----', width=10, height=10, font=("Courier New", 14, 'bold'))
        self.euro_variacao.place(x=540, y=5)
        self.cotacoes_moedas(self.euro,self.euro_variacao, 'euro')

        self.ibovespa = customtkinter.CTkLabel(self.cotacoes, text='', width=10, height=10, font=("Courier New", 14, 'bold'))
        self.ibovespa.place(x=640, y=5)
        self.cotacoes_acoes(self.ibovespa, 'ibovespa')

        self.nasdaq = customtkinter.CTkLabel(self.cotacoes, text='', width=10, height=10, font=("Courier New", 14, 'bold'))
        self.nasdaq.place(x=820, y=5)
        self.cotacoes_acoes(self.nasdaq, 'nasdaq')

        # cabeçalho--------------------------------------------------------------------------------------
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

        # body-----------------------------------------------------------------------------------------
        self.body = customtkinter.CTkFrame(self.root, fg_color='#5aabb3', width=795, height=450)
        self.body.place(x=200, y=145)
        
        ######### Em andamendo
        self.celula_1 = customtkinter.CTkLabel(self.body, width=192, height=105, fg_color='#ffffff', corner_radius=15)
        self.celula_1.place(x=5 , y=10)

        self.celula_2 = customtkinter.CTkLabel(self.body, width=192, height=105, fg_color='#ffffff', corner_radius=15)
        self.celula_2.place(x=5 , y=120)

        self.celula_3 = customtkinter.CTkLabel(self.body, width=192, height=105, fg_color='#ffffff', corner_radius=15)
        self.celula_3.place(x=5 , y=230)
        
        self.celula_4 = customtkinter.CTkLabel(self.body, width=192, height=105, fg_color='#ffffff', corner_radius=15)
        self.celula_4.place(x=5 , y=340)

        ######### agendada
        self.celula_5 = customtkinter.CTkLabel(self.body, width=192, height=105, fg_color='#ffffff', corner_radius=15)
        self.celula_5.place(x=202 , y=10)

        self.celula_6 = customtkinter.CTkLabel(self.body, width=192, height=105, fg_color='#ffffff', corner_radius=15)
        self.celula_6.place(x=202 , y=120)

        self.celula_7 = customtkinter.CTkLabel(self.body, width=192, height=105, fg_color='#ffffff', corner_radius=15)
        self.celula_7.place(x=202 , y=230)
        
        self.celula_8 = customtkinter.CTkLabel(self.body, width=192, height=105, fg_color='#ffffff', corner_radius=15)
        self.celula_8.place(x=202 , y=340)

        ######### Canceladas
        self.celula_9 = customtkinter.CTkLabel(self.body, width=192, height=105, fg_color='#ffffff', corner_radius=15)
        self.celula_9.place(x=399 , y=10)

        self.celula_10 = customtkinter.CTkLabel(self.body, width=192, height=105, fg_color='#ffffff', corner_radius=15)
        self.celula_10.place(x=399 , y=120)

        self.celula_11 = customtkinter.CTkLabel(self.body, width=192, height=105, fg_color='#ffffff', corner_radius=15)
        self.celula_11.place(x=399 , y=230)
        
        self.celula_12= customtkinter.CTkLabel(self.body, width=192, height=105, fg_color='#ffffff', corner_radius=15)
        self.celula_12.place(x=399 , y=340)

        ######### Concluidas
        self.celula_13 = customtkinter.CTkLabel(self.body, width=192, height=105, fg_color='#ffffff', corner_radius=15)
        self.celula_13.place(x=595 , y=10)

        self.celula_14 = customtkinter.CTkLabel(self.body, width=192, height=105, fg_color='#ffffff', corner_radius=15)
        self.celula_14.place(x=595 , y=120)

        self.celula_15 = customtkinter.CTkLabel(self.body, width=192, height=105, fg_color='#ffffff', corner_radius=15)
        self.celula_15.place(x=595 , y=230)
        
        self.celula_16 = customtkinter.CTkLabel(self.body, width=192, height=105, fg_color='#ffffff', corner_radius=15, )
        self.celula_16.place(x=595 , y=340)

        self.id_usuario = customtkinter.CTkLabel(self.root, text=f'ID do usuário: {id_usuario[0][0]}', text_color="#000000")
        self.id_usuario.place(x=865, y=595)

    def cotacoes_moedas(self, var_moeda, var_variacao, moeda):
        valor = cambio_acoes()
        if valor[f'{moeda}_variacao'] > 0:
            var_moeda.configure(text=f"{moeda} = {valor[f'{moeda}_atual']:.2f}", text_color='#12ff00')
            var_variacao.configure(text=f"%{valor[f'{moeda}_variacao']}▲", text_color='#12ff00')
        else:
            var_moeda.configure(text=f"{moeda} = {valor[f'{moeda}_atual']:.2f}", text_color='#ff0000')
            var_variacao.configure(text=f"%{valor[f'{moeda}_variacao']}▼", text_color='#ff0000')
        self.root.after(30000, lambda: self.cotacoes_moedas(var_moeda,var_variacao , moeda))

    def cotacoes_acoes(self, var_acao, acao):
        valor = cambio_acoes()
        if valor[acao] > 0:
            var_acao.configure(text=f"{acao} = %{valor[acao]}▲", text_color='#12ff00')
        else:
            var_acao.configure(text=f"{acao} = %{valor[acao]}▼", text_color='#ff0000')
        self.root.after(30000, lambda: self.cotacoes_acoes(var_acao, acao))

    def horario(self):
        import time
        tempo = time.strftime("%I:%M:%S %p")
        self.horario_atual.configure(text=tempo)
        self.root.after(1000, self.horario)

    def abrir_calendario(self):
        self.body.place_forget()
        
        self.frame_calendario = customtkinter.CTkFrame(self.root, width=795, height=470, fg_color='#ffffff')
        self.frame_calendario.place(x=200, y=145)
        from datetime import date
        dias_dos_meses = [0,31,28,31,30,31,30,31,31,30,31,30,31]
        data_atual = date.today()
        mes_atual = data_atual.month+modificador
        dias_do_mes_atual = dias_dos_meses[mes_atual]
        x = 15
        y = 10
        for dia in range(dias_do_mes_atual):
            customtkinter.CTkButton(self.frame_calendario,text=dia+1, text_color='#000000', font=('Comic Sans MS', 22, 'bold'), width=120, height=70, border_width=4, border_color="#000000",hover_color='#498e93', corner_radius=15, fg_color='#ffffff', command=lambda dia=dia : self.agendar_dia(dia+1)).place(x=x, y=y)
            if x < 630:
                x += 128
            else:
                x = 15
                y += 77

        meses = ['janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
        self.mes_atual = customtkinter.CTkLabel(self.frame_calendario, text=meses[(data_atual.month - 1) + modificador], width=300, height=70, font=('Comic Sans MS', 22, 'bold'), fg_color='#58acb2', corner_radius=15, anchor='center')
        self.mes_atual.place(x=200, y=395)

        self.voltar_dashboard = customtkinter.CTkButton(self.frame_calendario, text='Voltar', font=('Comic Sans MS', 18, 'bold'), width=200, height=70, fg_color='#58acb2', hover_color='#498e93', corner_radius=15, command=lambda:self.voltar_para_dashboard(self.frame_calendario,self.frame_titulo_calendario, self.body, self.cabecalho))
        self.voltar_dashboard.place(x=580, y=395)
        self.titulo_calendario()

    def titulo_calendario(self):
        self.cabecalho.place_forget()
        self.frame_titulo_calendario = customtkinter.CTkFrame(self.root, width=795, height=118, fg_color='#58acb2', )
        self.frame_titulo_calendario.place(x=200, y=25)
    
        self.mes_passado = customtkinter.CTkButton(self.frame_titulo_calendario, text='⇦', text_color='#000000',font=('Comic Sans MS', 50, 'bold'), fg_color='#58acb2', hover_color='#58acb2',command= lambda: self.mudar_mes('-'))
        self.mes_passado.place(x=10, y=30)

        self.calendario_title = customtkinter.CTkLabel(self.frame_titulo_calendario, text='Calendario', font=('Comic Sans MS', 70, 'bold'),anchor='center')
        self.calendario_title.place(x=210, y=15)

        self.mes_futuro = customtkinter.CTkButton(self.frame_titulo_calendario, text='⇨', text_color='#000000',font=('Comic Sans MS', 50, 'bold'), fg_color='#58acb2', hover_color='#58acb2', command= lambda: self.mudar_mes('+') )
        self.mes_futuro.place(x=620, y=30)
    
    def mudar_mes(self, operacao):
        global modificador
        if operacao == '-':
            modificador -= 1
            self.abrir_calendario()
        else:
            modificador += 1
            self.abrir_calendario()


    def agendar_dia(self, agendamento):
        self.frame_calendario.place_forget()
        self.frame_agendamento = customtkinter.CTkFrame(self.root, width=795, height=470, fg_color='#ffffff')
        self.frame_agendamento.place(x=200, y=145)

        self.titulo_tarefa = customtkinter.CTkEntry(self.frame_agendamento, width=780, height=30, font=('Comic Sans MS', 30, 'bold'), corner_radius=15, fg_color='#505256')
        self.titulo_tarefa.place(x=5, y=5)

        self.tarefa = customtkinter.CTkTextbox(self.frame_agendamento, width=780, height=300, font=('Comic Sans MS', 15, 'bold'), corner_radius=15, fg_color='#ffffff', border_color='#000000', border_width=2, text_color='#000000')
        self.tarefa.place(x=5, y=55)

        self.dia_inicio = customtkinter.CTkEntry(self.frame_agendamento, width=780, height=30, font=('Comic Sans MS', 30, 'bold'), corner_radius=15, fg_color='#505256')
        self.dia_inicio.place(x=5, y=5)

    

    def add_tarefa(self, status):
        return status
    
    def voltar_para_dashboard(self, frame_calendario,frame_titulo_calendario, frame_dashboard, frame_cabecalho):
        frame_calendario.place_forget()
        frame_titulo_calendario.place_forget()
        frame_dashboard.place(x=200, y=140)
        frame_cabecalho.place(x=200, y=25)
    
    def logoff_dashboard(self, dashboard):
        dashboard.destroy()

        


if __name__ == '__main__':
    root = customtkinter.CTk()
    app = Painel(root, '#000')
    root.mainloop()

