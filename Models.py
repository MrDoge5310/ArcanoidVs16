import pygame


class Sprite:
    def __init__(self, x, y, image_name):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, 10, 10)
        self.image = pygame.image.load(image_name)

    def draw(self, scr):
        scr.blit(self.image, (self.rect.x, self.rect.y))


class Ork(Sprite):
    def __init__(self, x, y,):
        super().__init__(x, y, "ork_image.png")


class Ball(Sprite):
    def __init__(self, x, y):
        super().__init__(x, y, "cannonball.png")
