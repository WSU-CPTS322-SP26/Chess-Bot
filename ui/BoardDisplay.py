import pygame
import chess

class BoardDisplay:
    def __init__(self, screen: pygame.Surface, game_state):

        self.game_state = game_state

        # Constants
        self.squareSize = 90
        self.boardSize = 8
        self.color1 = (235, 235, 208)
        self.color2 = (119, 149, 86)

        self.screen = screen # passed in by main

        # Board dimensions
        board_px = self.squareSize * self.boardSize

        # Resize window to fit board exactly
        # self.screen = pygame.display.set_mode((board_px, board_px))

        # add all pieces to board rendering
        self.pieces = {}

        piece_files = {
            "white": {
                "pawn":   "Chess_plt45.png",
                "rook":   "Chess_rlt45.png",
                "knight": "Chess_nlt45.png",
                "bishop": "Chess_blt45.png",
                "queen":  "Chess_qlt45.png",
                "king":   "Chess_klt45.png",
            },
            "black": {
                "pawn":   "Chess_pdt45.png",
                "rook":   "Chess_rdt45.png",
                "knight": "Chess_ndt45.png",
                "bishop": "Chess_bdt45.png",
                "queen":  "Chess_qdt45.png",
                "king":   "Chess_kdt45.png",
            }
        }

        for color in ["white", "black"]:
            for name, filename in piece_files[color].items():
                img = pygame.image.load(
                    f"assets/pieces/{color}/{filename}"
                ).convert_alpha()

                self.pieces[(color, name)] = pygame.transform.smoothscale(
                    img, (self.squareSize, self.squareSize)
                )


    def draw(self): # now have it render pieces from game_state.board
        for row in range(self.boardSize):
            for col in range(self.boardSize):
                color = self.color1 if (row + col) % 2 == 0 else self.color2
                pygame.draw.rect(
                    self.screen,
                    color,
                    (
                        col * self.squareSize,
                        row * self.squareSize,
                        self.squareSize,
                        self.squareSize
                    )
                )

        board = self.game_state.board

        piece_map = {
            chess.PAWN: "pawn",
            chess.ROOK: "rook",
            chess.KNIGHT: "knight",
            chess.BISHOP: "bishop",
            chess.QUEEN: "queen",
            chess.KING: "king",
        }

        for square in chess.SQUARES:
            piece = board.piece_at(square)
            if piece is None:
                continue

            col = chess.square_file(square)
            row = 7 - chess.square_rank(square)  # flip rank for pygame

            color = "white" if piece.color == chess.WHITE else "black"
            name = piece_map[piece.piece_type]

            img = self.pieces[(color, name)]
            self.screen.blit(img, (col * self.squareSize, row * self.squareSize))