from objects.piece import Piece
from enums.colors import Colors
from utils.vector import Vector

class Rook(Piece):
    def __init__(self, __name__: str, __color__: Colors, __x__: int = -1, __y__: int = -1) -> None:
        super().__init__(__name__, __color__, __x__, __y__)

    def get_legal_moves(self, board) -> list[tuple[Vector, Vector]]:
        moves = []
        bottom_state = True
        top_state = True
        right_state = True
        left_state = True
        i = 0

        while bottom_state or top_state or right_state or left_state:
            bottom = Vector(self.coords.x, self.coords.y + 1 + i)
            top = Vector(self.coords.x, self.coords.y - 1 - i)
            right = Vector(self.coords.x + 1 + i, self.coords.y)
            left = Vector(self.coords.x - 1 - i, self.coords.y)

            if bottom_state:
                bottom_state = self.is_move_legal(board, moves, bottom)

            if top_state:
                top_state = self.is_move_legal(board, moves, top)

            if right_state:
                right_state = self.is_move_legal(board, moves, right)

            if left_state:
                left_state = self.is_move_legal(board, moves, left)
            i += 1
        return moves

    def is_move_legal(self, board, moves: list, move: Vector) -> bool:
        if not board.is_move_legal(self.coords, move):
            return False
        elif board.is_enemy_at(self.coords, move):
            moves.append((self.coords, move))
            return False
        moves.append((self.coords, move))
        return True

    def get_attack_moves(self, board) -> list[tuple[Vector, Vector]]:
        moves = []
        bottom_state = True
        top_state = True
        right_state = True
        left_state = True
        i = 0

        while bottom_state or top_state or right_state or left_state:
            bottom = Vector(self.coords.x, self.coords.y + 1 + i)
            top = Vector(self.coords.x, self.coords.y - 1 - i)
            right = Vector(self.coords.x + 1 + i, self.coords.y)
            left = Vector(self.coords.x - 1 - i, self.coords.y)

            if bottom_state:
                bottom_state = self.is_move_valid(board, moves, bottom)

            if top_state:
                top_state = self.is_move_valid(board, moves, top)

            if right_state:
                right_state = self.is_move_valid(board, moves, right)

            if left_state:
                left_state = self.is_move_valid(board, moves, left)
            i += 1
        return moves

    def is_move_valid(self, board, moves: list, move: Vector) -> bool:
        if not board.is_move_valid(self.coords, move):
            return False
        elif board.is_enemy_at(self.coords, move):
            moves.append((self.coords, move))
            return False
        moves.append((self.coords, move))
        return True

    def get_controlled_tiles(self, board) -> list[tuple[Vector, Vector]]:
        moves = []
        bottom_state = True
        top_state = True
        right_state = True
        left_state = True
        i = 0

        while bottom_state or top_state or right_state or left_state:
            bottom = Vector(self.coords.x, self.coords.y + 1 + i)
            top = Vector(self.coords.x, self.coords.y - 1 - i)
            right = Vector(self.coords.x + 1 + i, self.coords.y)
            left = Vector(self.coords.x - 1 - i, self.coords.y)

            if bottom_state:
                bottom_state = self.is_tile_controlled(board, moves, bottom)

            if top_state:
                top_state = self.is_tile_controlled(board, moves, top)

            if right_state:
                right_state = self.is_tile_controlled(board, moves, right)

            if left_state:
                left_state = self.is_tile_controlled(board, moves, left)
            i += 1
        return moves

    def is_tile_controlled(self, board, moves: list, move: Vector) -> bool:
        if not board.is_move_valid(self.coords, move):
            return False
        moves.append((self.coords, move))
        return True
