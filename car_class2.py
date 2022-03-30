import pygame as pg
from math import *

class Enemy(pg.sprite.Sprite):
    pass

class Car2(Enemy):

    pos = pg.math.Vector2(600,450)
    angle = 0
    speed = 0

    def __init__(self, image):
        super().__init__()
        self.orig_image = image
        self.orig_image = pg.transform.scale(self.orig_image, (128, 128))
        self.rect =  self.orig_image.get_rect(center=self.pos)
        self.mask =  pg.mask.from_surface(self.orig_image)
        self.image = self.orig_image

    def control(self):
        if pg.key.get_pressed()[pg.K_w]:
            self.speed -= 0.1
        if pg.key.get_pressed()[pg.K_s]:
            self.speed += 0.1
        if pg.key.get_pressed()[pg.K_a]:
            self.angle -= 0.005 * self.speed
        if pg.key.get_pressed()[pg.K_d]:
            self.angle += 0.005 * self.speed

    def physics(self):
        self.pos.x += self.speed * sin(self.angle)
        self.pos.y += self.speed * cos(self.angle)
        self.rect.center = self.pos - self.image.get_rect().center
        self.speed /= 1.01
        self.pos.x %= 1200
        self.pos.y %= 700

    def update(self):
        self.image = pg.transform.rotate(self.orig_image, degrees(self.angle))
        self.mask = pg.mask.from_surface(self.image)

    def collision(self, obstacles):
        for obstacle in obstacles:
            offset = obstacle.rect.x - self.rect.x, obstacle.rect.y - self.rect.y
            if self.mask.overlap(obstacle.mask, offset) and not isinstance(obstacle, Car2):
                pass
