from model.pieceType import PieceType
from model.playingPiece import PlayingPiece
from typing import Optional, List, Dict
from model.playingPieceX import PlayingPieceX


class Board():

    def __init__(self, size: Optional[int] = None):
        self.size = size
        self.board: list[list[PlayingPiece]] = [[]]
        if self.size:
            self.board: list[list[PlayingPiece]] = [
                [PlayingPiece(PieceType.EMPTY) for _ in range(self.size)] for _ in range(self.size)
            ]

    def addPiece(self, row: int, column: int, playing_piece: PlayingPiece) -> bool:
        if self.board[row][column].piece_type != PieceType.EMPTY:
            return False
        self.board[row][column] = playing_piece
        return True

    def getFreeCells(self) -> List[Dict[int, int]]:
        freeCells: List[Dict[int, int]] = []

        if self.size:
            for i in range(self.size):
                for j in range(self.size):
                    if self.board[i][j].piece_type == PieceType.EMPTY:
                        rowColumn: Dict[int, int] = {i: j}
                        freeCells.append(rowColumn)
        return freeCells

    def printBoard(self):
        if self.size:
            for i in range(self.size):
                for j in range(self.size):
                    if self.board[i][j] != PieceType.EMPTY:
                        print(
                            f"{' ' if self.board[i][j].piece_type.value == None else self.board[i][j].piece_type.value}", end=" ")
                    else:
                        print(" ")

                    print("__|__", end="")
                print()
