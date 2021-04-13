import pygame
import time
from pygame.locals import *

if __name__ == "__main__":
    pygame.init()

    #update background surface to green
    surface = pygame.display.set_mode((500,500))
    surface.fill((56,123,45))

    #snek :D
    block = pygame.image.load("images/Block.png").convert()
    surface.blit(block,(0,0))

    ##update Screen
    pygame.display.flip()
    #While running is true dont stop the game loop
    running = True

    #game loop
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                pass
            elif event.type == QUIT:
                running = False
        
