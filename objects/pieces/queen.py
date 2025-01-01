from objects.piece import Piece
from enums.colors import Colors
from objects.pieces.rook import Rook
from objects.pieces.bishop import Bishop

class Queen(Piece):
    def __init__(self, __name__: str, __color__: Colors, __x__: int = -1, __y__: int = -1) -> None:
        super().__init__(__name__, __color__, __x__, __y__)

    def get_legal_moves(self, board)-> list[tuple[int, int, int, int]]:
        return Rook("rook", self.color, self.coords.x, self.coords.y).get_legal_moves(board) + Bishop("bishop", self.color, self.coords.x, self.coords.y).get_legal_moves(board)

    def get_attack_moves(self, board)-> list[tuple[int, int, int, int]]:
        return Rook("rook", self.color, self.coords.x, self.coords.y).get_attack_moves(board) + Bishop("bishop", self.color, self.coords.x, self.coords.y).get_attack_moves(board)

    def get_controlled_tiles(self, board)-> list[tuple[int, int, int, int]]:
        return Rook("rook", self.color, self.coords.x, self.coords.y).get_controlled_tiles(board) + Bishop("bishop", self.color, self.coords.x, self.coords.y).get_controlled_tiles(board)
