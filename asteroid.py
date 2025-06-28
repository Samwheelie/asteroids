import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        WHITE = (255, 255, 255)
        pygame.draw.circle(screen, WHITE, center=self.position, radius=self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)