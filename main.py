import pygame

def main():
    pygame.init()

    WIDTH, HEIGHT = 800, 600 # window dimensions
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Chess Bot - CPT_S 322")

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((30,30,30))

        pygame.draw.rect( # rectangle for game element
            screen,
            (200, 200, 200),
            pygame.Rect(300, 250, 200, 80),
            border_radius=12
        )

        pygame.display.flip()
        clock.tick(60)

    pygame.quit
        

if __name__ == "__main__":
    main()