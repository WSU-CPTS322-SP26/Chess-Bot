import pygame
from ui.MainMenu import MainMenu
from ui.BoardDisplay import BoardDisplay

def main():
    pygame.init()

    WIDTH, HEIGHT = 800, 600 # window dimensions
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Chess Bot - CPT_S 322")

    clock = pygame.time.Clock()

    menu = MainMenu(screen)
    board = BoardDisplay(screen)

    mode = "MENU"
    running = True

    while running: # pygame has started
        for event in pygame.event.get(): # get option from main menu
            if mode == "MENU":
                action = menu.handle_event(event) # check for an event
                if action in ("PVP", "PVB"): # user wants to play
                    mode = "GAME"
                elif action == "QUIT":
                    running = False

            if event.type == pygame.QUIT: # Window close button
                running = False

        if mode == "MENU":
            menu.draw()
        elif mode == "GAME":
            screen.fill((0,0,0))
            board.draw()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
        

if __name__ == "__main__":
    main()