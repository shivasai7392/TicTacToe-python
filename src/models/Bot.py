from src.models.Player import Player
from src.models.PlayerType import PlayerType
from src.models.Symbol import Symbol
from src.strategies.botplayingstrategies.BotFactory import BotFactory


class Bot(Player):
    def __init__(self, difficultyLevel):
        super().__init__("BOT", Symbol("O"), PlayerType.BOT)
        self._difficultyLevel = difficultyLevel
        self._botPlayingStrategy = BotFactory.getBotPlayingStrategyBasedOnDifficulty(difficultyLevel)

    @property
    def difficultyLevel(self):
        return self._difficultyLevel

    @difficultyLevel.setter
    def difficultyLevel(self, value):
        self._difficultyLevel = value

    @property
    def botPlayingStrategy(self):
        return self._botPlayingStrategy

    @botPlayingStrategy.setter
    def botPlayingStrategy(self, value):
        self._botPlayingStrategy = value

    def makeMove(self, board):
        return self.botPlayingStrategy.makeMove(board)

