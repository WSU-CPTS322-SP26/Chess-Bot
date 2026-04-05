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

        # panel
        self.panel_x = self.squareSize * self.boardSize
        self.panel_width = 500
        self.panel_color = (40, 40, 40)

        # Fonts
        self.font = pygame.font.SysFont("Arial", 24)
        self.button_font = pygame.font.SysFont(None, 32) 

        # button constants
        w, h = self.screen.get_size()
        bw, bh = 240, 35
        start_y = (h / 8) * 7
        start_x = (self.panel_x / 2) +  self.panel_x
        spacing = 50

        # buttons
        self.buttons = [
            ("Save Game", pygame.Rect(0,0, bw, bh)),
            ("Return to Menu", pygame.Rect(0, 0, bw, bh)),
        ]


        # button placement
        for i, (_, rect) in enumerate(self.buttons):
            rect.center = (start_x, start_y + i * spacing)

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
        
        pygame.draw.rect(
            self.screen, self.panel_color, 
            (self.panel_x, 0, self.panel_width, self.squareSize * self.boardSize)
        )
        
        turn = "White's" if self.game_state.board.turn else "Black's"
        text = f"{turn} turn"
        text_surface = self.font.render(text, True, (255, 255, 255))
        self.screen.blit(text_surface, (self.panel_x + 20, 20))
        
        MAX_MESSAGES = 1
        y_offset = 60
        messages_to_draw = self.game_state.messages[-MAX_MESSAGES:]
        for msg in messages_to_draw:
            text_surface = self.font.render(msg, True, (255, 255, 255))
            self.screen.blit(text_surface, (self.panel_x + 20, y_offset))
            y_offset = y_offset + 30

        # buttons drawing
        for label, rect in self.buttons:
            pygame.draw.rect(self.screen, (80,80,80), rect)
            text = self.button_font.render(label, True, (255, 255, 255))
            self.screen.blit(text, text.get_rect(center=rect.center))
    def pixel_to_square(self, pos):
        x, y = pos
        column = x // self.squareSize
        row = y // self.squareSize

        # Check if the click is actually on the 8x8 board
        if 0 <= column < 8 and 0 <= row < 8:
            # Pygame (0,0) is TOP-LEFT. 
            # Chess Rank 0 is BOTTOM. We have to flip the row.
            rank = 7 - row 
            file = column
            return chess.square(file, rank)
        return None