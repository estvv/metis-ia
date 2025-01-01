from objects.piece import Piece
from enums.colors import Colors
from utils.vector import Vector

class Pawn(Piece):
    def __init__(self, __name__: str, __color__: Colors, __x__: int = -1, __y__: int = -1) -> None:
        super().__init__(__name__, __color__, __x__, __y__)

    def get_legal_moves(self, board) -> list[tuple[Vector, Vector]]:
        moves = []
        direction = 1 if self.is_white() else -1

        forward_one = (self.coords.x, self.coords.y + direction)
        if board.is_move_legal(self.coords, Vector(forward_one)) and not board.is_enemy_at(self.coords, Vector(forward_one)):
            moves.append((self.coords, Vector(forward_one)))

        forward_two = (self.coords.x, self.coords.y + 2 * direction)
        if self.first_move and board.is_move_legal(self.coords, Vector(forward_two)) and not board.is_enemy_at(self.coords, Vector(forward_two)):
            moves.append((self.coords, Vector(forward_two)))

        for dx in [-1, 1]:
            diagonal = (self.coords.x + dx, self.coords.y + direction)
            if board.is_move_legal(self.coords, Vector(diagonal)) and board.is_enemy_at(self.coords, Vector(diagonal)):
                moves.append((self.coords, Vector(diagonal)))

        return moves

    def get_attack_moves(self, board) -> list[tuple[Vector, Vector]]:
        moves = []
        if self.is_white():
            # Left diagonal tile ahead
            left_diag = (self.coords.x - 1, self.coords.y + 1)
            if board.is_move_valid(self.coords, Vector(left_diag)):
                moves.append((self.coords, Vector(left_diag)))

            # Right diagonal tile ahead
            right_diag = (self.coords.x + 1, self.coords.y + 1)
            if board.is_move_valid(self.coords, Vector(right_diag)):
                moves.append((self.coords, Vector(right_diag)))
        else:
            # Left diagonal tile ahead
            left_diag = (self.coords.x - 1, self.coords.y - 1)
            if board.is_move_valid(self.coords, Vector(left_diag)):
                moves.append((self.coords, Vector(left_diag)))

            # Right diagonal tile ahead
            right_diag = (self.coords.x + 1, self.coords.y - 1)
            if board.is_move_valid(self.coords, Vector(right_diag)):
                moves.append((self.coords, Vector(right_diag)))
        return moves

    def get_controlled_tiles(self, board):
        return self.get_attack_moves(board)
