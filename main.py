# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from src.controllers.GameController import GameController


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Create a Game with a board of dimension 3
    game_controller = GameController()
    game_controller.createGame()
    # Create 2 players
    # while Game status is in progress
    # Ask if anyone wants to make a undo move
    # if yes undo
    # if no
    # tell whos turn it is
    # if human user take input from user
    # first row and then col - zero based index
    # else make move from bot

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
