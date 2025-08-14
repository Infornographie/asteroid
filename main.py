# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

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
    
    Player.containers = updatables, drawables
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while pygame.get_init():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0, 0, 0))
        updatables.update(dt)
        for obj in drawables:
            obj.draw(screen)

        pygame.display.flip()
        clock.tick(60)  # Limit to 60 FPS      

if __name__ == "__main__":
    main()
