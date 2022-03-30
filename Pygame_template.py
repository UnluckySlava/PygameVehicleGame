import pygame as pg
from car_class2 import Car2
from tank_class import Tank, Bullet
from obstacle_classes import Square

# инициализация пайгейма
screen_size = screen_width, screen_height = 1200, 700
pg.init()
screen = pg.display.set_mode(screen_size)
clock = pg.time.Clock()

# создаём группы спрайтов
player = pg.sprite.GroupSingle()
enemies = pg.sprite.Group()
visible_sprites = pg.sprite.Group()

# создаём препятствие
square = Square()

# создаём "врага"
car = Car2(pg.image.load('car.png').convert_alpha())
car.add(enemies)

# создаём игрока
tank = Tank(pg.image.load('tank.png').convert_alpha())
tank.add(player)
player_sprite = pg.sprite.GroupSingle(tank)

# создаём массив снарядов танка
visible_sprites.add(square, car, tank)
bullets = []

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_r:
                visible_sprites.add(square, car)
            if event.key == pg.K_SPACE:
                bullet = Bullet(tank.angle, tank.pos)
                bullets.append(bullet)

    screen.fill('lightgrey')

    tank.control()
    tank.physics()
    tank.update()

    car.physics()
    car.update()

    for bullet in bullets:
        bullet.physics()
        bullet.collision(visible_sprites)
        if bullet.hit:
            bullets.pop(0)
        screen.blit(bullet.image, bullet.rect)

    visible_sprites.draw(screen)
    car.collision(visible_sprites)
    tank.collision(enemies)

    pg.display.flip()
    clock.tick(60)
    pg.display.set_caption(str(round(clock.get_fps(), 2)))
