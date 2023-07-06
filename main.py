import sys
from main_window import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QLabel)
from variabels import WINDOW_ICON_PATH


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Cria a janela principal
    window = MainWindow()

    labe1 = QLabel('O meu texto')
    labe1.setStyleSheet('font-size: 60px')

    # Add o widget de label criado para a layot da janela
    window.addWidgetToVLayout(labe1)

    # Exibe a janela principal
    window.show()

    # Setando o icone da aplicação
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    
    # Executa a aplicação
    app.exec()
