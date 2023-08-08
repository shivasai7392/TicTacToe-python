# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from src.controllers.GameController import GameController
from src.models.DifficlutyLevel import DifficultyLevel
from src.models.GameStatus import GameStatus
from src.models.Player import Player
from src.models.Bot import Bot
from src.models.PlayerType import PlayerType
from src.models.Symbol import Symbol
from src.strategies.winningstrategies.OrderOneColWinningStrategy import OrderOneColWinningStrategy
from src.strategies.winningstrategies.OrderOneDiagWinningStrategy import OrderOneDiagonalWinningStrategy
from src.strategies.winningstrategies.OrderOneRowWinningStrategy import OrderOneRowWinningStrategy


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Create a Game with a board of dimension 3, 2 players and one winning strategy
    dimension = 3
    players = [Player("Shiva", Symbol("X"), PlayerType.HUMAN), Bot(DifficultyLevel.EASY)]
    winnning_strategies = [OrderOneColWinningStrategy(dimension),
                           OrderOneRowWinningStrategy(dimension),
                           OrderOneDiagonalWinningStrategy(dimension)]
    game_controller = GameController()
    game = game_controller.createGame(3, players, winnning_strategies)

    # while Game status is in progress
    # print the Game
    # Ask if anyone wants to make a undo move
    # if yes undo
    # if no
    # tell whos turn it is
    # if human user take input from user
    # first row and then col - zero based index
    # else make move from bot
    while game.gameStatus == GameStatus.IN_PROGRESS:
        game_controller.displayBoard(game)
        print("Anyone wants to Undo. Y/N")
        undo_string = input()
        if undo_string.lower() == "y":
            game_controller.undo(game)
        else:
            game_controller.makeMove(game)
    if game.gameStatus == GameStatus.ENDED:
        game_controller.printWinner(game)
    else:
        game_controller.displayBoard()
        print("Game is a Draw.")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
