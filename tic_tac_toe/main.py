from ticTacToeGame import TicTacToeGame


def main():
    game: TicTacToeGame = TicTacToeGame()
    result = game.startGame()
    if result != "tie":
        print(f"Winner of this game: {result}")
    else:
        print("Draw!!")


if __name__ == "__main__":
    main()
