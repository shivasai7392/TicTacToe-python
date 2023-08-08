from src.models.Board import Board
from src.models.CellStatus import CellStatus
from src.models.GameStatus import GameStatus
from src.models.Move import Move
from src.models.PlayerType import PlayerType


class Game:
    def __init__(self, dimension, players, winningStrategies):
        self._moves = []
        self._board = Board(dimension)
        self._players = players
        self._currentPlayerIndex = 0
        self._winningStrategies = winningStrategies
        self._gameStatus = GameStatus.IN_PROGRESS
        self._winner = None

    @property
    def moves(self):
        return self._moves

    @moves.setter
    def moves(self, value):
        self._moves = value

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, value):
        self._board = value

    @property
    def players(self):
        return self._players

    @players.setter
    def players(self, value):
        self._players = value

    @property
    def currentPlayerIndex(self):
        return self._currentPlayerIndex

    @currentPlayerIndex.setter
    def currentPlayerIndex(self, value):
        self._currentPlayerIndex = value

    @property
    def winningStrategies(self):
        return self._winningStrategies

    @winningStrategies.setter
    def winningStrategies(self, value):
        self._winningStrategies = value

    @property
    def gameStatus(self):
        return self._gameStatus

    @gameStatus.setter
    def gameStatus(self, value):
        self._gameStatus = value

    @property
    def winner(self):
        return self._winner

    @winner.setter
    def winner(self, value):
        self._winner = value

    def printBoard(self):
        self.board.print()

    def undo(self):
        if len(self.moves) == 0:
            print("Undo option is not available")
            return
        move = self.moves[-1]
        cell = move.cell
        row = cell.row
        col = cell.col
        grid = self.board.grid
        grid_cell = grid[row][col]
        grid_cell.cellStatus = CellStatus.EMPTY
        grid_cell.player = None

        for strategy in self.winningStrategies:
            strategy.undo(move)

        self.moves.pop()

        self.currentPlayerIndex -= 1
        self.currentPlayerIndex += (self.board.size-1)
        self.currentPlayerIndex %= (self.board.size-1)

    def makeMove(self):
        player = self.players[self.currentPlayerIndex]
        print(player.name+"'s Turn.")
        proposed_cell = player.makeMove(self.board)
        if not self.validateMove(proposed_cell):
            print("Invalid Move.")
            return
        actual_cell = self.board.grid[proposed_cell.row][proposed_cell.col]
        actual_cell.row = proposed_cell.row
        actual_cell.col = proposed_cell.col
        actual_cell.cellStatus = CellStatus.FILLED
        actual_cell.player = player

        move = Move(player, proposed_cell)
        self.moves.append(move)

        for strategy in self.winningStrategies:
            if strategy.checkWinner(move):
                self.winner = player
                self.gameStatus = GameStatus.ENDED
                return

        self.currentPlayerIndex += 1
        self.currentPlayerIndex %= (self.board.size - 1)

        if len(self.moves) == self.board.size**2:
            self.gameStatus = GameStatus.DRAW
            return

    def validateMove(self, cell):
        if cell.row < 0 or cell.row >= self.board.size or cell.col < 0 or cell.col >= self.board.size or self.board.grid[cell.row][cell.col].cellStatus == CellStatus.FILLED:
            return False
        return True

    def printWinner(self):
        print(self.winner.name+" had won the game.")

    class Builder:

        def __init__(self):
            self.dimension = 0
            self.players = None
            self.winningStrategies = None

        def setDimension(self, dimension):
            self.dimension = dimension
            return self

        def setPlayers(self, players):
            self.players = players
            return self

        def setWinningStrategies(self, winningStrategies):
            self.winningStrategies = winningStrategies
            return self

        def validate(self):
            if self.dimension <= 2:
                return False
            if len(self.players) != self.dimension - 1:
                return False
            bot_count = 0
            for player in self.players:
                if player.playerType == PlayerType.BOT:
                    bot_count += 1
                    if bot_count > 1:
                        return False
            if not self.winningStrategies or len(self.winningStrategies) <= 0:
                return False
            return True

        def build(self):
            if self.validate():
                return Game(self.dimension, self.players, self.winningStrategies)
            print("Invalid Game")

    @staticmethod
    def getBuilder():
        return Game.Builder()
