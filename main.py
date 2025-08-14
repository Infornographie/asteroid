# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 1 / 60  

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Player.containers = updatables, drawables
    Asteroids.containers = asteroids, updatables, drawables
    AsteroidField.containers = updatables
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while pygame.get_init():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0, 0, 0))
        updatables.update(dt)
        for obj in drawables:
            obj.draw(screen)

        # Check for collisions between player and asteroids
        for asteroid in asteroids:
            if player.collides(asteroid):
                print("Game over!")
                pygame.quit()
                sys.exit()
                
        pygame.display.flip()
        clock.tick(60)  # Limit to 60 FPS      

if __name__ == "__main__":
    main()
