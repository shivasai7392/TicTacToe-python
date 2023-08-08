from src.models.Game import Game


class GameController:
    def createGame(self, dimension, players, winningStrategies):
        game = Game.getBuilder()\
                .setDimension(dimension)\
                .setPlayers(players)\
                .setWinningStrategies(winningStrategies).build()
        return game

    def displayBoard(self, game):
        game.printBoard()

    def undo(self, game):
        game.undo()

    def makeMove(self, game):
        game.makeMove()

    def printWinner(self, game):
        game.printBoard()
        game.printWinner()
