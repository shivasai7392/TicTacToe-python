class Symbol:
    def __init__(self):
        self._shape = None

    @property
    def shape(self):
        return self._shape

    @shape.setter
    def shape(self, value):
        self._shape = value
        