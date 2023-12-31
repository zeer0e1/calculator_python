from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QMessageBox)


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Cria o widget principal onde vai os outros widgets
        self.cw = QWidget()

        # Cria o layout da aplicação
        self.v_layout = QVBoxLayout()

        # Seta o layout para onde vai todos os widgets
        self.cw.setLayout(self.v_layout)

        # Setando o titulo da janela
        self.setWindowTitle('PyCalc')

        # Seta o layout para a janela principal
        self.setCentralWidget(self.cw)

    def adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addWidgetToVLayout(self, widget: QWidget):
        self.v_layout.addWidget(widget)
        # Corrigindo o tamanho da janela para caber todos os elementos
    
    def makeMsgBox(self):
        return QMessageBox(self)
