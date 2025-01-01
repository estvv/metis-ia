from game.game import Game
from enums.colors import Colors
from objects.pieces.bishop import Bishop
from objects.pieces.knight import Knight
from objects.pieces.queen import Queen
from objects.pieces.rook import Rook
from objects.pieces.king import King
from objects.pieces.pawn import Pawn
from utils.vector import Vector
from bot.ai import AI

def move():
    game = Game()
    game.board.init_empty_board()

    game.board.chessboard[0][0].update_tile_piece(King("king", Colors.white))
    game.board.chessboard[7][7].update_tile_piece(King("king", Colors.black))
    game.board.chessboard[6][5].update_tile_piece(Queen("queen", Colors.black))

    print("--------- Basic move --------")
    game.board.display()
    print("Move Queen")
    game.board.make_move(Vector(6, 5), Vector(3, 5))
    game.board.display()
    print("Unmove")
    game.board.unmake_move()
    game.board.display()
    print("-----------------------------")

def move_on_a_piece():
    game = Game()
    game.board.init_empty_board()

    game.board.chessboard[0][0].update_tile_piece(King("king", Colors.white))
    game.board.chessboard[6][5].update_tile_piece(Queen("queen", Colors.white))
    game.board.chessboard[7][7].update_tile_piece(King("king", Colors.black))
    game.board.chessboard[3][5].update_tile_piece(Pawn("pawn", Colors.black))

    print("--------- Move on a piece --------")
    game.board.display()
    print("Move Queen")
    game.board.make_move(Vector(6, 5), Vector(3, 5))
    game.board.display()
    print("Unmove")
    game.board.unmake_move()
    game.board.display()
    print("----------------------------------")

def multiple_moves():
    game = Game()
    game.board.init_empty_board()

    game.board.chessboard[0][0].update_tile_piece(King("king", Colors.white))
    game.board.chessboard[6][5].update_tile_piece(Queen("queen", Colors.white))
    game.board.chessboard[7][7].update_tile_piece(King("king", Colors.black))
    game.board.chessboard[3][5].update_tile_piece(Pawn("pawn", Colors.black))

    print("--------- Move on a piece --------")
    game.board.display()
    print("Move Queen")
    game.board.make_move(Vector(6, 5), Vector(3, 5))
    game.board.display()
    print("Move Queen")
    game.board.make_move(Vector(3, 5), Vector(3, 0))
    game.board.display()
    print("Unmove")
    game.board.unmake_move()
    game.board.display()
    print("Unmove")
    game.board.unmake_move()
    game.board.display()
    print("----------------------------------")

def checkmate():
    game = Game()
    game.board.init_empty_board()

    game.board.chessboard[0][3].update_tile_piece(Rook("rook", Colors.black))
    game.board.chessboard[2][1].update_tile_piece(Queen("queen", Colors.black))
    game.board.chessboard[0][1].update_tile_piece(King("king", Colors.white))

    print("--------- Checkmate --------")
    print(f"Check :  {game.board.is_check(Colors.white)}")
    print(f"Stalemate : {game.board.is_stalemate(Colors.white)}")
    print(f"Checkmate : {game.board.is_checkmate(Colors.white)}")
    print(f"Game over : {game.board.is_game_over()}")
    # game.board.display()
    print("----------------------------")

def simple_check():
    game = Game()
    game.board.init_empty_board()

    game.board.chessboard[1][3].update_tile_piece(Rook("rook", Colors.black))
    game.board.chessboard[2][1].update_tile_piece(Queen("queen", Colors.black))
    game.board.chessboard[0][1].update_tile_piece(King("king", Colors.white))

    print("--------- Simple Check --------")
    print(f"Check :  {game.board.is_check(Colors.white)}")
    print(f"Stalemate : {game.board.is_stalemate(Colors.white)}")
    print(f"Checkmate : {game.board.is_checkmate(Colors.white)}")
    print(f"Game over : {game.board.is_game_over()}")
    # game.board.display()
    print("-------------------------------")

def stalemate():
    game = Game()
    game.board.init_empty_board()

    game.board.chessboard[1][3].update_tile_piece(Rook("rook", Colors.black))
    game.board.chessboard[2][1].update_tile_piece(Queen("queen", Colors.black))
    game.board.chessboard[0][0].update_tile_piece(King("king", Colors.white))

    print("--------- Stalemate --------")
    print(f"Check :  {game.board.is_check(Colors.white)}")
    print(f"Stalemate : {game.board.is_stalemate(Colors.white)}")
    print(f"Checkmate : {game.board.is_checkmate(Colors.white)}")
    print(f"Game over : {game.board.is_game_over()}")
    # game.board.display()
    print("-------------------------------")

