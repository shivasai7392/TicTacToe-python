import abc


class IBotPlayingStrategy(abc.ABC):
    @abc.abstractmethod
    def makeMove(self, board):
        pass
