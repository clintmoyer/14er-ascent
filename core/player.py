import pygame
import random

class Player:
    def __init__(self):
        # Load the player animation images (idle, walk, jump)
        self.idle_image = pygame.image.load("assets/images/player/idle.png").convert_alpha()
        self.walk_images = [
            pygame.image.load("assets/images/player/walk1.png").convert_alpha(),
            pygame.image.load("assets/images/player/walk2.png").convert_alpha()
        ]
        self.jump_image = pygame.image.load("assets/images/player/jump.png").convert_alpha()

        self.current_image = self.idle_image
        self.rect = self.current_image.get_rect(midbottom=(100, 500))

        self.velocity_y = 0
        self.is_jumping = False
        self.is_walking = False
        self.is_climbing = False
        self.on_steep_slope = False

        self.health = 100
        self.stamina = 100
        self.alive = True

        self.walk_frame = 0
        self.walk_frame_timer = 0

        self.wind_resistance = False  # Wind will slow the player
        self.slide_down = False  # Sliding when on a steep surface

    def handle_input(self):
        if not self.alive:
            return

        keys = pygame.key.get_pressed()
        self.is_walking = False
        self.is_climbing = False

        # Wind resistance effect
        wind_strength = random.choice([0, 1, 2, 3]) if self.wind_resistance else 0

        if keys[pygame.K_LEFT]:
            self.rect.x -= (5 - wind_strength)
            self.is_walking = True
        if keys[pygame.K_RIGHT]:
            self.rect.x += (5 - wind_strength)
            self.is_walking = True
        if keys[pygame.K_SPACE] and not self.is_jumping:
            if self.stamina > 0:
                self.is_jumping = True
                self.velocity_y = -10
                self.stamina -= 10  # Decrease stamina when jumping

        # Slow movement when climbing (scrambling on steep slopes)
        if self.on_steep_slope:
            self.is_climbing = True
            self.rect.x += (1 if keys[pygame.K_RIGHT] else -1)  # Slower movement
            self.stamina -= 0.1  # Decrease stamina when climbing

    def apply_gravity(self):
        if not self.alive:
            return

        # Apply gravity with sliding or wind resistance
        gravity = 0.5 if not self.slide_down else 1.0
        self.velocity_y += gravity
        self.rect.y += self.velocity_y

        if self.rect.y >= 500:
            self.rect.y = 500
            self.is_jumping = False
            self.slide_down = False

        # Stamina regenerates when idle
        if not self.is_jumping and not self.is_climbing:
            self.stamina = min(self.stamina + 0.5, 100)

    def update_animation(self):
        """Update the player's image based on movement state (idle, walking, jumping)."""
        if self.is_jumping:
            self.current_image = self.jump_image  # Jumping image
        elif self.is_climbing:
            self.current_image = self.walk_images[self.walk_frame]  # Climbing looks like slow walking
        elif self.is_walking:
            # Cycle through walking images
            self.walk_frame_timer += 1
            if self.walk_frame_timer >= 10:  # Control speed of walking animation
                self.walk_frame = (self.walk_frame + 1) % len(self.walk_images)
                self.walk_frame_timer = 0
            self.current_image = self.walk_images[self.walk_frame]
        else:
            self.current_image = self.idle_image  # Idle image

    def take_damage(self, amount):
        if not self.alive:
            return
        self.health -= amount
        if self.health <= 0:
            self.die()

    def die(self):
        self.alive = False
        print("Game Over!")

    def respawn(self):
        self.rect.x, self.rect.y = 100, 500
        self.health = 100
        self.stamina = 100
        self.alive = True

    def update(self):
        self.handle_input()
        self.apply_gravity()
        self.update_animation()

    def draw(self, screen):
        screen.blit(self.current_image, self.rect)

    # Simulate wind resistance
    def apply_wind(self, active=True):
        self.wind_resistance = active

    # Simulate sliding down steep slopes
    def apply_sliding(self, sliding=True):
        self.slide_down = sliding

