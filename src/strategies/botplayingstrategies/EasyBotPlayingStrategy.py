from src.strategies.botplayingstrategies.IBotPlayingStrategy import IBotPlayingStrategy


class EasyBotPlayingStrategy(IBotPlayingStrategy):
    def makeMove(self, board):
        grid = board.grid
        for cells in grid:
            for cell in cells:
                if cell.cellStatus is None:
                    return cell
