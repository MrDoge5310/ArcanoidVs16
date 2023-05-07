import pygame
import sys
import Models
pygame.init()

width = 800
height = 600
scr = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
GameOver = False

orks = []
i = 0
for y in range(0, height // 2, 20):
    for x in range(0, width, 20):
        orks.append(Models.Ork(x, y))
        orks[i].draw(scr)
        i += 1

platform = Models.Platform(width / 2, height)
platform.draw(scr)

while not GameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()
    clock.tick(40)
