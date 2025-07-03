import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        WHITE = (255, 255, 255)
        pygame.draw.circle(screen, WHITE, center=self.position, radius=self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if(self.radius <= ASTEROID_MIN_RADIUS):
            return

        displacement = random.uniform(20, 50)

        v1 = pygame.math.Vector2.rotate(self.velocity, displacement)
        v2 = pygame.math.Vector2.rotate(self.velocity, -displacement)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = v1 * 1.2
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = v2 * 1.2
        