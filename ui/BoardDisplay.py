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

    def draw(self):
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