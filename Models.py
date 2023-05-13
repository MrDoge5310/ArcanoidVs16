import pygame


class Sprite:
    def __init__(self, x, y, image_name):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, 20, 20)
        self.image = pygame.image.load(image_name)

    def draw(self, scr):
        scr.blit(self.image, (self.rect.x, self.rect.y))


class Ork(Sprite):
    def __init__(self, x, y,):
        super().__init__(x, y, "ork_image.png")


class Ball(Sprite):
    def __init__(self, x, y):
        super().__init__(x, y, "cannonball.png")
        self.dx = -3
        self.dy = -3

    def move(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

    def check_colision(self, pl):
        # collide walls
        if self.rect.x + 20 == 800 and self.rect.y in range(0, 600 - 20):
            self.dx *= -1
        elif self.rect.x == 0 and self.rect.y in range(0, 600 - 20):
            self.dx *= -1
        elif self.rect.y <= 0:
            self.dy *= -1
        # collide platform
        if self.rect.colliderect(pl.rect):
            self.dy *= -1
        if self.rect.y >= 600:
            return True
        else:
            return False

    def collide_enemy(self, ork):
        if self.rect.colliderect(ork.rect):
            self.dy *= -1
            return True
        else:
            return False


class Platform:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = 'white'
        self.rect = pygame.Rect(self.x - 75, self.y - 75, 150, 20)

    def draw(self, scr):
        pygame.draw.rect(scr, self.color, self.rect, 0, 5)

    def move_left(self):
        if self.rect.x - 20 >= 0:
            self.rect.x -= 20

    def move_right(self):
        if self.rect.x + self.rect.width + 20 <= 800:
            self.rect.x += 20
