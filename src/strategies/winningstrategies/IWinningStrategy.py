import abc


class IWinningStrategy(abc.ABC):
    @abc.abstractmethod
    def checkWinner(self, move):
        pass
