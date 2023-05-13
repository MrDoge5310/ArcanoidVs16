import pygame
import sys
import Models
from tkinter import messagebox
pygame.init()

width = 800
height = 600
scr = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
GameOver = False
score = 0

orks = []
i = 0
for y in range(0, height // 2, 20):
    for x in range(0, width, 20):
        orks.append(Models.Ork(x, y))


platform = Models.Platform(width / 2, height)
ball = Models.Ball(width // 2 - 10, height - 95)

while not GameOver:
    scr.fill('black')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                platform.move_right()
            if event.key == pygame.K_LEFT:
                platform.move_left()

    ball.move()
    GameOver = ball.check_colision(platform)
    for ork in orks:
        if ball.collide_enemy(ork):
            orks.remove(ork)
            score += 1
        else:
            ork.draw(scr)

    platform.draw(scr)
    ball.draw(scr)
    pygame.display.update()
    clock.tick(40)
messagebox.showinfo('GameOver', f"GameOver!\nYour Score is: {score}")
sys.exit("GameOver")
