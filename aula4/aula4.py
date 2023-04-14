import sys

from PySide6.QtWidgets import QApplication, QPushButton, \
    QWidget, QGridLayout, QMainWindow


def slot_example(status_bar):
    status_bar.showMessage('O slot foi executado')


def outro_slot(checked):
    print('Está marcado?', checked)


def terceiro_slot(action):
    def inner():
        outro_slot(action.isChecked())
    return inner


app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)

botao = QPushButton('Texto do Botão')
botao.setStyleSheet('font-size: 80px;')
botao.show()

botao2 = QPushButton('Botão 2')
botao2.setStyleSheet('font-size: 40px;')
botao2.show()

botao3 = QPushButton('Botão 3')
botao3.setStyleSheet('font-size: 40px;')
botao3.show()

layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 3, 1, 1, 2)

# statusBar
status_bar = window.statusBar()
status_bar.showMessage('Mostra Mensagem na barra')

# menuBar
menu = window.menuBar()
primeiro_menu = menu.addMenu('Primeiro Menu')
primeira_acao = primeiro_menu.addAction('Primeira Acao')
primeira_acao.triggered.connect(lambda: slot_example(status_bar))

segunda_action = primeiro_menu.addAction('Segunda acao')
segunda_action.setCheckable(True)
segunda_action.toggled.connect(outro_slot)
segunda_action.hovered.connect(terceiro_slot(segunda_action))

botao.clicked.connect(terceiro_slot(segunda_action))

window.show()  # Central Widget entre na tela
app.exec()  # O loop da aplicação
