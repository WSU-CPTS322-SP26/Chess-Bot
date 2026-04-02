import pygame
import chess

class MainMenu:
    def __init__(self, screen: pygame.Surface): # pass rendered screen into class
        self.screen = screen

        # Font
        self.title_font = pygame.font.SysFont(None, 72)
        self.button_font = pygame.font.SysFont(None, 44)

        # Layout
        w, h = self.screen.get_size()
        bw, bh = 360, 70
        cx = w // 2

        self.buttons = [
            ("User vs User", pygame.Rect(0, 0, bw, bh)),
            ("User vs Bot - Stockfish",  pygame.Rect(0, 0, bw, bh)),
            ("User vs Bot - Homemade", pygame.Rect(0, 0, bw, bh)),
            ("Quit",         pygame.Rect(0, 0, bw, bh)),
        ]

        # button placement
        start_y = h // 2 - 80
        spacing = 95
        for i, (_, rect) in enumerate(self.buttons):
            rect.center = (cx, start_y + i * spacing)

    def handle_event(self, event):
        if event.type == pygame.QUIT: # Window close button
            return "QUIT"
            
        # handle user button clicks
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for label, rect in self.buttons:
                if rect.collidepoint(event.pos):
                    if label == "User vs User":
                        return "PVP"
                    if label == "User vs Bot":
                        return "PVB"
                    if label == "Quit":
                        return "QUIT"
        return None

    def draw(self):
        self.screen.fill((30,30,30))

        # Title
        title_text = self.title_font.render("Chess Bot", True, (255,255,255))
        title_rect = title_text.get_rect(
            center=(self.screen.get_width() // 2, 120)
        )
        self.screen.blit(title_text, title_rect)

        # Buttons
        for label, rect in self.buttons:
            pygame.draw.rect(self.screen, (80, 80, 80), rect)
            text = self.button_font.render(label, True, (255, 255, 255))
            self.screen.blit(text, text.get_rect(center=rect.center))