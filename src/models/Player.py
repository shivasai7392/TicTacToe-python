from src.models.Cell import Cell


class Player:
    def __init__(self, name, symbol, playerType):
        self._name = name
        self._symbol = symbol
        self._playerType = playerType

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, value):
        self._symbol = value

    @property
    def playerType(self):
        return self._playerType

    @playerType.setter
    def playerType(self, value):
        self._playerType = value

    def makeMove(self, board):
        print("Enter the row value.")
        row = int(input())
        print("Enter the col value.")
        col = int(input())

        return Cell(row, col)
