from src.strategies.winningstrategies.IWinningStrategy import IWinningStrategy


class OrderOneDiagonalWinningStrategy(IWinningStrategy):
    def __init__(self, dimension):
        self.dimension = dimension
        self.counter = {}
        for idx in range(2):
            self.counter[idx] = {}

    def checkWinner(self, move):
        shape = move.player.symbol.shape
        row = move.cell.row
        col = move.cell.col
        if row == col:
            if shape in self.counter[0]:
                self.counter[0][shape] += 1
                if self.counter[0][shape] == self.dimension:
                    return True
            else:
                self.counter[0][shape] = 1
        if row + col == self.dimension - 1:
            if shape in self.counter[1]:
                self.counter[1][shape] += 1
                if self.counter[1][shape] == self.dimension:
                    return True
            else:
                self.counter[1][shape] = 1
        return False

    def undo(self, move):
        shape = move.player.symbol.shape
        col = move.cell.col
        row = move.cell.row
        if row == col:
            self.counter[0][shape] -= 1
        if row+col == self.dimension - 1:
            self.counter[1][shape] -= 1
