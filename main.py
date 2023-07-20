import sys
from main_window import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from display import Display
from variabels import WINDOW_ICON_PATH
from info import Infor
from styles import setupTheme
from buttons import ButtonsGrid
if __name__ == '__main__':

    app = QApplication(sys.argv)

    # Style da aplicação
    setupTheme()

    # Cria a janela principal
    window = MainWindow()

    # Info
    info_label = Infor('Sua conta')
    window.addWidgetToVLayout(info_label)

    # Display
    display = Display()
    window.addWidgetToVLayout(display)

    # GridButton
    buttonsGrid = ButtonsGrid(display, info_label)
    window.v_layout.addLayout(buttonsGrid)

    # Setando o icone da aplicação
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Executa a aplicação
    window.adjustFixedSize()

    # Exibe a janela principal
    window.show()

    app.exec()
