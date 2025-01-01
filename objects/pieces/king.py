from objects.piece import Piece
from enums.colors import Colors
from utils.vector import Vector

class King(Piece):
    def __init__(self, __name__: str, __color__: Colors, __x__: int = -1, __y__: int = -1) -> None:
        super().__init__(__name__, __color__, __x__, __y__)

    def get_legal_moves(self, board) -> list[tuple[Vector, Vector]]:
        moves = []
        for x in range(self.coords.x - 1, self.coords.x + 2):
            for y in range(self.coords.y - 1, self.coords.y + 2):
                if board.is_move_legal(self.coords, Vector(x, y)):
                    moves.append((self.coords, Vector(x, y)))
        return moves

    def get_attack_moves(self, board) -> list[tuple[Vector, Vector]]:
        return []

    def get_controlled_tiles(self, board):
        moves = []
        for x in range(self.coords.x - 1, self.coords.x + 2):
            for y in range(self.coords.y - 1, self.coords.y + 2):
                if board.is_move_valid(self.coords, Vector(x, y)):
                    moves.append((self.coords, Vector(x, y)))
        return moves
