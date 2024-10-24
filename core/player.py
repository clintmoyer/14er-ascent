import pygame

class Player:
    def __init__(self):
        self.rect = pygame.Rect(100, 500, 50, 50)  # Placeholder player rectangle
        self.color = (255, 0, 0)  # Red color for now
        self.velocity_y = 0
        self.is_jumping = False

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_SPACE] and not self.is_jumping:
            self.is_jumping = True
            self.velocity_y = -10  # Jump velocity

    def apply_gravity(self):
        self.velocity_y += 0.5  # Gravity effect
        self.rect.y += self.velocity_y
        if self.rect.y >= 500:  # Hit ground
            self.rect.y = 500
            self.is_jumping = False

    def update(self):
        self.handle_input()
        self.apply_gravity()

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
