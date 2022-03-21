import pygame as pg

class Square(pg.sprite.Sprite):
    pos = pg.math.Vector2(100,100)
    image = pg.surface.Surface((200,200))
    rect = image.get_rect(topleft=pos)
    mask = pg.mask.from_surface(image)