def AI_rook_capture_queen():
    game = Game()
    game.board.init_empty_board()

    game.board.chessboard[7][7].update_tile_piece(King("king", Colors.black))
    game.board.chessboard[1][3].update_tile_piece(Rook("rook", Colors.black))
    game.board.chessboard[1][5].update_tile_piece(Pawn("pawn", Colors.black))
    game.board.chessboard[0][0].update_tile_piece(King("king", Colors.white))
    game.board.chessboard[1][4].update_tile_piece(Queen("queen", Colors.white))
    game.board.chessboard[1][2].update_tile_piece(Pawn("pawn", Colors.white))

    print("--------- Capture a better piece --------")
    game.board.display()
    game.p2 = AI()
    game.p1 = AI()
    game.p1.update_color(Colors.white)
    game.p2.update_color(Colors.black)
    move = game.p2.get_best_move(game.board)
    print(f"White best moove choosen : {move}")
    game.board.make_move(move[0], move[1])
    game.board.display()
    game.board.unmake_move()
    move = game.p1.get_best_move(game.board)
    print(f"Black best moove choosen : {move}")
    game.board.make_move(move[0], move[1])
    game.board.display()
    print("-----------------------------------------")

def AI_bishop_capture_rook():
    game = Game()
    game.board.init_empty_board()

    game.board.chessboard[7][7].update_tile_piece(King("king", Colors.black))
    game.board.chessboard[0][4].update_tile_piece(Bishop("bishop", Colors.black))
    game.board.chessboard[1][5].update_tile_piece(Pawn("pawn", Colors.white))
    game.board.chessboard[0][1].update_tile_piece(King("king", Colors.white))
    game.board.chessboard[2][2].update_tile_piece(Rook("rook", Colors.white))

    print("--------- Capture a better piece --------")
    game.board.display()
    game.p2 = AI()
    game.p1.update_color(Colors.white)
    game.p2.update_color(Colors.black)
    move = game.p2.get_best_move(game.board)
    print(f"White Moove choosen : {move}")
    game.board.make_move(move[0], move[1])
    game.board.display()
    print("-----------------------------------------")

def AI_not_capture_lower_piece():
    game = Game()
    game.board.init_empty_board()

    game.board.chessboard[7][7].update_tile_piece(King("king", Colors.black))
    game.board.chessboard[1][3].update_tile_piece(Rook("rook", Colors.black))
    game.board.chessboard[0][0].update_tile_piece(King("king", Colors.white))
    game.board.chessboard[1][4].update_tile_piece(Pawn("pawn", Colors.white))
    game.board.chessboard[1][5].update_tile_piece(Queen("queen", Colors.white))

    print("--------- Not Capture a better piece --------")
    game.board.display()
    game.p1 = AI()
    game.p2 = AI()
    game.p1.update_color(Colors.white)
    game.p2.update_color(Colors.black)
    move = game.p2.get_best_move(game.board)
    print(f"Moove choosen : {move}")
    game.board.make_move(move[0], move[1])
    game.board.display()
    game.board.unmake_move()
    move = game.p1.get_best_move(game.board)
    print(f"Black Moove choosen : {move}")
    game.board.make_move(move[0], move[1])
    game.board.display()
    print("-----------------------------------------")

def AI_capture_lower_piece():
    game = Game()
    game.board.init_empty_board()

    game.board.chessboard[7][7].update_tile_piece(King("king", Colors.black))
    game.board.chessboard[1][3].update_tile_piece(Rook("rook", Colors.black))
    game.board.chessboard[0][0].update_tile_piece(King("king", Colors.white))
    game.board.chessboard[1][4].update_tile_piece(Pawn("pawn", Colors.white))

    print("--------- Capture a better piece --------")
    game.board.display()
    game.p1 = AI()
    game.p2 = AI()
    game.p1.update_color(Colors.white)
    game.p2.update_color(Colors.black)
    move = game.p2.get_best_move(game.board)
    print(f"Moove choosen : {move}")
    game.board.make_move(move[0], move[1])
    game.board.display()
    game.board.unmake_move()
    move = game.p1.get_best_move(game.board)
    print(f"Black Moove choosen : {move}")
    game.board.make_move(move[0], move[1])
    game.board.display()
    print("-----------------------------------------")

def main():
    return

if __name__ == "__main__":
    # move()
    # move_on_a_piece()
    # multiple_moves()
    # checkmate()
    # simple_check()
    # stalemate()
    # AI_rook_capture_queen()
    # AI_bishop_capture_rook()
    # AI_not_capture_lower_piece()
    # AI_capture_lower_piece()
    main()
