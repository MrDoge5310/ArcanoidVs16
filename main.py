import pygame
import sys
import Models
pygame.init()

width = 800
height = 600
scr = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
GameOver = False

ork = Models.Ork(0, 0)
ork.draw(scr)

platform = Models.Platform(width / 2, height)
platform.draw(scr)

while not GameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()
    clock.tick(40)
