from model.playingPiece import PlayingPiece


class Player:
    def __init__(self, name: str, playing_piece: PlayingPiece):
        self._name = name
        self._playing_piece = playing_piece

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def playing_piece(self):
        return self._playing_piece

    @playing_piece.setter
    def playing_piece(self, playing_piece: PlayingPiece):
        self._playing_piece = playing_piece
