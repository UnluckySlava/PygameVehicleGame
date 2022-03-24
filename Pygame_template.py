import pygame as pg
from car_class2 import Car2
from tank_class import Tank, Bullet
from obstacle_classes import Square

# инициализация пайгейма
screen_size = screen_width, screen_height = 1200, 700
pg.init()
screen = pg.display.set_mode(screen_size)
clock = pg.time.Clock()

player = pg.sprite.GroupSingle()
enemies = pg.sprite.Group()
visible_sprites = pg.sprite.Group()

# создаём препятствие
square = Square()

# создаём машину
car = Car2(pg.image.load('car.png').convert_alpha())
car.add(enemies)

# создаём танк
tank = Tank(pg.image.load('tank.png').convert_alpha())
tank.add(player)

# player_sprite = pg.sprite.GroupSingle(tank)

visible_sprites.add(square, car, tank)
bullets = []
pressed = False

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if pg.key.get_pressed()[pg.K_r]:
            visible_sprites.add(square, car)

        if pg.key.get_pressed()[pg.K_SPACE]:
            if not pressed:
                bullet = Bullet(tank.angle,tank.pos)
                bullets.append(bullet)
            pressed = True
        else:
            pressed = False

    screen.fill('lightgrey')

    tank.control()
    tank.physics()
    tank.draw()

    car.physics()
    car.draw()

    for bullet in bullets:
        bullet.physics()
        bullet.collision(visible_sprites)
        if (0, 0) > bullet.rect.center\
                or bullet.rect.center > screen_size\
                or bullet.hit:
            bullets.pop(0)
        screen.blit(bullet.image, bullet.rect)

    visible_sprites.draw(screen)
    car.collision(visible_sprites)
    tank.collision(enemies)

    pg.display.flip()
    clock.tick(60)
