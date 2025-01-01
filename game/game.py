
import time
from bot.ai import AI
from game.player import Player
from objects.board import Board
from enums.colors import Colors
from utils.vector import Vector
from utils.annotations import annotations_to_coordinates, is_annotations_correct

class Game:
    p1: AI = None
    p2: AI = None
    board: Board = None
    p_turn: Player = None

    def __init__(self) -> None:
        self.board = Board()
        self.board.init_board_with_pieces()
        self.p1 = Player()
        self.p2 = AI()

    def next_turn(self) -> None:
        if self.p_turn == self.p1:
            self.p_turn = self.p2
        else:
            self.p_turn = self.p1

    def bot_turn(self, bot: AI) -> None:
        move = bot.get_best_move(self.board)
        if not move:
            print(f"END GAME {bot.color} lost !")
            exit()
        self.board.make_move(move[0], move[1])

    def player_turn(self):
        move: str = None
        source: Vector = None
        target: Vector = None

        while 1:
            move = input("Enter a move >")
            if is_annotations_correct(move):
                source = annotations_to_coordinates(move[1], move[2])
                target = annotations_to_coordinates(move[3], move[4])
                if self.board.make_move(source, target):
                    break
                else:
                    print(f"Cant move : {source} {target}")

    def interactive_player(self):
        while 1:
            p_type = input("Choose the type of the first player").strip().lower()

            if p_type == "player":
                self.p1 = Player()
                break
            if p_type == "ia" or p_type == "ai":
                self.p1 = AI()
                break

        while 1:
            p_type = input("Choose the type of the second player").strip().lower()

            if p_type == "player":
                self.p2 = Player()
                break
            if p_type == "ia" or p_type == "ai":
                self.p2 = AI()
                break

    def player_vs_bot(self):
        if self.p_turn == self.p1:
            if self.board.is_game_over():
                print("END GAME")
                exit()
            self.player_turn()
        else:
            self.bot_turn(self.p2)

    def bot_vs_bot(self):
        self.bot_turn(self.p_turn)

    def interactive_game(self):
        self.p1 = AI()
        self.p1.update_color(Colors.white)
        self.p2 = AI()
        self.p2.update_color(Colors.black)
        self.p_turn = self.p1

        while 1:
            self.board.display()
            # self.player_turn()
            self.bot_turn(self.p_turn)
            self.next_turn()
