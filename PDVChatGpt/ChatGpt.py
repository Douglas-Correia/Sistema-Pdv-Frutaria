from customtkinter import CustomTk, CustomLabel, CustomButton, CustomEntry, CustomFrame, CustomTreeview

class App(CustomTk):
    def __init__(self):
        super().__init__()

        self.attributes('-fullscreen', True)

        self.title("Sistema Responsivo")
        self.geometry("800x600")

        self.columnconfigure(0, weight=0)  
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        self.menu_frame = CustomFrame(self, width=200, bg="blue")
        self.menu_frame.grid(row=0, column=0, sticky="nsew")

        self.menu_frame.columnconfigure(0, weight=1)
        self.menu_frame.rowconfigure(0, weight=0)

        self.btn_caixa = CustomButton(self.menu_frame, text="Caixa", width=30, padding=15, command=self.show_caixa)
        self.btn_caixa.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.btn_cadastrar_produto = CustomButton(self.menu_frame, text="Cadastrar produto", width=30, padding=15, command=self.show_cadastrar_produto)
        self.btn_cadastrar_produto.grid(row=2, column=0, padx=10, pady=10)

        self.btn_relatorio = CustomButton(self.menu_frame, text="Relatórios", width=30, padding=15, command=self.show_relatorios)
        self.btn_relatorio.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        self.btn_list_prod = CustomButton(self.menu_frame, text="Listar Produtos", width=30, padding=15, command=self.show_listar_produtos)
        self.btn_list_prod.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        self.button_sair = CustomButton(self.menu_frame, text="Sair", width=30, padding=15, command=self.close_window)
        self.button_sair.grid(row=5, column=0, padx=10, pady=10, sticky="w")

        self.content_frame = CustomFrame(self)
        self.content_frame.grid(row=0, column=1, sticky="nsew")

        self.content_frame.columnconfigure(0, weight=1)
        self.content_frame.rowconfigure(0, weight=0)
        self.content_frame.rowconfigure(1, weight=1)

        self.show_caixa()

    def show_caixa(self):
        self.clear_content_frame()

        label_title_caixa = CustomLabel(self.content_frame, text="Caixa Livre", font=("Ivy", 50), justify="center")
        label_title_caixa.grid(row=0, column=0, padx=10, pady=10, sticky="n")

        self.entry_pesquisar = CustomEntry(self.content_frame, width=59, font=("Ivy", 18))
        self.entry_pesquisar.grid(row=1, column=0, padx=10, pady=50, sticky="nw")
        self.entry_pesquisar.set_placeholder("Código do produto")

        self.label_total = CustomEntry(self.content_frame, width=25, font=("Ivy", 18))
        self.label_total.grid(row=1, column=1, padx=100, pady=50, sticky="nw")
        self.label_total.set_placeholder("R$ 0,00")

        tree = CustomTreeview(self.content_frame, height=35)
        tree["columns"] = ("Coluna1", "Coluna2", "Coluna3")

        tree.heading("#0", text="ID")
        tree.heading("Coluna1", text="Nome")
        tree.heading("Coluna2", text="Quantidade")
        tree.heading("Coluna3", text="Preço")

        data = [
            ("1", "Dado 1.1", "Dado 1.2", "Dado 1.3"),
            ("2", "Dado 2.1", "Dado 2.2", "Dado 2.3"),
            ("3", "Dado 3.1", "Dado 3.2", "Dado 3.3")
        ]

        for item in data:
            tree.insert("", "end", text=item[0], values=(item[1], item[2], item[3]))

        tree.grid(row=2, column=0, columnspan=2, padx=10, pady=(10, 30), sticky="nw")

    def show_cadastrar_produto(self):
        self.clear_content_frame()

    def show_relatorios(self):
        self.clear_content_frame()

        label = CustomLabel(self.content_frame, text="Conteúdo dos Relatórios")
        label.grid(row=0, column=0, padx=10, pady=10)

    def show_listar_produtos(self):
        self.clear_content_frame()

        label = CustomLabel(self.content_frame, text="Conteúdo de Listar Produtos")
        label.grid(row=0, column=0, padx=10, pady=10)

    def clear_content_frame(self):
        for child in self.content_frame.winfo_children():
            child.destroy()

    def close_window(self):
        self.destroy()

if __name__ == "__main__":
    window = App()
    window.mainloop()
