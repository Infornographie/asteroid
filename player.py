from constants import *
from circleshape import *

class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = 0.0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        points = self.triangle()
        pygame.draw.polygon(screen, (255, 255, 255), points, width=2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.cooldown -= dt

        if keys[pygame.K_q]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_z]:
            self.move(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self):
        if self.cooldown <= 0:
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            shot_position = self.position + forward * (self.radius + SHOT_RADIUS)
            shot_velocity = forward * PLAYER_SHOOT_SPEED
            self.cooldown = PLAYER_SHOOT_COOLDOWN
            return Shot(shot_position.x, shot_position.y, SHOT_RADIUS, shot_velocity)
        else:
            pass

class Shot(CircleShape):

    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt