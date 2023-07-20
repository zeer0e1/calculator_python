from PySide6.QtWidgets import QPushButton, QGridLayout
from variabels import MEDIUM_FONT_SIZE
from utils import isEmpty, isNumOrDot, isValidNumber
from PySide6.QtCore import Slot
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from display import Display
    from info import Infor


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)


class ButtonsGrid(QGridLayout):
    def __init__(
            self, display: 'Display', info: 'Infor', *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._grid_mask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]
        self.display = display
        self.info = info
        self._equation = ''
        self._equationInitialValue = 'Sua conta'
        self._left = None
        self._right = None
        self._op = None

        self.equation = self._equationInitialValue
        self._makeGrid()

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def _makeGrid(self):
        for i, row in enumerate(self._grid_mask):
            for j, button_text in enumerate(row):
                button = Button(button_text)

                if not isNumOrDot(button_text) and not isEmpty(button_text):
                    button.setProperty('cssClass', 'specialButton')
                    self._configSpecialButton(button)

                self.addWidget(button, i, j)
                slot = self._makeSlot(
                    self._inserButtonTextToDisplay, button)
                self._connectButtonClicked(button, slot)

    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)

    def _configSpecialButton(self, button):
        text = button.text()

        if text == 'C':
            self._connectButtonClicked(button, self._clear)
        
        if text in '+-/*':   
            self._connectButtonClicked(
                button, 
                self._makeSlot(self._operatorClicked, button)
                
                )
        
        if text in '=':   
            self._connectButtonClicked(
               button, self._eq)

    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)
        return realSlot

    def _inserButtonTextToDisplay(self, button):
        button_text = button.text()
        new_display_value = self.display.text() + button_text

        if not isValidNumber(new_display_value):
            return

        self.display.insert(button_text)

    def _clear(self):
        self.display.clear()
        self._left = None
        self._right = None
        self._op = None
        self.equation = self._equationInitialValue
    
    def _operatorClicked(self, button):
        buttonText = button.text()  # +-/*
        displayText = self.display.text()  # Devera ser o numero _left
        self.display.clear()  # Limpa o display
        
        if not isValidNumber(displayText) and self._left is None:
            print('n tem nada para colocar no valor da esquerda')
            return

        if self._left is None:
            self._left = float(displayText)
        
        self._op = buttonText
        self.equation = f'{self._left} {self._op} ??'

    def _eq(self):
        displayText = self.display.text()

        if not isValidNumber(displayText):
            print('N tenho nada para a direita')
            return
        
        self._right = float(displayText)
        self.equation = f'{self._left} {self._op} {self._right}'

        try:
            result = eval(self.equation)
            print(result)
        except ZeroDivisionError:
            print('Zero divios error')
        
        self.display.clear()
        self.info.setText(f'{self.equation} = {result}')