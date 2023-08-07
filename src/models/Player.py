class Player:
    def __init__(self):
        self._name = None
        self._symbol = None
        self._playerType = None

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
