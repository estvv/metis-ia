from objects.piece import Piece
from enums.colors import Colors
from utils.vector import Vector

class Knight(Piece):
    def __init__(self, __name__: str, __color__: Colors, __x__: int = -1, __y__: int = -1) -> None:
        super().__init__(__name__, __color__, __x__, __y__)
        self.first_letter = "n"

    def get_legal_moves(self, board)-> list[tuple[int, int, int, int]]:
        moves = []

        # top left
        self.is_move_legal(board, moves, (self.coords.x - 1, self.coords.y - 2))
        # top right
        self.is_move_legal(board, moves, (self.coords.x + 1, self.coords.y - 2))
        # bottom let
        self.is_move_legal(board, moves, (self.coords.x - 1, self.coords.y + 2))
        # bottom right
        self.is_move_legal(board, moves, (self.coords.x + 1, self.coords.y + 2))
        # right top
        self.is_move_legal(board, moves, (self.coords.x + 2, self.coords.y + 1))
        # right bottom
        self.is_move_legal(board, moves, (self.coords.x + 2, self.coords.y - 1))
        # left top
        self.is_move_legal(board, moves, (self.coords.x - 2, self.coords.y + 1))
        # left bottom
        self.is_move_legal(board, moves, (self.coords.x - 2, self.coords.y - 1))

        return moves

    def is_move_legal(self, board, moves: list, move: tuple) -> None:
        if board.is_move_legal(self.coords, Vector(move)):
            moves.append((self.coords, Vector(move)))

    def get_attack_moves(self, board)-> list[tuple[int, int, int, int]]:
        moves = []

        # top left
        self.is_move_valid(board, moves, (self.coords.x - 1, self.coords.y - 2))
        # top right
        self.is_move_valid(board, moves, (self.coords.x + 1, self.coords.y - 2))
        # bottom let
        self.is_move_valid(board, moves, (self.coords.x - 1, self.coords.y + 2))
        # bottom right
        self.is_move_valid(board, moves, (self.coords.x + 1, self.coords.y + 2))
        # right top
        self.is_move_valid(board, moves, (self.coords.x + 2, self.coords.y + 1))
        # right bottom
        self.is_move_valid(board, moves, (self.coords.x + 2, self.coords.y - 1))
        # left top
        self.is_move_valid(board, moves, (self.coords.x - 2, self.coords.y + 1))
        # left bottom
        self.is_move_valid(board, moves, (self.coords.x - 2, self.coords.y - 1))

        return moves

    def is_move_valid(self, board, moves: list, move: tuple) -> None:
        if board.is_move_valid(self.coords, Vector(move)):
            moves.append((self.coords, Vector(move)))

    def get_controlled_tiles(self, board):
        return self.get_attack_moves(board)
