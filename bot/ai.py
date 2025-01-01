import random
from game.player import Player
from enums.colors import Colors
from objects.board import Board
from utils.vector import Vector


pst_b = {
    "p": [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [-31, 8, -7, -37, -36, -14, 3, -31],
        [-22, 9, 5, -11, -10, -2, 3, -19],
        [-26, 3, 10, 9, 6, 1, 0, -23],
        [-17, 16, -2, 15, 14, 0, 15, -13],
        [7, 29, 21, 44, 40, 31, 44, 7],
        [78, 83, 86, 73, 102, 82, 85, 90],
        [100, 100, 100, 100, 105, 100, 100, 100],
    ],
    "n": [
        [-74, -23, -26, -24, -19, -35, -22, -69],
        [-23, -15, 2, 0, 2, 0, -23, -20],
        [-18, 10, 13, 22, 18, 15, 11, -14],
        [-1, 5, 31, 21, 22, 35, 2, 0],
        [24, 24, 45, 37, 33, 41, 25, 17],
        [10, 67, 1, 74, 73, 27, 62, -2],
        [-3, -6, 100, -36, 4, 62, -4, -14],
        [-66, -53, -75, -75, -10, -55, -58, -70],
    ],
    "b": [
        [-7, 2, -15, -12, -14, -15, -10, -10],
        [19, 20, 11, 6, 7, 6, 20, 16],
        [14, 25, 24, 15, 8, 25, 20, 15],
        [13, 10, 17, 23, 17, 16, 0, 7],
        [25, 17, 20, 34, 26, 25, 15, 10],
        [-9, 39, -32, 41, 52, -10, 28, -14],
        [-11, 20, 35, -42, -39, 31, 2, -22],
        [-59, -78, -82, -76, -23, -107, -37, -50],
    ],
    "r": [
        [-30, -24, -18, 5, -2, -18, -31, -32],
        [-53, -38, -31, -26, -29, -43, -44, -53],
        [-42, -28, -42, -25, -25, -35, -26, -46],
        [-28, -35, -16, -21, -13, -29, -46, -30],
        [0, 5, 16, 13, 18, -4, -9, -6],
        [19, 35, 28, 33, 45, 27, 25, 15],
        [55, 29, 56, 67, 55, 62, 34, 60],
        [35, 29, 33, 4, 37, 33, 56, 50],
    ],
    "q": [
        [-39, -30, -31, -13, -31, -36, -34, -42],
        [-36, -18, 0, -19, -15, -15, -21, -38],
        [-30, -6, -13, -11, -16, -11, -16, -27],
        [-14, -15, -2, -5, -1, -10, -20, -22],
        [1, -16, 22, 17, 25, 20, -13, -6],
        [-2, 43, 32, 60, 72, 63, 43, 2],
        [14, 32, 60, -10, 20, 76, 57, 24],
        [6, 1, -8, -104, 69, 24, 88, 26],
    ],
    "k": [
        [17, 30, -3, -14, 6, -1, 40, 18],
        [-4, 3, -14, -50, -57, -18, 13, 4],
        [-47, -42, -43, -79, -64, -32, -29, -32],
        [-55, -43, -52, -28, -51, -47, -8, -50],
        [-55, 50, 11, -4, -19, 13, 0, -49],
        [-62, 12, -57, 44, -67, 28, 37, -31],
        [-32, 10, 55, 56, 56, 55, 10, 3],
        [4, 54, 47, -99, -99, 60, 83, -62],
    ],
}

pst_w = {key: [row[::-1] for row in value[::-1]] for key, value in pst_b.items()}

class AI(Player):
    def __init__(self) -> None:
        return

    def is_player(self) -> bool:
        return False

    def get_color(self):
        return self.color

    def get_opponent_color(self) -> Colors:
        if self.color == Colors.white:
            return Colors.black
        return Colors.white

    def get_opposite_color(self, color: Colors):
        if color == Colors.white:
            return Colors.black
        return Colors.white

    def get_pieces_weight(self, board: Board):
        score = 0
        for piece in board.get_pieces():
            if piece.name != "king":
                if piece.get_color() == self.color:
                    score += piece.weight.value
                else:
                    score -= piece.weight.value
        return score

    def pawn_control_center(self, board: Board) -> int:
        center_squares = [Vector(3, 3), Vector(3, 4), Vector(4, 3), Vector(4, 4)]
        score = 0
        for piece in board.get_pieces():
            if piece.name == "pawn" and piece.coords in center_squares:
                if piece.get_color() == self.color:
                    score += 50
                else:
                    score -= 50
        return score

    def piece_control_center(self, board: Board) -> int:
        center_squares = [Vector(3, 3), Vector(3, 4), Vector(4, 3), Vector(4, 4)]
        score = 0
        for piece in board.get_pieces():
            for (source, target) in piece.get_attack_moves(board):
                if target in center_squares:
                    if piece.get_color() == self.color:
                        score += 30
                    else:
                        score -= 30
        return score

    def evaluate_board(self, board: Board, my_turn: bool):
        score = 0
        score += self.get_pieces_weight(board)
        score += self.pawn_control_center(board)
        score += self.piece_control_center(board)
        if my_turn:
            return -score
        return score

    def minimax(self, board: Board, depth: int, alpha: float, beta: float, my_turn: bool, level: int = 0):
        if depth == 0:
            score = self.evaluate_board(board, my_turn)
            return score, None
        if my_turn:
            max_eval = -float("inf")
            best_move = None
            moves = board.get_color_legal_moves(self.color)
            random.shuffle(moves)
            for (source, target) in moves:
                board.make_move(source, target)
                temporary_eval, _ = self.minimax(board, depth - 1, alpha, beta, False, level + 1)
                board.unmake_move()

                if temporary_eval >= max_eval:
                    max_eval = temporary_eval
                    best_move = (source, target)

                alpha = max(alpha, temporary_eval)
                if alpha < beta:
                    break

            return max_eval, best_move

        else:
            min_eval = float("inf")
            best_move = None
            moves = board.get_color_legal_moves(self.get_opponent_color())
            random.shuffle(moves)
            for (source, target) in moves:
                board.make_move(source, target)
                temporary_eval, _ = self.minimax(board, depth - 1, alpha, beta, True, level + 1)
                board.unmake_move()

                if temporary_eval <= min_eval:
                    min_eval = temporary_eval
                    best_move = (source, target)

                beta = min(beta, temporary_eval)
                if beta < alpha:
                    break

            return min_eval, best_move

    def get_best_move(self, board, depth=3) -> str:
        _, (source, target) = self.minimax(board, depth, -float("inf"), float("inf"), True)
        return (source, target)
