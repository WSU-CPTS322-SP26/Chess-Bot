import pygame
import chess

class MainMenu:
    def __init__(self, screen: pygame.Surface): # pass rendered screen into class
        self.screen = screen
        
        # Main menu background from Unsplash
        self.background = pygame.image.load("assets/background/menu.jpg").convert()
        self.background = pygame.transform.scale(self.background, self.screen.get_size())

        # Font from Google Fonts
        self.title_font = pygame.font.Font("assets/fonts/Cinzel-Bold.ttf", 72)
        self.button_font = pygame.font.Font("assets/fonts/Cinzel-Regular.ttf", 36)

        # Layout
        w, h = self.screen.get_size()
        bw, bh = 470, 70
        start_x = 10 

        self.buttons = [
            ("User vs User", pygame.Rect(0, 0, bw, bh)),
            ("User vs Stockfish Bot",  pygame.Rect(0, 0, bw, bh)),
            ("User vs Homemade Bot", pygame.Rect(0, 0, bw, bh)),
            ("Quit",         pygame.Rect(0, 0, bw, bh)),
        ]

        # button placement
        start_y = 130
        spacing = 95
        for i, (_, rect) in enumerate(self.buttons):
            rect.topleft = (start_x, start_y + i * spacing)

    def handle_event(self, event):
        if event.type == pygame.QUIT: # Window close button
            return "QUIT"
            
        # handle user button clicks
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for label, rect in self.buttons:
                if rect.collidepoint(event.pos):
                    if label == "User vs User":
                        return "PVP"
                    if label == "User vs Stockfish Bot":
                        return "PVBS"
                    if label == "User vs Homemade Bot":
                        return "PVBH"
                    if label == "Quit":
                        return "QUIT"
        return None

    def draw(self):
        self.screen.blit(self.background, (0, 0))

        # Tracking for buttons
        mouse_pos = pygame.mouse.get_pos()

        # Title
        title_text = self.title_font.render("Chess Bot", True, (255,255,255))
        title_rect = title_text.get_rect(topleft = (20,20))
        self.screen.blit(title_text, title_rect)

        # Buttons
        for label, rect in self.buttons:

            # Creating see through surfaec
            button_surface = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)

            # To show hovering
            if rect.collidepoint(mouse_pos):
                color = (130, 130, 150, 200)  # lighter + more visible
            else:
                color = (80, 80, 80, 140)     # translucent default

            button_surface.fill(color)

            # Drawing button
            self.screen.blit(button_surface, rect.topleft)

            # Text
            text = self.button_font.render(label, True, (255, 255, 255))
            text_rect = text.get_rect(midleft=(rect.left + 15, rect.centery))
            self.screen.blit(text, text_rect)