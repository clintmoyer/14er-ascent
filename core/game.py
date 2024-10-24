import pygame
from core.player import Player
from core.settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Initialize player
    player = Player()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update game objects
        player.update()

        # Render game objects
        screen.fill((135, 206, 250))  # Sky blue background
        player.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    run_game()

