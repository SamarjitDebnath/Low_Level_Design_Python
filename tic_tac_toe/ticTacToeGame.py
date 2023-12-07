from model.pieceType import PieceType
from model.player import Player
from model.board import Board
from model.playingPieceX import PlayingPieceX
from model.playingPieceO import PlayingPieceO
from model.player import Player
from typing import List, Dict


class TicTacToeGame:

    players: list[Player] = []
    gameBoard: Board = Board()

    def __init__(self):
        self.initializeGame()

    def initializeGame(self):
        TicTacToeGame.players = []
        crossPiece: PlayingPieceX = PlayingPieceX()
        player1: Player = Player("player1", crossPiece)
        TicTacToeGame.players.append(player1)

        noughtPiece: PlayingPieceO = PlayingPieceO()
        player2: Player = Player("player2", noughtPiece)
        TicTacToeGame.players.append(player2)

        TicTacToeGame.gameBoard = Board(3)

    def startGame(self) -> str:
        noWinner: bool = True

        while noWinner:
            # take out the player whose turn is and also put the player in the list back
            playerTurn: Player = TicTacToeGame.players.pop(0)

            # get the free space from the board
            TicTacToeGame.gameBoard.printBoard()
            freeSpaces: List[Dict[int, int]
                             ] = TicTacToeGame.gameBoard.getFreeCells()
            if not freeSpaces:
                noWinner = False
                continue

            # read user input from console game board
            inputScanner = input(
                f"Player: {playerTurn.name} enter row, column: ")
            row, column = inputScanner.split(',')
            row, column = int(row), int(column)

            # place the piece
            pieceAddedSuccessfully: bool = TicTacToeGame.gameBoard.addPiece(
                row, column, playerTurn.playing_piece)
            if not pieceAddedSuccessfully:
                print("Invalid position, please try again")
                TicTacToeGame.players.insert(0, playerTurn)
                continue
            TicTacToeGame.players.append(playerTurn)

            winner: bool = self.isThereWinner(
                row, column, playerTurn.playing_piece.piece_type)
            if winner:
                TicTacToeGame.gameBoard.printBoard()
                return playerTurn.name

        return "tie!"

    def isThereWinner(self, row: int, column: int, piece_type: PieceType) -> bool:
        rowMatch: bool = True
        columnMatch: bool = True
        diagonalMatch: bool = True
        antiDiagonalMatch: bool = True

        if TicTacToeGame.gameBoard.size:
            for i in range(TicTacToeGame.gameBoard.size):
                if (TicTacToeGame.gameBoard.board[row][i].piece_type == PieceType.EMPTY or TicTacToeGame.gameBoard.board[row][i].piece_type != piece_type):
                    rowMatch = False

            for i in range(TicTacToeGame.gameBoard.size):
                if (TicTacToeGame.gameBoard.board[i][column].piece_type == PieceType.EMPTY or TicTacToeGame.gameBoard.board[i][column].piece_type != piece_type):
                    columnMatch = False

            for i in range(TicTacToeGame.gameBoard.size):
                if (TicTacToeGame.gameBoard.board[i][i].piece_type == PieceType.EMPTY or TicTacToeGame.gameBoard.board[i][i].piece_type != piece_type):
                    diagonalMatch = False

            for i in range(TicTacToeGame.gameBoard.size):
                if (TicTacToeGame.gameBoard.board[i][~i].piece_type == PieceType.EMPTY or TicTacToeGame.gameBoard.board[i][~i].piece_type != piece_type):
                    antiDiagonalMatch = False

        return rowMatch or columnMatch or diagonalMatch or antiDiagonalMatch
