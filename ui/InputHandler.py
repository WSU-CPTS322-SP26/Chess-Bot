import pygame
import chess

# helps handle UI actions -> core pineline
class InputHandler:

    def __init__(self, board_display): # passes in board UI
        self.board_display = board_display

    def process_event(self, event: pygame.event.Event, controller):

        if event.type == pygame.QUIT:
            return "QUIT"
        
        # Check if the game has ended
        controller.check_game_end()
            
        # Mouse left click -> square
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            square = self.board_display.pixel_to_square(event.pos)
            rank = self.board_display.pixel_to_square(event.pos)
            if square is not None:
                controller.handle_square_click(square)
            return None

        # check for panel button events
        
        return None