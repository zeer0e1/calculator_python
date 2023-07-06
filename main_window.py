from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout,)


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Cria o widget principal onde vai os outros widgets
        self.cw = QWidget()

        # Cria o layout da aplicação
        self.v_layout = QVBoxLayout()

        # Seta o layout para onde vai todos os widgets
        self.cw.setLayout(self.v_layout)

        # Seta o layout para a janela principal
        self.setCentralWidget(self.cw)

        # Setando o titulo da janela
        self.setWindowTitle('CALCULADORA')

        # Configura para deixar um tamanho fixo da janela
        
    def adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

