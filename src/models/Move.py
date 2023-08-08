class Move:
    def __init__(self, player, cell):
        self._player = player
        self._cell = cell

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, value):
        self._player = value

    @property
    def cell(self):
        return self._cell

    @cell.setter
    def cell(self, value):
        self._cell = value
