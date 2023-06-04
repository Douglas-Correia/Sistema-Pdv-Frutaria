import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTreeView, QTreeWidgetItem, QStandardItemModel, QStandardItem

class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sistema Responsivo")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.menu_widget = QWidget(self.central_widget)
        self.menu_layout = QVBoxLayout(self.menu_widget)

        self.btn_caixa = QPushButton("Caixa", self.menu_widget)
        self.btn_caixa.clicked.connect(self.show_caixa)
        self.menu_layout.addWidget(self.btn_caixa)

        self.btn_cadastrar_produto = QPushButton("Cadastrar produto", self.menu_widget)
        self.btn_cadastrar_produto.clicked.connect(self.show_cadastrar_produto)
        self.menu_layout.addWidget(self.btn_cadastrar_produto)

        self.btn_relatorio = QPushButton("Relatórios", self.menu_widget)
        self.btn_relatorio.clicked.connect(self.show_relatorios)
        self.menu_layout.addWidget(self.btn_relatorio)

        self.btn_list_prod = QPushButton("Listar Produtos", self.menu_widget)
        self.btn_list_prod.clicked.connect(self.show_listar_produtos)
        self.menu_layout.addWidget(self.btn_list_prod)

        self.button_sair = QPushButton("Sair", self.menu_widget)
        self.button_sair.clicked.connect(self.close_window)
        self.menu_layout.addWidget(self.button_sair)

        self.content_widget = QWidget(self.central_widget)
        self.content_layout = QVBoxLayout(self.content_widget)

        self.show_caixa()

        self.main_layout = QHBoxLayout(self.central_widget)
        self.main_layout.addWidget(self.menu_widget)
        self.main_layout.addWidget(self.content_widget)

    def show_caixa(self):
        self.clear_content_layout()

        label_title_caixa = QLabel("Caixa Livre", self.content_widget)
        label_title_caixa.setStyleSheet("font-size: 50px;")
        self.content_layout.addWidget(label_title_caixa)

        self.entry_pesquisar = QLineEdit(self.content_widget)
        self.entry_pesquisar.setPlaceholderText("Código do produto")
        self.content_layout.addWidget(self.entry_pesquisar)

        self.label_total = QLineEdit(self.content_widget)
        self.label_total.setPlaceholderText("R$ 0,00")
        self.content_layout.addWidget(self.label_total)

        model = QStandardItemModel()
        model.setColumnCount(4)
        model.setHeaderData(0, Qt.Horizontal, "ID")
        model.setHeaderData(1, Qt.Horizontal, "Nome")
        model.setHeaderData(2, Qt.Horizontal, "Quantidade")
        model.setHeaderData(3, Qt.Horizontal, "Preço")

        tree = QTreeView(self.content_widget)
        tree.setModel(model)

        data = [
            ("1", "Dado 1.1", "Dado 1.2", "Dado 1.3"),
            ("2", "Dado 2.1", "Dado 2.2", "Dado 2.3"),
            ("3", "Dado 3.1", "Dado 3.2", "Dado 3.3")
        ]

        for item in data:
            tree.addTopLevelItem(QTreeWidgetItem(item))

        self.content_layout.addWidget(tree)

    def show_cadastrar_produto(self):
        self.clear_content_layout()

    def show_relatorios(self):
        self.clear_content_layout()

        label = QLabel("Conteúdo dos Relatórios", self.content_widget)
        self.content_layout.addWidget(label)

    def show_listar_produtos(self):
        self.clear_content_layout()

        label = QLabel("Conteúdo de Listar Produtos", self.content_widget)
        self.content_layout.addWidget(label)

    def clear_content_layout(self):
        while self.content_layout.count() > 0:
            item = self.content_layout.itemAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
            self.content_layout.removeItem(item)

    def close_window(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())
