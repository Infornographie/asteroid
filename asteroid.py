import random
from circleshape import *
from constants import *

class Asteroids(CircleShape):
    
    def __init__(self, x, y, radius, field):
        super().__init__(x, y, radius)
        self.field = field

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        # Split the asteroid into two smaller ones
        new_angle = random.uniform(20, 50)
        new_speed = random.uniform(0.8, 1.4)
        vector1 = self.velocity.rotate(new_angle)
        vector2 = self.velocity.rotate(-new_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        self.field.spawn(new_radius, self.position, vector1 * new_speed)
        self.field.spawn(new_radius, self.position, vector2 * new_speed)
        self.kill()
        