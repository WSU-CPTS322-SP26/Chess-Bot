import pygame
import chess
from ui.MainMenu import MainMenu
from ui.BoardDisplay import BoardDisplay
from ui.InputHandler import InputHandler # New
from core.GameState import GameState
from core.GameController import GameController # New

def main():
    pygame.init()

    BOARD_SIZE_PX = 720 
    screen = pygame.display.set_mode((BOARD_SIZE_PX, BOARD_SIZE_PX))
    pygame.display.set_caption("Chess Bot - CPT_S 322")

    clock = pygame.time.Clock()
    menu = MainMenu(screen)

    game_state = GameState()
    board_ui = BoardDisplay(screen, game_state)
    controller = GameController(game_state)
    input_handler = InputHandler(board_ui)

    mode = "MENU"
    running = True

    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

            if mode == "MENU":
                action = menu.handle_event(event)
                if action in ("PVP", "PVB"):
                    mode = "GAME"
                elif action == "QUIT":
                    running = False
            
            elif mode == "GAME":
                # Sending actual clicks to controller logic
                input_handler.process_event(event, controller)

                # return to menu if game is done
                if input_handler.process_event(event, controller) == "MENU":
                    
                    mode = "MENU"
                    
                    # reset board for next game
                    game_state.reset()

                    break

        if mode == "MENU":
            menu.draw()
        elif mode == "GAME":
            screen.fill((0,0,0))
            board_ui.draw() 

        pygame.display.flip()
        clock.tick(60) 

    pygame.quit()

if __name__ == "__main__":
    main()