from src.strategies.winningstrategies.IWinningStrategy import IWinningStrategy


class OrderOneColWinningStrategy(IWinningStrategy):
    def __init__(self, dimension):
        self.dimension = dimension
        self.counter = {}
        for idx in range(dimension):
            self.counter[idx] = {}

    def checkWinner(self, move):
        shape = move.player.symbol.shape
        col = move.cell.col
        if shape in self.counter[col]:
            self.counter[col][shape] += 1
            if self.counter[col][shape] == self.dimension:
                return True
        else:
            self.counter[col][shape] = 1
        return False

    def undo(self, move):
        shape = move.player.symbol.shape
        col = move.cell.col
        self.counter[col][shape] -= 1
