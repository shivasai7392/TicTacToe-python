from src.models.Board import Board
from src.models.PlayerType import PlayerType


class Game:
    def __init__(self, dimension, players, winningStrategies):
        self._moves = None
        self._board = Board(dimension)
        self._players = players
        self._currentPlayerIndex = 0
        self._winningStrategies = winningStrategies
        self._gameStatus = None
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
