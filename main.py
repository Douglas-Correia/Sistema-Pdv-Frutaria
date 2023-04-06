import customtkinter as ctk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3 

janela = ctk.CTk()
janela_pdv = ctk.CTk()
janela_Cadastrar_Produto = ctk.CTk()

# SESSÃO DE CRIAÇÃO DA TELA DE CAIXA    SESSÃO DE CRIAÇÃO DA TELA DE CAIXA  SESSÃO DE CRIAÇÃO DA TELA DE CAIXA

class Tela_Pdv:
    def Chamar_Funções_Pdv(self):
        self.Conectar_Banco()
        self.Frames_pdv()
        self.Treeview()
        self.Label_entrys()
        self.Button_Incluir_Finalizar()
        self.Button_Menu()
        self.Configurando_tela()

    def Conectar_Banco(self):
        self.conn = sqlite3.connect("SistemaPDV.db")

        self.cursor = self.conn.cursor()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS UsersName (
            Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            userName TEXT NOT NULL,
            userPassword TEXT NOT NULL)
        """)
        print("Conectado")


    def Frames_pdv(self):
        self.frame_finalizar_venda = ctk.CTkFrame(master=janela_pdv, width=1530, height=70, corner_radius=0, fg_color="white")
        self.frame_finalizar_venda.place(x=0, y=5)

        self.frame_menu = ctk.CTkFrame(master=janela_pdv, width=180, height=710, corner_radius=0, fg_color="#485d71")
        self.frame_menu.place(x=0, y=80)

        self.frame_main = ctk.CTkFrame(master=janela_pdv, width=1340, height=710, corner_radius=0, fg_color="#ebf0f4")
        self.frame_main.place(x=180, y=80)

        self.frame_entry_pdv = ctk.CTkFrame(master=self.frame_main, width=650, height=518, fg_color="white", corner_radius=0)
        self.frame_entry_pdv.place(x=670, y=100)

        self.frame_total = ctk.CTkFrame(master=janela_pdv, width=1310, height=60, corner_radius=0, fg_color="white")
        self.frame_total.place(x=190, y=720)

    def Treeview(self):
        treeview = ttk.Treeview(master=self.frame_main, height=31, columns=("Item", "Quantidade", "Nome", "Preço", "Total"), show="headings")
        treeview.heading("Item", text="Item")
        treeview.heading("Quantidade", text="Quantidade")
        treeview.heading("Nome", text="Nome")
        treeview.heading("Preço", text="Preço")
        treeview.heading("Total", text="Total")
        treeview.column("Item", width=130)
        treeview.column("Quantidade", width=150)
        treeview.column("Nome", width=270)
        treeview.column("Preço", width=130)
        treeview.column("Total", width=130)
        treeview.place(x=10, y=125)

       # treeview.insert(parent="" ,index=0, values=(1))

    def Label_entrys(self):
        # LABEL TITULO
        label_title = ctk.CTkLabel(self.frame_main, text="CAIXA LIVRE",
        font=ctk.CTkFont(family="Roboto", size=25), text_color="DarkBlue")
        label_title.place(x=590, y=35)

        # ENTRY PRODUTOS
        self.entry_codigo_produto = ctk.CTkEntry(master=self.frame_entry_pdv, width=600, height=50,
        placeholder_text="Nome do produto", placeholder_text_color="black",
        font=ctk.CTkFont(family="Roboto", size=14))
        self.entry_codigo_produto.place(x=15, y=320)

        self.entry_quantidade_produto = ctk.CTkEntry(master=self.frame_entry_pdv, width=600, height=50,
        placeholder_text="Quantidade", placeholder_text_color="black",
        font=ctk.CTkFont(family="Roboto", size=14))
        self.entry_quantidade_produto.place(x=15, y=380)

        self.label_total = ctk.CTkLabel(master=self.frame_total, text="Valor total a pagar: R$ 0,00", font=ctk.CTkFont(family="Roboto", size=20))
        self.label_total.place(x=540, y=15)
        self.label_total.setvar()

    def Total_Compra(self):
        self.total_db = "SELECT Valor FROM Produtos WHERE "

    def Button_Incluir_Finalizar(self):
        self.button_incluir = ctk.CTkButton(self.frame_entry_pdv, text="+ Incluir Produto",
        width=600, height=50, corner_radius=3, text_color="white", font=ctk.CTkFont(family="Roboto bold", size=18)).place(x=15, y=445)

        self.img_finalize = PhotoImage(file="Finalize-png.png")
        self.button_finalizar = ctk.CTkButton(master=self.frame_finalizar_venda, text="Finalizar venda", height=40, font=ctk.CTkFont(family="Roboto", size=18), text_color="white")
        self.button_finalizar.place(x=1350, y=20)

    def Button_Menu(self):
        self.btn_produto = ctk.CTkButton(master=self.frame_menu, text="Produto", width=179, height=50, fg_color="#485d71", font=ctk.CTkFont(family="Roboto bold", size=18), corner_radius=1, hover_color="#415567", text_color="white", command=self.Cadastrar_Produto).place(x=0, y=0)

    def Cadastrar_Produto_Db(self):
        self.ent_db_nome = self.ent_cad_nome.get()
        self.ent_db_quant = self.ent_cad_quant.get()
        self.ent_db_peso = self.ent_cad_peso.get()
        self.ent_db_data = self.ent_cad_data_entrada.get()
        self.ent_db_valor = self.ent_cad_valor.get()

        self.cursor.execute(f"""INSERT INTO Produtos (Nome, Quantidade, Peso, Data_Entrada, Valor) VALUES ('{self.ent_db_nome}', {self.ent_db_quant}, {self.ent_db_peso}, '{self.ent_db_data}', {self.ent_db_valor})""")
        self.conn.commit()
        messagebox.showinfo(title="Cadastro de produtos", message="Produtos cadastrados com sucesso!!")

        self.ent_cad_nome.delete(0, END)
        self.ent_cad_quant.delete(0, END)
        self.ent_cad_peso.delete(0, END)
        self.ent_cad_data_entrada.delete(0, END)
        self.ent_cad_valor.delete(0, END)

    def Cadastrar_Produto(self):
        self.janela_Cadastrar_Produto = ctk.CTkToplevel()

        self.lb_cad_nome = ctk.CTkLabel(master=self.janela_Cadastrar_Produto, text="Nome do Produto", font=ctk.CTkFont(family="Roboto", size=18)).place(x=25, y=20)
        self.ent_cad_nome = ctk.CTkEntry(master=self.janela_Cadastrar_Produto, width=300, height=30)
        self.ent_cad_nome.place(x=25, y=60)

        self.lb_cad_quant = ctk.CTkLabel(master=self.janela_Cadastrar_Produto, text="Quantidade", font=ctk.CTkFont(family="Roboto", size=18)).place(x=25, y=100)
        self.ent_cad_quant = ctk.CTkEntry(master=self.janela_Cadastrar_Produto, width=300, height=30)
        self.ent_cad_quant.place(x=25, y=140)

        self.lb_cad_peso = ctk.CTkLabel(master=self.janela_Cadastrar_Produto, text="Peso do Produto", font=ctk.CTkFont(family="Roboto", size=18)).place(x=25, y=180)
        self.ent_cad_peso = ctk.CTkEntry(master=self.janela_Cadastrar_Produto, width=300, height=30)
        self.ent_cad_peso.place(x=25, y=220)

        self.lb_data_entrada = ctk.CTkLabel(master=self.janela_Cadastrar_Produto, text="Data de Entrada", font=ctk.CTkFont(family="Roboto", size=18)).place(x=25, y=260)
        self.ent_cad_data_entrada = ctk.CTkEntry(master=self.janela_Cadastrar_Produto, width=300, height=30)
        self.ent_cad_data_entrada.place(x=25, y=300)

        self.lb_valor = ctk.CTkLabel(master=self.janela_Cadastrar_Produto, text="Valor do Produto:", font=ctk.CTkFont(family="Roboto", size=18)).place(x=25, y=340)
        self.ent_cad_valor = ctk.CTkEntry(master=self.janela_Cadastrar_Produto, width=300, height=30)
        self.ent_cad_valor.place(x=25, y=380)

        self.btn_cadastrar_produto = ctk.CTkButton(master=self.janela_Cadastrar_Produto, text="Cadastrar", width=300, height=45, font=ctk.CTkFont(family="Roboto", size=20), command=self.Cadastrar_Produto_Db).place(x=25, y=430)

        self.btn_sair = ctk.CTkButton(master=self.janela_Cadastrar_Produto, text="Sair", width=200, height=45, font=ctk.CTkFont(family="Roboto", size=20), command=self.Sair_Janela_Produto).place(x=350, y=430)
        
        self.janela_Cadastrar_Produto.title("Cadastro de Produtos")
        self.janela_Cadastrar_Produto.geometry("600x500+620+220")
        self.janela_Cadastrar_Produto.mainloop()

    def Sair_Janela_Produto(self):
        self.janela_Cadastrar_Produto.destroy()

    def Configurando_tela(self):
        ctk.set_appearance_mode("white")
       # janela_pdv.geometry("1300x725+180+20")
       # janela_pdv.state("zoomed")
        janela_pdv.geometry("{}x{}+0+0".format(janela_pdv.winfo_screenwidth(), janela_pdv.winfo_screenheight()))
        janela_pdv.title("Sistema de caixa")
        janela_pdv.mainloop()


# SESSÃO DE CRIAÇÃO DA TELA DE LOGIN  SESSÃO DE CRIAÇÃO DA TELA DE LOGIN  SESSÃO DE CRIAÇÃO DA TELA DE LOGIN

class Application_Login(Tela_Pdv):
    def __init__(self):
        self.janela = janela
        self.Conectar_Banco()
        self.Tema()
        self.Tela()
        self.Tela_Login()
        self.Campo_Entrys()
        janela.mainloop()
        
    def Conectar_Banco(self):
        self.conn = sqlite3.connect("SistemaPDV.db")

        self.cursor = self.conn.cursor()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS UsersName (
            Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            userName TEXT NOT NULL,
            userPassword TEXT NOT NULL)
        """)
        print("Conectado")

    # DEFININDO O TEMA
    def Tema(self):
        janela._set_appearance_mode("dark")

    # CONFIGURANDO A JANELA
    def Tela(self):
        self.janela.geometry("700x400+500+200")
        self.janela.title("Area de login")
        self.janela.iconbitmap("icon.ico")
        self.janela.resizable(False, False)

    # CAMPO DE LOGIN
    def Tela_Login(self):
        self.img = PhotoImage(file="frutaria-altura.png") 
        self.label_img = ctk.CTkLabel(master=self.janela, image=self.img)
        self.label_img.place(x=5, y=50)

        # FRAME DA JANELA DE LOGIN
        self.frame_login = ctk.CTkFrame(master=self.janela, width=360, height=400, fg_color="#252525", corner_radius=0).pack(side=RIGHT)

        # CAMPO DE LABELS
        self.label_ = ctk.CTkLabel(master=self.frame_login, text="SISTEMA DE PDV",
        font=ctk.CTkFont(family="Roboto", size=22), text_color="white", bg_color="#252525", corner_radius=None).place(x=50, y=5)
        self.label_ = ctk.CTkLabel(master=self.frame_login, text="EFETUAR LOGIN",
        font=ctk.CTkFont(family="Roboto", size=18), text_color="white" ,bg_color="#252525", corner_radius=None).place(x=470, y=5)

    def Campo_Entrys(self):
        # CAMPO DE ENTRY PARA RECEBER VARIÁVEIS DE LOGIN E SENHA
        self.entry_username = ctk.CTkEntry(master=self.frame_login,
        placeholder_text="Entre com Usuario", width=300, height=45,
        font=ctk.CTkFont(family="Roboto", size=14), text_color="black" ,bg_color="#252525", corner_radius=None)
        self.entry_username.place(x=380, y=60)
        self.lb_alert_obg = ctk.CTkLabel(master=self.frame_login,
        text="*O campo de usuario é de carater obrigatório", text_color="green",bg_color="#252525", corner_radius=None).place(x=380, y=109)

        self.entry_password = ctk.CTkEntry(master=self.frame_login,
        placeholder_text="Entre com a Senha", width=300, height=45,
        font=ctk.CTkFont(family="Roboto", size=14), show="*", text_color="black", bg_color="#252525", corner_radius=None)
        self.entry_password.place(x=380, y=150)
        self.lb_alert_obg = ctk.CTkLabel(master=self.frame_login,
        text="*O campo de senha é de carater obrigatório", text_color="green", bg_color="#252525", corner_radius=None).place(x=380, y=200)

        # CAMPO DE CHECKBOX
        self.check_box = ctk.CTkCheckBox(master=self.frame_login, text="Lembrar senha", hover_color="blue", text_color="white" ,bg_color="#252525", corner_radius=None).place(x=380, y=240)

        # CAMPO DE BOTÕES
        self.button = ctk.CTkButton(master=self.frame_login, text="Entrar", command=self.Verificar_Login
        ,width=300, height=45, hover_color="blue", font=ctk.CTkFont(family="Roboto", size=20), text_color="white" ,bg_color="#252525", corner_radius=None).place(x=380, y=280)
    
    def Receber_Variaveis_Login(self):
        self.username = str(self.entry_username.get())
        self.userpassword = str(self.entry_password.get())

    def Verificar_Login(self):
        self.Conectar_Banco()
        self.Receber_Variaveis_Login()
        veri_login = "SELECT * FROM UsersName WHERE userName like '"+self.username+"'AND userPassword like '"+self.userpassword+"'"
        self.cursor.execute(veri_login)
        validado = self.cursor.fetchall()
        if len(validado) > 0:
            Tela_Pdv(self.Chamar_Funções_Pdv())
            self.frame_login.pack_forget()
        else:
            messagebox.showerror(title="Erro de Login", message="Verifique usuario e senha!!")
        
        if self.entry_username and self.entry_password == "":
            messagebox.showinfo(title="Erro", message="Preencha todos os campos!!")
            return self.Verificar_Login()

        
Application_Login()