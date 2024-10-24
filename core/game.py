import pygame
from core.player import Player
from core.settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS

def draw_health_bar(screen, player):
    pygame.draw.rect(screen, (255, 0, 0), (10, 10, player.health * 2, 20))  # Red health bar
    pygame.draw.rect(screen, (0, 0, 0), (10, 10, 200, 20), 2)  # Black border

def draw_stamina_bar(screen, player):
    pygame.draw.rect(screen, (0, 255, 0), (10, 40, player.stamina * 2, 20))  # Green stamina bar
    pygame.draw.rect(screen, (0, 0, 0), (10, 40, 200, 20), 2)  # Black border

def show_game_over(screen):
    font = pygame.font.SysFont(None, 55)
    text = font.render('Game Over!', True, (255, 0, 0))
    screen.blit(text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 30))
    pygame.display.flip()
    pygame.time.wait(2000)  # Pause for 2 seconds before respawning

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

        if not player.alive:
            show_game_over(screen)
            player.respawn()

        # Update game objects
        player.update()

        # Render game objects
        screen.fill((135, 206, 250))  # Sky blue background
        player.draw(screen)
        draw_health_bar(screen, player)
        draw_stamina_bar(screen, player)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    run_game()

