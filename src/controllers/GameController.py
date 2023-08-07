from src.models.Game import Game


class GameController:
    def createGame(self, dimension, players, winningStrategies):
        game = Game.getBuilder()\
                .setDimension(dimension)\
                .setPlayers(players)\
                .setWinningStrategies(winningStrategies).build()
        return game

