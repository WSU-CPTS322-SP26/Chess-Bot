import pygame
import chess

class MainMenu:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen

        # Font
        self.title_font = pygame.font.SysFont(None, 72)
        self.button_font = pygame.font.SysFont(None, 44)

        