import pygame as pg
from math import *
from car_class2 import Enemy

class Tank(pg.sprite.Sprite):

    pos = pg.math.Vector2(1000,500)
    angle = 0
    speed = 0

    def __init__(self, image):
        super().__init__()
        self.orig_image = image
        self.orig_image = pg.transform.scale(self.orig_image, (128, 128))
        self.rect = self.orig_image.get_rect(center=self.pos)
        self.mask = pg.mask.from_surface(self.orig_image)
        self.image = self.orig_image

    def control(self):
        if pg.key.get_pressed()[pg.K_UP]:
            self.speed -= 0.1
        if pg.key.get_pressed()[pg.K_DOWN]:
            self.speed += 0.1
        if pg.key.get_pressed()[pg.K_RIGHT]:
            self.angle -= 0.01
        if pg.key.get_pressed()[pg.K_LEFT]:
            self.angle += 0.01

    def physics(self):
        self.pos.x += self.speed * sin(self.angle)
        self.pos.y += self.speed * cos(self.angle)
        self.rect.center = self.pos - self.image.get_rect().center
        self.speed /= 1.03
        self.pos.x %= 1200
        self.pos.y %= 700

    def update(self):
        self.image = pg.transform.rotate(self.orig_image, degrees(self.angle))
        self.mask = pg.mask.from_surface(self.image)

    def collision(self, obstacles):
        for obstacle in obstacles:
            offset = obstacle.rect.x - self.rect.x, obstacle.rect.y - self.rect.y
            if self.mask.overlap(obstacle.mask, offset) and obstacle is not self:
                obstacle.kill()


class Bullet:
    speed = 10
    image = pg.image.load('bullet.png')
    image = pg.transform.scale(image,(50,50))
    hit = False

    def __init__(self, angle, pos):
        super().__init__()
        self.pos = pg.math.Vector2(pos)
        self.angle = angle
        self.image = pg.transform.rotate(self.image, degrees(self.angle))
        self.mask = pg.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=self.pos)

    def physics(self):
        self.pos.x -= self.speed * sin(self.angle)
        self.pos.y -= self.speed * cos(self.angle)
        self.rect.center = self.pos

    def collision(self, obstacles):
        for obstacle in obstacles:
            offset = obstacle.rect.x - self.rect.x, obstacle.rect.y - self.rect.y
            if self.mask.overlap(obstacle.mask, offset) and not isinstance(obstacle,Tank):
                if isinstance(obstacle, Enemy):
                    obstacle.kill()
                self.hit = True
