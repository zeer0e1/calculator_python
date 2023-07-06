import sys
from main_window import MainWindow

from PySide6.QtWidgets import (QApplication, QLabel)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Cria a janela principal
    window = MainWindow()

    labe1 = QLabel('O meu texto')
    labe1.setStyleSheet('font-size: 60px')
    window.v_layout.addWidget(labe1)

    # Corrigindo o tamanho da janela para caber todos os elementos
    window.adjustFixedSize()

    # Exibe a janela principal
    window.show()

    # Executa a aplicação
    app.exec()
