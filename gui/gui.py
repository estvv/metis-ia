import pygame, threading
from bot.ai import AI
from game.game import Game
from objects.tile import Tile
from enums.colors import Colors
from game.player import Player
from objects.pieces.king import King
from utils.vector import Vector

WINDOW_SIZE = 600
SQUARE_SIZE = WINDOW_SIZE // 8

class Gui(Game):
    def __init__(self) -> None:
        super().__init__()
        pygame.init()
        self.window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
        pygame.display.set_caption("Chess")

        self.turn = Colors.white
        self.selected_tile: Tile = None

    def select_player_color(self):
        font = pygame.font.Font(None, 40)
        text_white = font.render("Jouer Blanc", True, (0, 0, 0))
        text_black = font.render("Jouer Noir", True, (255, 255, 255))

        button_width, button_height = 200, 60
        white_button_rect = pygame.Rect((WINDOW_SIZE // 2 - button_width // 2, WINDOW_SIZE // 3), (button_width, button_height))
        black_button_rect = pygame.Rect((WINDOW_SIZE // 2 - button_width // 2, 2 * WINDOW_SIZE // 3), (button_width, button_height))
        clock = pygame.time.Clock()

        while 1:
            clock.tick(60)

            self.window.fill((0, 0, 0))

            mouse_pos = pygame.mouse.get_pos()

            white_hover = white_button_rect.collidepoint(mouse_pos)
            black_hover = black_button_rect.collidepoint(mouse_pos)

            pygame.draw.rect(self.window, (200, 200, 200) if white_hover else (255, 255, 255), white_button_rect)
            pygame.draw.rect(self.window, (0, 0, 0), white_button_rect, 3)
            self.window.blit(text_white, text_white.get_rect(center=white_button_rect.center))

            pygame.draw.rect(self.window, (100, 100, 100) if black_hover else (0, 0, 0), black_button_rect)
            pygame.draw.rect(self.window, (255, 255, 255), black_button_rect, 3)
            self.window.blit(text_black, text_black.get_rect(center=black_button_rect.center))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if white_button_rect.collidepoint(mouse_pos):
                        self.p1.update_color(Colors.white)
                        self.p2.update_color(Colors.black)
                        self.p_turn = self.p1
                        return
                    elif black_button_rect.collidepoint(mouse_pos):
                        self.p1.update_color(Colors.black)
                        self.p2.update_color(Colors.white)
                        self.p_turn = self.p2
                        return

    def load_piece_images(self):
        pieces = ["king", "queen", "rook", "bishop", "knight", "pawn"]
        colors = ["white", "black"]
        images = {}
        for color in colors:
            for piece in pieces:
                images[f"{color}_{piece}"] = pygame.transform.scale(pygame.image.load(f"./assets/{color}/{piece}.svg"), (SQUARE_SIZE, SQUARE_SIZE))
        return images

    def coords_to_gui(self, coords: Vector):
        return (coords.y * SQUARE_SIZE, coords.x * SQUARE_SIZE)

    def gui_to_coords(self, coords: Vector) -> tuple:
        return (coords.x // SQUARE_SIZE, coords.y // SQUARE_SIZE)

    def display_check(self):
        if self.board.is_check(Colors.white):
            king = self.board.get_piece("king", Colors.white)
            surface = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE), pygame.SRCALPHA)
            surface.fill((255, 0, 0, 100))
            self.window.blit(surface, self.coords_to_gui(king.coords))
        if self.board.is_check(Colors.black):
            king = self.board.get_piece("king", Colors.black)
            surface = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE), pygame.SRCALPHA)
            surface.fill((255, 0, 0, 100))
            self.window.blit(surface, self.coords_to_gui(king.coords))

    def display_selected_tile(self):
        if self.selected_tile:
            surface = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE), pygame.SRCALPHA)
            surface.fill((0, 255, 0, 150))
            self.window.blit(surface, self.coords_to_gui(self.selected_tile.coords))

            if not self.selected_tile.is_empty():
                moves = self.selected_tile.piece.get_legal_moves(self.board)
                for (source, target) in moves:
                    coords = self.coords_to_gui(target)

                    surface = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE), pygame.SRCALPHA)
                    if self.selected_tile.piece == Colors.white:
                        surface.fill((0, 255, 0, 100))
                    else:
                        surface.fill((0, 0, 255, 100))
                    self.window.blit(surface, coords)

    def display_chessboard(self):
        pieces_assets = self.load_piece_images()

        for i in range(len(self.board.chessboard)):
            for j in range(len(self.board.chessboard)):
                coords = self.coords_to_gui(Vector(i, j))

                if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
                    color = (181, 136, 99)
                else:
                    color = (240, 217, 181)

                pygame.draw.rect(self.window, color, pygame.Rect(coords[0], coords[1], SQUARE_SIZE, SQUARE_SIZE))
                piece = self.board.get_piece_at(Vector(i, j))

                if piece:
                    image = pieces_assets[f"{piece.color.name}_{piece.name.lower()}"]
                    self.window.blit(image, (coords[0], coords[1]))

    def get_clicked_square(self, mouse_pos):
        x, y = self.gui_to_coords(Vector(mouse_pos))

        if 0 <= y < len(self.board.chessboard) and 0 <= x < len(self.board.chessboard):
            return self.board.chessboard[y][x]
        return None

    def get_infos(self):
        mouse_pos = pygame.mouse.get_pos()
        temp_tile: Tile = self.get_clicked_square(mouse_pos)
        if temp_tile and self.selected_tile and not self.selected_tile.is_empty() and self.selected_tile.piece.color == self.p_turn.color:
            flag = False
            for (source, target) in self.selected_tile.piece.get_legal_moves(self.board):
                if target == temp_tile.coords:
                    move = self.board.make_move(source, target)
                    if not move:
                        break
                    self.selected_tile = None
                    flag = True
                    break
            if not flag:
                self.selected_tile = temp_tile
            else:
                if self.p_turn == self.p1:
                    self.p_turn = self.p2
                else:
                    self.p_turn = self.p1
        else:
            self.selected_tile = temp_tile

    def ia_move(self):
        move = self.p2.get_best_move(self.board)
        if not move:
            print(f"END GAME {self.bot.color} lost !")
            exit()
        self.board.make_move(move[0], move[1])
        self.p_turn = self.p1

    def bot_turn(self, player):
        move = player.get_best_move(self.board)
        if not move:
            exit()
        self.board.make_move(move[0], move[1])
        if player == self.p2:
            self.p_turn = self.p1
        else:
            self.p_turn = self.p2

    def run(self):
        # self.p1 = AI()
        # self.p2 = AI()
        self.select_player_color()

        while 1:
            if self.board.is_game_over():
                pygame.quit()
                break
            if not self.p_turn.is_player() and self.p_turn == self.p2:
                self.ia_move()
            # self.bot_turn(self.p_turn)

            self.display_chessboard()
            self.display_selected_tile()
            self.display_check()

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.get_infos()
