import pygame
import random
from core.player import Player
from core.settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS

# Define terrain types
FLAT = pygame.Rect(0, 550, 800, 50)  # Flat ground
STEEP = pygame.Rect(300, 450, 200, 100)  # Steep slope

def draw_health_bar(screen, player):
    pygame.draw.rect(screen, (255, 0, 0), (10, 10, player.health * 2, 20))  # Red health bar
    pygame.draw.rect(screen, (0, 0, 0), (10, 10, 200, 20), 2)  # Black border

def draw_stamina_bar(screen, player):
    pygame.draw.rect(screen, (0, 255, 0), (10, 40, player.stamina * 2, 20))  # Green stamina bar
    pygame.draw.rect(screen, (0, 0, 0), (10, 40, 200, 20), 2)  # Black border

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Colorado 14er Platformer")
    clock = pygame.time.Clock()

    # Initialize player
    player = Player()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Simulate wind and sliding conditions
        player.apply_wind(active=random.choice([True, False]))  # Random wind for now

        # Check if player is on steep terrain
        if player.rect.colliderect(STEEP):
            player.apply_sliding(True)  # Slide if on a steep slope
        else:
            player.apply_sliding(False)

        # Check if player should be in climbing mode
        if player.rect.colliderect(STEEP):
            player.on_steep_slope = True
        else:
            player.on_steep_slope = False

        if not player.alive:
            player.respawn()

        # Update game objects
        player.update()

        # Render game objects
        screen.fill((135, 206, 250))  # Sky blue background

        # Draw terrain
        pygame.draw.rect(screen, (139, 69, 19), FLAT)  # Flat ground (brown)
        pygame.draw.rect(screen, (169, 169, 169), STEEP)  # Steep slope (grey)

        player.draw(screen)
        draw_health_bar(screen, player)
        draw_stamina_bar(screen, player)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    run_game()

