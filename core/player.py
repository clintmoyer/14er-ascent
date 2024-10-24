import pygame

class Player:
    def __init__(self):
        # Load the player animation images (these should be PNGs generated from your SVGs)
        self.idle_image = pygame.image.load("assets/images/player/idle.png").convert_alpha()
        self.walk_images = [
            pygame.image.load("assets/images/player/walk1.png").convert_alpha(),
            pygame.image.load("assets/images/player/walk2.png").convert_alpha()
        ]
        self.jump_image = pygame.image.load("assets/images/player/jump.png").convert_alpha()

        self.current_image = self.idle_image  # Start with idle state
        self.rect = self.current_image.get_rect(midbottom=(100, 500))  # Player rectangle

        self.velocity_y = 0
        self.is_jumping = False
        self.is_walking = False
        self.health = 100
        self.stamina = 100
        self.alive = True

        # Animation variables
        self.walk_frame = 0  # To keep track of which walking frame to show
        self.walk_frame_timer = 0  # Timer to control frame changes

    def handle_input(self):
        if not self.alive:
            return

        keys = pygame.key.get_pressed()
        self.is_walking = False  # Reset walking state

        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
            self.is_walking = True
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
            self.is_walking = True
        if keys[pygame.K_SPACE] and not self.is_jumping:
            if self.stamina > 0:
                self.is_jumping = True
                self.velocity_y = -10
                self.stamina -= 10

    def apply_gravity(self):
        if not self.alive:
            return

        self.velocity_y += 0.5
        self.rect.y += self.velocity_y
        if self.rect.y >= 500:
            self.rect.y = 500
            self.is_jumping = False

        if not self.is_jumping:
            self.stamina = min(self.stamina + 1, 100)

    def update_animation(self):
        """Update the player's image based on movement state (idle, walking, jumping)."""
        if self.is_jumping:
            self.current_image = self.jump_image  # Show jumping image
        elif self.is_walking:
            # Cycle through walking images
            self.walk_frame_timer += 1
            if self.walk_frame_timer >= 10:  # Control speed of walking animation
                self.walk_frame = (self.walk_frame + 1) % len(self.walk_images)
                self.walk_frame_timer = 0
            self.current_image = self.walk_images[self.walk_frame]  # Show walking frame
        else:
            self.current_image = self.idle_image  # Show idle image

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
        screen.blit(self.current_image, self.rect)  # Draw the current animation frame

