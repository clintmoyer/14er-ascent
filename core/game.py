import pygame
from core.player import Player
from core.settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS

def draw_health_bar(screen, player):
    """Draws the player's health bar on the screen."""
    pygame.draw.rect(screen, (255, 0, 0), (10, 10, player.health * 2, 20))  # Red health bar background
    pygame.draw.rect(screen, (0, 0, 0), (10, 10, 200, 20), 2)  # Black border around the health bar

def draw_stamina_bar(screen, player):
    """Draws the player's stamina bar on the screen."""
    pygame.draw.rect(screen, (0, 255, 0), (10, 40, player.stamina * 2, 20))  # Green stamina bar background
    pygame.draw.rect(screen, (0, 0, 0), (10, 40, 200, 20), 2)  # Black border around the stamina bar

def run_game():
    """Main game loop to initialize and run the game."""
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Colorado 14er Platformer")  # Set the window title
    clock = pygame.time.Clock()

    # Initialize player
    player = Player()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update game objects (player and other game logic)
        player.update()

        # Render game objects
        screen.fill((135, 206, 250))  # Sky blue background (to represent the outdoors)
        player.draw(screen)  # Draw the player
        draw_health_bar(screen, player)  # Draw the player's health bar
        draw_stamina_bar(screen, player)  # Draw the player's stamina bar

        # Update the display with everything drawn this frame
        pygame.display.flip()

        # Control the frame rate (FPS)
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    run_game()

