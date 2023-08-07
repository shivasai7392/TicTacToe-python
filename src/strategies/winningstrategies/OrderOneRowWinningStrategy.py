from src.strategies.winningstrategies.IWinningStrategy import IWinningStrategy


class OrderOneRowWinningStrategy(IWinningStrategy):
    def __init__(self, dimension):
        self.counter = {}
        self.dimension = dimension
        for idx in range(dimension):
            self.counter[idx] = {}

    def checkWinner(self, move):
        shape = move.player.symbol.shape
        row = move.cell.row
        if shape in self.counter[row]:
            self.counter[row][shape] += 1
            if self.counter[row][shape] == self.dimension:
                return True
        else:
            self.counter[row][shape] = 1
        return False
