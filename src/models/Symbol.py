class Symbol:
    def __init__(self, shape):
        self._shape = shape

    @property
    def shape(self):
        return self._shape

    @shape.setter
    def shape(self, value):
        self._shape = value
        