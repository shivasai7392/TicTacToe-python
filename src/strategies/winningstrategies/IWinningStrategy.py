import abc


class IWinningStrategy(abc.ABC):
    @abc.abstractmethod
    def checkWinner(self, move):
        pass

    @abc.abstractmethod
    def undo(self, move):
        pass
