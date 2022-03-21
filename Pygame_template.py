import pygame as pg
from car_class2 import Car2
from tank_class import Tank, Bullet
from obstacle_classes import Square

# инициализация пайгейма
screen_size = screen_width, screen_height = 1200, 700
pg.init()
screen = pg.display.set_mode(screen_size)
clock = pg.time.Clock()
visible_sprites = pg.sprite.Group()

# создаём препятствие
square = Square()

# создаём машину
car = Car2(pg.image.load('car.png').convert_alpha())

# создаём танк
tank = Tank(pg.image.load('tank.png').convert_alpha())

# player_sprite = pg.sprite.GroupSingle(tank)

visible_sprites.add(square, car, tank)
bullets = []

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if pg.key.get_pressed()[pg.K_r]:
            visible_sprites.add(square, car)

        if pg.key.get_pressed()[pg.K_SPACE]:
            bullet = Bullet(tank.angle,tank.pos)
            bullets.append(bullet)

    screen.fill('lightgrey')

    tank.control()
    tank.physics()
    tank.draw()

    car.control()
    car.physics()
    car.draw()

    for bullet in bullets:
        bullet.physics()
        bullet.collision(visible_sprites)
        screen.blit(bullet.image, bullet.rect)

    # player_sprite.draw(screen)
    visible_sprites.draw(screen)
    car.collision(visible_sprites)
    tank.collision(visible_sprites)

    pg.display.flip()
    clock.tick(60)
