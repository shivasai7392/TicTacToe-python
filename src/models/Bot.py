class Bot:
    def __init__(self):
        self._difficultyLevel = None

    @property
    def difficultyLevel(self):
        return self._difficultyLevel

    @difficultyLevel.setter
    def difficultyLevel(self, value):
        self._difficultyLevel = value
