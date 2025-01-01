from objects.piece import Piece
from enums.colors import Colors
from utils.vector import Vector

class Bishop(Piece):
    def __init__(self, __name__: str, __color__: Colors, __x__: int = -1, __y__: int = -1) -> None:
        super().__init__(__name__, __color__, __x__, __y__)

    def get_legal_moves(self, board) -> list[tuple[Vector, Vector]]:
        moves = []
        left_bottom_state = True
        left_top_state = True
        right_bottom_state = True
        right_top_state = True

        i = 0
        while left_bottom_state or left_top_state or right_bottom_state or right_top_state:
            left_bottom = Vector(self.coords.x - 1 - i, self.coords.y + 1 + i)
            left_top = Vector(self.coords.x - 1 - i, self.coords.y - 1 - i)
            right_bottom = Vector(self.coords.x + 1 + i, self.coords.y + 1 + i)
            right_top = Vector(self.coords.x + 1 + i, self.coords.y - 1 - i)

            if left_bottom_state:
                left_bottom_state = self.is_move_legal(board, moves, left_bottom)

            if left_top_state:
                left_top_state = self.is_move_legal(board, moves, left_top)

            if right_bottom_state:
                right_bottom_state = self.is_move_legal(board, moves, right_bottom)

            if right_top_state:
                right_top_state = self.is_move_legal(board, moves, right_top)
            i += 1
        return moves

    def is_move_legal(self, board, moves: list, dest: Vector) -> bool:
        if not board.is_move_legal(self.coords, dest):
            return False
        elif board.is_enemy_at(self.coords, dest):
            moves.append((self.coords, dest))
            return False
        moves.append((self.coords, dest))
        return True

    def get_attack_moves(self, board) -> list[tuple[Vector, Vector]]:
        moves = []
        left_bottom_state = True
        left_top_state = True
        right_bottom_state = True
        right_top_state = True

        i = 0
        while left_bottom_state or left_top_state or right_bottom_state or right_top_state:
            left_bottom = Vector(self.coords.x - 1 - i, self.coords.y + 1 + i)
            left_top = Vector(self.coords.x - 1 - i, self.coords.y - 1 - i)
            right_bottom = Vector(self.coords.x + 1 + i, self.coords.y + 1 + i)
            right_top = Vector(self.coords.x + 1 + i, self.coords.y - 1 - i)

            if left_bottom_state:
                left_bottom_state = self.is_move_valid(board, moves, left_bottom)

            if left_top_state:
                left_top_state = self.is_move_valid(board, moves, left_top)

            if right_bottom_state:
                right_bottom_state = self.is_move_valid(board, moves, right_bottom)

            if right_top_state:
                right_top_state = self.is_move_valid(board, moves, right_top)
            i += 1
        return moves

    def is_move_valid(self, board, moves: list, dest: Vector) -> bool:
        if not board.is_move_valid(self.coords, dest):
            return False
        elif board.is_enemy_at(self.coords, dest):
            moves.append((self.coords, dest))
            return False
        moves.append((self.coords, dest))
        return True

    def get_controlled_tiles(self, board) -> list[tuple[Vector, Vector]]:
        moves = []
        i = 1
        while True:
            targets = [
                Vector(self.coords.x - i, self.coords.y + i),
                Vector(self.coords.x - i, self.coords.y - i),
                Vector(self.coords.x + i, self.coords.y + i),
                Vector(self.coords.x + i, self.coords.y - i)
            ]

            control_exists = False

            for target in targets:
                if board.is_move_valid(self.coords, target):
                    moves.append((self.coords, target))
                    control_exists = True

            if not control_exists:
                break

            i += 1
        return moves

