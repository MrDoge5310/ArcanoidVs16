import pygame
import sys
import Models
pygame.init()

scr = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
GameOver = False

while not GameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()
    clock.tick(40)
