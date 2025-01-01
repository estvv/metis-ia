from objects.piece import Piece
from enums.colors import Colors
from utils.vector import Vector
from enums.characters import WhiteCharacters, BlackCharacters

class Tile:
    color: Colors
    piece: Piece | None
    coords: Vector

    def __init__(self, __color__: Colors, __piece__: Piece, __coordinates__: tuple) -> None:
        self.color = __color__
        self.piece = __piece__
        self.coords = Vector(__coordinates__)

    def __str__(self):
        if self.piece:
            return f"{self.piece.color} {self.piece.name} at {self.coords}"
        return f"tile empty at {self.coords}"

    def duplicate(self) -> "Tile":

        new_tile = Tile(self.color, None, self.coords)
        if self.piece:
            new_tile.piece = Piece(self.piece.name, self.piece.color, self.piece.coords.x, self.piece.coords.y)
        return new_tile

    def display_tile(self) -> None:
        """ Display the Tile """
        if not self.is_empty():
            print(self.piece, end="")
        else:
            self.display_empty_tile()

    def display_empty_tile(self) -> None:
        """ Display en empty character """
        if self.is_tile_white():
            print(f"{WhiteCharacters.empty.value} ", end="")
        else:
            print(f"{BlackCharacters.empty.value} ", end="")

    def get_coords(self) -> Vector:
        """ Return the Tile coordinates """
        return self.coords

    def get_color(self) -> Colors:
        """ Return Tile color """
        return self.color

    def get_color_name(self) -> str:
        """ Return Tile color name """
        return self.color.name

    def get_color_value(self) -> str:
        """ Return Tile color value"""
        return self.color.value

    def is_empty(self) -> bool:
        """ Return True if the tile is empty """
        return self.piece == None

    def is_tile_white(self) -> bool:
        """ Return True if the tile is white """
        return self.color.value == Colors.white.value

    def is_tile_black(self) -> bool:
        """ Return True if the tile is black """
        return self.color.value == Colors.black.value

    def is_piece_white(self) -> bool:
        """ Return True if the tile contains a white piece """
        return self.piece and self.piece.is_white()

    def is_piece_black(self) -> bool:
        """ Return True if the tile contains a black piece """
        return self.piece and self.piece.is_black()

    def add_new_piece(self, piece: Piece) -> None:
        self.piece = piece
        self.piece.coords = self.get_coords()

    def update_tile_piece(self, piece: Piece) -> None:
        """ Forgot the previous piece and update the piece with a given one """
        self.piece = piece
        self.piece.coords = Vector(self.coords.x, self.coords.y)
