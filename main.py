import pygame

print("John Uno says Hello!")

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("John Uno")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("dodgerblue")

    pygame.display.flip()

# Quit Pygame
pygame.quit()
