import sys

from PySide6.QtWidgets import QApplication, QPushButton, \
    QWidget, QVBoxLayout, QHBoxLayout, QGridLayout

app = QApplication(sys.argv)

botao = QPushButton('Texto do Botão')
botao.setStyleSheet('font-size: 80px;')
botao.show()

botao2 = QPushButton('Botão 2')
botao2.setStyleSheet('font-size: 40px;')
botao2.show()

botao3 = QPushButton('Botão 3')
botao3.setStyleSheet('font-size: 40px;')
botao3.show()

central_widget = QWidget()

layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao, 1, 1)
layout.addWidget(botao2, 2, 1)
layout.addWidget(botao3, 3, 1)


central_widget.show()  # Central Widget entre na tela
app.exec()  # O loop da aplicação
