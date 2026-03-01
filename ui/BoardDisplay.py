import pygame
import chess

class BoardDisplay:
    def __init__(self, screen: pygame.Surface):
        # Constants
        self.squareSize = 150
        self.boardSize = 8
        self.color1 = (235, 235, 208)
        self.color2 = (119, 149, 86)

        self.screen = screen # passed in by main

        # Fit board to open window
        w, h = self.screen.get_size()
        self.squareSize = min(w, h) // self.boardSize

        # Center board
        self.x_offset = (w - self.squareSize * self.boardSize) // 2
        self.y_offset = (h - self.squareSize * self.boardSize) // 2

    def draw(self):
        for row in range(self.boardSize):
            for col in range(self.boardSize):
                color = self.color1 if (row + col) % 2 == 0 else self.color2
                pygame.draw.rect(
                    self.screen,
                    color,
                    (
                        self.x_offset + col * self.squareSize,
                        self.y_offset + row * self.squareSize,
                        self.squareSize,
                        self.squareSize
                    )
                )