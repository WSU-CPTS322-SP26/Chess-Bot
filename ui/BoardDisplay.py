import pygame

# Constants
squareSize = 150
boardSize = 8
color1 = (235, 235, 208)
color2 = (119, 149, 86) 

# Initialize Pygame
pygame.init()
info = pygame.display.Info()  
screen = pygame.display.set_mode((info.current_w, info.current_h))
pygame.display.set_caption("Simple Chess Board")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw board
    for row in range(boardSize):
        for col in range(boardSize):
            color = color1 if (row + col) % 2 == 0 else color2
            pygame.draw.rect(screen, color, (col*squareSize, row*squareSize, squareSize, squareSize))

    pygame.display.flip()

pygame.quit()