import copy
from objects.tile import Tile
from enums.colors import Colors
from objects.piece import Piece
from utils.vector import Vector
from objects.pieces.king import King
from objects.pieces.rook import Rook
from objects.pieces.pawn import Pawn
from objects.pieces.queen import Queen
from objects.pieces.knight import Knight
from objects.pieces.bishop import Bishop
from utils.annotations import ROW_ANNOTATIONS, COL_ANNOTATIONS

class Board:
    past_moves: list[dict] = []
    chessboard: list[list[Tile]]

    def __init__(self) -> None:
        self.init_empty_board()

    def __str__(self) -> str:
        chessboard = ""
        for i in range(len(self.chessboard)):
            for j in range(len(self.chessboard)):
                if self.chessboard[i][j].piece:
                    chessboard += self.chessboard[i][j].piece.character
                else:
                    chessboard += "x"
                chessboard += " "
            chessboard += "\n"
        return chessboard

    def init_empty_board(self) -> None:
        """ Init the chessboard without any pieces """
        self.chessboard = [[Tile(Colors.white, None, (i, j)) if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0) else Tile(Colors.black, None, (i, j)) for j in range(8)] for i in range(8)]

    def init_board_with_pieces(self) -> None:
        """ Init the chessboard with basic pieces """
        self.chessboard[0][0].add_new_piece(Rook("rook", Colors.white))
        self.chessboard[1][0].add_new_piece(Knight("knight", Colors.white))
        self.chessboard[2][0].add_new_piece(Bishop("bishop", Colors.white))
        self.chessboard[3][0].add_new_piece(Queen("queen", Colors.white))
        self.chessboard[4][0].add_new_piece(King("king", Colors.white))
        self.chessboard[5][0].add_new_piece(Bishop("bishop", Colors.white))
        self.chessboard[6][0].add_new_piece(Knight("knight", Colors.white))
        self.chessboard[7][0].add_new_piece(Rook("rook", Colors.white))

        self.chessboard[0][7].add_new_piece(Rook("rook", Colors.black))
        self.chessboard[1][7].add_new_piece(Knight("knight", Colors.black))
        self.chessboard[2][7].add_new_piece(Bishop("bishop", Colors.black))
        self.chessboard[3][7].add_new_piece(Queen("queen", Colors.black))
        self.chessboard[4][7].add_new_piece(King("king", Colors.black))
        self.chessboard[5][7].add_new_piece(Bishop("bishop", Colors.black))
        self.chessboard[6][7].add_new_piece(Knight("knight", Colors.black))
        self.chessboard[7][7].add_new_piece(Rook("rook", Colors.black))

        for i in range(8):
            self.chessboard[i][1].add_new_piece(Pawn("pawn", Colors.white))
            self.chessboard[i][6].add_new_piece(Pawn("pawn", Colors.black))

    def duplicate(self) -> "Board":
        new_board = Board()
        new_board.past_moves = copy.deepcopy(self.past_moves)
        new_board.chessboard = [[tile.duplicate() for tile in row] for row in self.chessboard]
        return new_board

    def get_pieces(self) -> list[Piece]:
        """ Return a list of every pieces """
        pieces = []
        for x in range(len(self.chessboard)):
            for y in range(len(self.chessboard)):
                if not self.chessboard[x][y].is_empty():
                    pieces.append(self.chessboard[x][y].piece)
        return pieces

    def get_piece_at(self, coords: Vector) -> Piece | None:
        """ Return the piece at coords """
        return self.chessboard[coords.x][coords.y].piece

    def get_piece(self, name: str, color: Colors) -> Piece | None:
        for piece in self.get_color_pieces(color):
            if piece.name == name:
                return piece
        return None

    def get_color_pieces(self, color) -> list[Piece]:
        """ Return a list of every color pieces """
        pieces = []
        for x in range(len(self.chessboard)):
            for y in range(len(self.chessboard)):
                if not self.chessboard[x][y].is_empty() and self.chessboard[x][y].piece.get_color() == color:
                    pieces.append(self.chessboard[x][y].piece)
        return pieces


    def get_moves(self) -> list[tuple[Vector, Vector]]:
        moves = []

        for piece in self.get_pieces():
            moves += piece.get_legal_moves(self)
        return moves

    def get_color_legal_moves(self, color: Colors) -> list[tuple[Vector, Vector]]:
        """ Return a list of possible color move """
        moves = []

        for piece in self.get_color_pieces(color):
            moves += piece.get_legal_moves(self)
        return moves

    def get_color_attack_moves(self, color: Colors) -> list[tuple[Vector, Vector]]:
        """ Return a list of possible color move """
        moves = []

        for piece in self.get_color_pieces(color):
            moves += piece.get_attack_moves(self)
        return moves

    def get_color_controlled_tiles(self, color: Colors) -> list[tuple[Vector, Vector]]:
        """ Return a list of possible color move """
        moves = []

        for piece in self.get_color_pieces(color):
            moves += piece.get_controlled_tiles(self)
        return moves

    def is_game_over(self) -> bool:
        """ Return True if the game is over (stalemate, checkmate, insufficient material)"""
        return (self.is_stalemate(Colors.white) or self.is_checkmate(Colors.white) or self.is_insufficient_material(Colors.white)) \
            or (self.is_stalemate(Colors.black) or self.is_checkmate(Colors.black) or self.is_insufficient_material(Colors.black))

    def is_stalemate(self, color: Colors) -> bool:
        """ Return True if color are stalemate """
        return len(self.get_color_legal_moves(color)) == 0

    def is_checkmate(self, color: Colors) -> bool:
        return self.is_check(color) and self.is_stalemate(color)

    def is_insufficient_material(self, color: Colors) -> bool:
        """ Return True if there is an insufficience of material """
        return False

    def is_check(self, color: Colors) -> bool:
        """ Return True if color is in check"""

        king = self.get_piece("king", color)
        if not king:
            return False

        if color == Colors.white:
            moves = self.get_color_attack_moves(Colors.black)
        else:
            moves = self.get_color_attack_moves(Colors.white)

        for (source, target) in moves:
            if target == king.get_position():
                return True
        return False

    def is_piece_at(self, target: Vector) -> bool:
        """ Return True if a piece is at coords """
        return not self.chessboard[target.x][target.y].is_empty()

    def is_enemy_at(self, source: Vector, target: Vector) -> bool:
        """ Return True if an opposite piece is at coords """
        if not self.is_piece_at(target):
            return False
        return self.get_piece_at(source).get_color() != self.get_piece_at(target).get_color()

    def is_ally_at(self, source: Vector, target: Vector):
        """ Return True if an ally piece is at coords """
        if not self.is_piece_at(target):
            return False
        return self.get_piece_at(source).get_color() == self.get_piece_at(target).get_color()

    def is_move_in_board(self, target: Vector) -> bool:
        """ Return True if the move is in the board """
        return target.x >= 0 and target.x <= 7 and target.y >= 0 and target.y <= 7

    def is_move_valid(self, source: Vector, target: Vector) -> bool:
        return self.is_move_in_board(target) and not self.is_ally_at(source, target)

    def is_move_legal(self, source: Vector, target: Vector) -> bool:
        if not self.is_move_valid(source, target):
            return False
        color = self.chessboard[source.x][source.y].piece.color
        self.move(source, target)
        if self.is_check(color):
            self.unmake_move()
            return False
        self.unmake_move()
        return True

    def make_move(self, source: Vector, dest: Vector) -> bool:
        if self.is_move_legal(source, dest):
            self.move(source, dest)
            return True
        return False

    def move(self, source: Vector, target: Vector) -> None:
        self.past_moves.append({"source": source, "target": target, "target_piece": self.chessboard[target.x][target.y].piece})
        self.swap_tiles(source, target)

    def unmake_move(self) -> None:
        previous_state = self.past_moves.pop()
        self.swap_tiles(previous_state["target"], previous_state["source"], previous_state["target_piece"])

    def swap_tiles(self, source: Vector, target: Vector, piece = None) -> None:
        source_tile = self.chessboard[source.x][source.y]
        target_tile = self.chessboard[target.x][target.y]

        source_to_target_tile = Tile(target_tile.color, None, (target.x, target.y))
        if source_tile.piece:
            source_to_target_tile.piece = type(source_tile.piece)(source_tile.piece.name, source_tile.piece.color, target.x, target.y)

        target_to_source_tile = Tile(source_tile.color, None, (source.x, source.y))
        if piece:
            target_to_source_tile.piece = type(piece)(piece.name, piece.color, source.x, source.y)

        self.chessboard[source.x][source.y] = target_to_source_tile
        self.chessboard[target.x][target.y] = source_to_target_tile

    ##################


    def display(self) -> None:
        """ Display the board with annotations"""
        _VERTICAL_SEPARATOR_ = "|"
        _HORIZONTAL_SEPARATOR_ = "-"

        self.display_row_annotation()
        self.display_row_separators(_HORIZONTAL_SEPARATOR_)
        for i in range(len(self.chessboard)):
            self.display_col_annotation(i)
            self.display_col_separators(_VERTICAL_SEPARATOR_)
            for j in range(len(self.chessboard)):
                self.chessboard[i][j].display_tile()
                # print(f"({i},{j})", end="")
                # print(self.chessboard[i][j].coords, end="")
            self.display_col_separators(_VERTICAL_SEPARATOR_)
            self.display_col_annotation(i)
            print("")
        self.display_row_separators(_HORIZONTAL_SEPARATOR_)
        self.display_row_annotation()

    def display_row_annotation(self) -> None:
        """ Display row letters annotations """
        print("    ", end="")
        for char in COL_ANNOTATIONS:
            print(f"{char} ", end="")
        print("")

    def display_row_separators(self, _HORIZONTAL_SEPARATOR_) -> None:
        """ Display row separators """
        print(f"    {f"{_HORIZONTAL_SEPARATOR_} " * len(ROW_ANNOTATIONS)}")

    def display_col_annotation(self, idx) -> None:
        """ Display column numbers annotations """
        print(f"{ROW_ANNOTATIONS[idx]}", end="")

    def display_col_separators(self, _VERTICAL_SEPARATOR_) -> None:
        """ Display col separators """
        print(f" {_VERTICAL_SEPARATOR_} ", end="")
