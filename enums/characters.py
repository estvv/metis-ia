from enum import Enum
from enums.colors import Colors

class BlackCharacters(Enum):
    king = "♔"
    queen = "♕"
    rook = "♖"
    knight = "♘"
    bishop = "♗"
    pawn = "♙"
    empty = "□"

class WhiteCharacters(Enum):
    king = "♚"
    queen = "♛"
    rook = "♜"
    knight = "♞"
    bishop = "♝"
    pawn = "♟"
    empty = "■"

__get_characters__ = {("king", Colors.white.value): WhiteCharacters.king.value,
                      ("queen", Colors.white.value): WhiteCharacters.queen.value,
                      ("rook", Colors.white.value): WhiteCharacters.rook.value,
                      ("knight", Colors.white.value): WhiteCharacters.knight.value,
                      ("bishop", Colors.white.value): WhiteCharacters.bishop.value,
                      ("pawn", Colors.white.value): WhiteCharacters.pawn.value,
                      ("king", Colors.black.value): BlackCharacters.king.value,
                      ("queen", Colors.black.value): BlackCharacters.queen.value,
                      ("rook", Colors.black.value): BlackCharacters.rook.value,
                      ("knight", Colors.black.value): BlackCharacters.knight.value,
                      ("bishop", Colors.black.value): BlackCharacters.bishop.value,
                      ("pawn", Colors.black.value): BlackCharacters.pawn.value
                      }
