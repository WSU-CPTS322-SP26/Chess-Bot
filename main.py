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
    PANEL_WIDTH = 500
    screen = pygame.display.set_mode((BOARD_SIZE_PX + PANEL_WIDTH, BOARD_SIZE_PX))
    pygame.display.set_caption("Chess Bot - CPT_S 322")

    clock = pygame.time.Clock()
    menu = MainMenu(screen)

    game_state = GameState()
    board_ui = BoardDisplay(screen, game_state)
    controller = None # will create later based on game selection
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

                #if user selects to begin game
                if action in ("PVP", "PVBS", "PVBH"):
                    game_state.reset()

                    #create the specific GameController type based on selection
                    if action == "PVP":
                        controller = GameController(game_state, mode="PVP")
                    elif action == "PVBS":
                        controller = GameController(game_state, mode="PVBS")
                    elif action == "PVBH":
                        controller = GameController(game_state, mode="PVBH")

                    mode = "GAME"

                elif action == "QUIT":
                    running = False
            
            elif mode == "GAME":
                # Sending actual clicks to controller logic
                result = input_handler.process_event(event, controller)

                # check in-game buttons
                ingameAction = board_ui.handle_event(event)

                # user wants to save game as pgn
                if ingameAction == "SAVE":
                    controller.save_game()

                # user wants to load game as pgn
                if ingameAction == "LOAD":
                    game_state.board = controller.load_game()
                    
                # user wants to return to menu
                if ingameAction == "MENU":
                    
                    mode = "MENU"
                    # reset board for next game
                    game_state.reset()
                    break
                
                
               


        if mode == "MENU":
            menu.draw()
        elif mode == "GAME":
            if controller:
                controller.make_bot_move()
                controller.check_game_end()

            screen.fill((0,0,0))
            board_ui.draw()

        pygame.display.flip()
        clock.tick(60) 

    pygame.quit()

if __name__ == "__main__":
    main()