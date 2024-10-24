import pygame

class Player:
    def __init__(self):
        self.rect = pygame.Rect(100, 500, 50, 50)  # Player hitbox
        self.idle_color = (255, 0, 0)  # Idle color (red)
        self.walking_colors = [(0, 255, 0), (0, 200, 0), (0, 150, 0)]  # Colors for walking animation
        self.jumping_color = (0, 0, 255)  # Jumping color (blue)
        self.current_color = self.idle_color  # Default to idle color

        self.velocity_y = 0
        self.is_jumping = False
        self.is_walking = False
        self.health = 100
        self.stamina = 100
        self.alive = True

        self.walk_frame = 0  # Frame index for walking animation
        self.walk_frame_timer = 0  # Timer to control frame change rate

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
        """Update the player's color/animation based on movement state."""
        if self.is_jumping:
            self.current_color = self.jumping_color  # Blue when jumping
        elif self.is_walking:
            # Cycle through walking colors for animation
            self.walk_frame_timer += 1
            if self.walk_frame_timer >= 5:  # Adjust to control frame speed
                self.walk_frame = (self.walk_frame + 1) % len(self.walking_colors)
                self.walk_frame_timer = 0
            self.current_color = self.walking_colors[self.walk_frame]
        else:
            self.current_color = self.idle_color  # Red when idle

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
        pygame.draw.rect(screen, self.current_color, self.rect)

