
from enums.colors import Colors
from utils.vector import Vector
from enums.weights import Weights
from enums.characters import __get_characters__

class Piece:
    name: str
    color: Colors
    weight: Weights
    character: str = "?"
    first_letter: str
    first_move: bool
    coords: Vector

    def __init__(self, __name__: str, __color__: Colors, x: int = -1, y: int = -1) -> None:
        self.name = __name__
        self.first_letter = __name__[0]
        self.color = __color__
        self.weight = Weights[__name__]
        self.character = __get_characters__[(__name__, __color__.value)]
        self.coords = Vector(x, y)
        self.first_move = True

    def __str__(self) -> None:
        """ Display the piece character """
        return f"{self.character} "

    def duplicate(self):
        return type(self)(self.name, self.color, self.position)

    def get_name(self) -> str:
        """ Return piece name """
        return self.name

    def get_position(self) -> Vector:
        """ Return piece coords """
        return self.coords

    def get_character(self) -> str:
        """ Return piece character """
        return self.character

    def get_weight(self) -> int:
        """ Return piece weight """
        return self.weight.value

    def get_color(self) -> Colors:
        """ Return piece color """
        return self.color

    def get_color_name(self) -> str:
        """ Return piece color name """
        return self.color.name

    def get_color_value(self) -> int:
        """ Return piece color value """
        return self.color.value

    def is_white(self) -> bool:
        """ Return True if the piece is white """
        return self.color.value == Colors.white.value

    def is_black(self) -> bool:
        """ Return True if the piece is black """
        return self.color.value == Colors.black.value

    def has_moved(self) -> bool:
        """ Return True if piece has already moved """
        return not self.first_move

    def update_first_move(self) -> None:
        """ Update the first move at False """
        self.first_move = False

    def duplicate(self) -> "Piece":
        """ Create a duplicate of the actual piece """
        new_piece = type(self)(self.name, self.color)
        new_piece.first_move = self.first_move
        return new_piece

    def get_legal_moves(self, board) -> list[tuple[Vector, Vector]]:
        return []

    def get_attack_moves(self, board) -> list[tuple[Vector, Vector]]:
        return self.get_legal_moves(board)

    def get_controlled_tiles(self, board) -> list[tuple[Vector, Vector]]:
        return self.get_legal_moves(board)
