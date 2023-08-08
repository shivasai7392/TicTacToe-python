from src.models.CellStatus import CellStatus


class Cell:
    def __init__(self, row, col):
        self._row = row
        self._col = col
        self._cellStatus = CellStatus.EMPTY
        self._player = None

    @property
    def row(self):
        return self._row

    @row.setter
    def row(self, value):
        self._row = value

    @property
    def col(self):
        return self._col

    @col.setter
    def col(self, value):
        self._col = value

    @property
    def cellStatus(self):
        return self._cellStatus

    @cellStatus.setter
    def cellStatus(self, value):
        self._cellStatus = value

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, value):
        self._player = value

    def print(self):
        if self.cellStatus == CellStatus.EMPTY:
            print("-|", end="")
        else:
            print(self.player.symbol.shape+"|", end="")
