class Cell:
    def __init__(self):
        self._row = 0
        self._col = 0
        self._cellStatus = None
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
