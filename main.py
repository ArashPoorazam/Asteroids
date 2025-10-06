import pygame
import player as p
from constants import *


def main():
    pygame.init()
    print("Starting Asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time = pygame.time.Clock()
    dt = 0

    player = p.player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    ### START THE GAME LOOP
    while True:    
        screen.fill(40)
        player.draw(screen)
        player.update(dt)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        dt = time.tick() / 1000
        pygame.display.flip()


if __name__ == "__main__":
    main()
