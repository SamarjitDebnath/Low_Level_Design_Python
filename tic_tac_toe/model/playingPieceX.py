from model.playingPiece import PlayingPiece
from model.pieceType import PieceType


class PlayingPieceX(PlayingPiece):
    def __init__(self):
        super().__init__(PieceType.cross)
