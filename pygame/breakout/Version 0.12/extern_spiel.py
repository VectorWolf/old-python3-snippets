import sys
import pygame
import time

from StdKlasse import BounceObj
from StdKlasse import StaticObj
from StdKlasse import PaddelObj

pygame.init()

start_time = time.time()

size = width, height = 600, 800

BounceObj.set_borders([0, width], [0, height])

color = 40, 20, 20

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

Balls = []
Balls.append(BounceObj("grauball.png", 340, 420, 0, -2))
Balls.append(BounceObj("grauball.png", 360, 420, 0, -3))


Blocks = []
for i in range(0, 200, 25):
    for j in range(0, width, 60):
        if i >= 50 and i < 150 and j >= 120 and j < 480:
            continue
        Blocks.append(StaticObj("block.png", j, i))

Paddels = []
Paddels.append(PaddelObj("paddelsmall.png", 300, 720, 0, width))

while True:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
            if event.key == pygame.K_SPACE:
                Balls.pop().destroy()
            if event.key == pygame.K_c:
                Balls.append(BounceObj("grauball.png", 360, 420, 0, -4))
            if event.key == pygame.K_v:
                for i in range(len(Blocks)):
                    Blocks.pop().destroy()
            if event.key == pygame.K_b:
                for i in range(0, 200, 25):
                    for j in range(0, width, 60):
                        if i >= 50 and i < 150 and j >= 120 and j < 480:
                            continue
                        Blocks.append(StaticObj("block.png", j, i))
                print(len(StaticObj.get_oblist()))
            if event.key == pygame.K_n:
                Paddels.pop().destroy()

    presslist = pygame.key.get_pressed()

    if presslist[pygame.K_LEFT]:
        PaddelObj.get_oblist()[1].move_left()
    if presslist[pygame.K_RIGHT]:
        PaddelObj.get_oblist()[1].move_right()
    if presslist[pygame.K_a]:
        PaddelObj.get_oblist()[0].move_left()
    if presslist[pygame.K_d]:
        PaddelObj.get_oblist()[0].move_right()

    BounceObj.collide_dyn_self()
    BounceObj.collide_rev(StaticObj.get_oblist())
    BounceObj.collide_rev(PaddelObj.get_oblist())

    BounceObj.update_pos()
    PaddelObj.update_pos()

    StaticObj.cleanup()
    BounceObj.cleanup()
    PaddelObj.cleanup()

    screen.fill(color)

    BounceObj.draw_all(screen)
    StaticObj.draw_all(screen)
    PaddelObj.draw_all(screen)

    pygame.display.flip()
