import pygame

class Player:
    def __init__(self):
        self.rect = pygame.Rect(100, 500, 50, 50)  # Player hitbox
        self.color = (255, 0, 0)  # Player color
        self.velocity_y = 0
        self.is_jumping = False
        self.health = 100  # Health starts at 100
        self.stamina = 100  # Stamina starts at 100
        self.alive = True  # Player starts alive

    def handle_input(self):
        if not self.alive:
            return  # Player can't move when dead

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_SPACE] and not self.is_jumping:
            if self.stamina > 0:
                self.is_jumping = True
                self.velocity_y = -10  # Jump velocity
                self.stamina -= 10  # Reduce stamina when jumping

    def apply_gravity(self):
        if not self.alive:
            return  # No gravity if the player is dead

        self.velocity_y += 0.5  # Simulate gravity
        self.rect.y += self.velocity_y
        if self.rect.y >= 500:  # Hit the ground
            self.rect.y = 500
            self.is_jumping = False

        if not self.is_jumping:
            self.stamina = min(self.stamina + 1, 100)  # Regain stamina while on the ground

    def take_damage(self, amount):
        if not self.alive:
            return  # No damage if the player is already dead

        self.health -= amount
        if self.health <= 0:
            self.die()

    def die(self):
        self.alive = False
        print("Game Over!")  # Temporary Game Over message

    def respawn(self):
        self.rect.x, self.rect.y = 100, 500  # Reset player position
        self.health = 100  # Reset health
        self.stamina = 100  # Reset stamina
        self.alive = True  # Player is alive again

    def update(self):
        self.handle_input()
        self.apply_gravity()

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

