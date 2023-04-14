import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QPushButton, \
    QWidget, QGridLayout, QMainWindow


class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.central_widget = QWidget()

        self.setCentralWidget(self.central_widget)
        self.setWindowTitle('Minha Janela Bonita')

        # botão

        self.botao1 = self.make_button('Texto do botão')
        self.botao1.clicked.connect(self.segunda_acao_marcada)   # type:ignore

        self.botao2 = self.make_button('Botão 2')

        self.botao3 = QPushButton('Botão 3')
        self.botao3.setStyleSheet('font-size: 40px;')

        self.grid_layout = QGridLayout()
        self.central_widget.setLayout(self.grid_layout)

        self.grid_layout.addWidget(self.botao1, 1, 1, 1, 1)
        self.grid_layout.addWidget(self.botao2, 1, 2, 1, 1)
        self.grid_layout.addWidget(self.botao3, 3, 1, 1, 2)

        # statusBar
        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Mostra Mensagem na barra')

        # menuBar
        self.menu = self.menuBar()
        self.primeiro_menu = self.menu.addMenu('Primeiro Menu')
        self.primeira_acao = self.primeiro_menu.addAction('Primeira Acao')
        self.primeira_acao.triggered.connect(self.slot_example)

        self.segunda_action = self.primeiro_menu.addAction('Segunda acao')
        self.segunda_action.setCheckable(True)
        self.segunda_action.toggled.connect(self.segunda_acao_marcada)
        self.segunda_action.hovered.connect(
            self.segunda_acao_marcada)  # type:ignore

    @Slot()
    def slot_example(self):
        self.status_bar.showMessage('O meu slot foi executado')

    @Slot()
    def segunda_acao_marcada(self):
        print('Está marcado?', self.segunda_action.isChecked())

    def make_button(self, text):
        btn = QPushButton(text)
        btn.setStyleSheet('font-size: 80px;')
        return btn


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec()  # O loop da aplicação
