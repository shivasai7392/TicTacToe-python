from src.models.DifficlutyLevel import DifficultyLevel
from src.strategies.botplayingstrategies.EasyBotPlayingStrategy import EasyBotPlayingStrategy


class BotFactory:
    @staticmethod
    def getBotPlayingStrategyBasedOnDifficulty(difficultyLevel):
        if difficultyLevel == DifficultyLevel.EASY:
            return EasyBotPlayingStrategy()
        elif difficultyLevel == DifficultyLevel.MEDIUM:
            return EasyBotPlayingStrategy()
        return EasyBotPlayingStrategy()
