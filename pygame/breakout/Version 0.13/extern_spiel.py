import sys
import pygame
import time

from StdKlasse import BounceObj
from StdKlasse import StdBlock
from StdKlasse import PaddelObj
from StdKlasse import BrBlock
from StdKlasse import BrBlock1
from StdKlasse import BrBlock2
from StdKlasse import BrBlock3
from NmbrClass import NmbrObj

block_cls = [StdBlock, BrBlock3, BrBlock2, BrBlock1, BrBlock]

pygame.mixer.pre_init(22050, -16, 2, 1024)
pygame.init()

start_time = time.time()

size = 900, 950

width, height = 600, 800

BounceObj.set_borders([50, 650], [100, 900])

color = 40, 20, 20

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

Balls = []
Balls.append(BounceObj("grauball.png", 340, 420, 0, -2))
Balls.append(BounceObj("grauball.png", 360, 420, 0, -3))


def sound_generator():
    sounds = ["Dong" + str(x) + ".ogg" for x in range(1, 4)]
    while True:
        sound = sounds.pop(0)
        yield sound
        sounds.append(sound)

soundz = sound_generator()

pygame.mixer.get_init()

Blocks = []
for i in range(100, 300, 25):
    for j in range(50, width + 50, 60):
        if i >= 150 and i < 250 and j >= 170 and j < 530:
            continue
        Blocks.append(StdBlock(j, i, next(soundz)))

Paddels = []
Paddels.append(PaddelObj("paddelsmall.png", 300, 820, 50, width + 50))


def ball_generator():
    balls = ["Ball" + str(x) + ".png" for x in range(1, 13)]
    while True:
        ball = balls.pop(0)
        yield ball
        balls.append(ball)

ballz = ball_generator()

background = pygame.Surface.convert(pygame.image.load("bg.png"))
screen.blit(background, (0, 0))


pygame.display.update()
dirties = []

running = True
ass = NmbrObj(90903, 865, 150, 6)

while running:

    clock.tick(60)
#    print(Stats.get_points())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
            if event.key == pygame.K_SPACE:
                Balls.pop().destroy()
            if event.key == pygame.K_c:
                Balls.append(BounceObj(next(ballz), 360, 420, 0, -4))
            if event.key == pygame.K_v:
                for i in range(len(Blocks)):
                    Blocks.pop().destroy()
            if event.key == pygame.K_b:
                for i in range(100, 300, 25):
                    for j in range(50, width + 50, 60):
                        if i >= 150 and i < 250 and j >= 170 and j < 530:
                            continue
                        Blocks.append(StdBlock(j, i, next(soundz)))
                print(len(StdBlock.get_oblist()))
            if event.key == pygame.K_n:
                Paddels.pop().destroy()
            if event.key == pygame.K_m:
                BrBlock(250, 400)

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
    for i in block_cls:
        BounceObj.collide_rev(i.get_oblist())
    BounceObj.collide_rev(PaddelObj.get_oblist())

    BounceObj.update_pos()
    PaddelObj.update_pos()

    for i in block_cls:
        i.cleanup()
    BounceObj.cleanup()
    PaddelObj.cleanup()

    screen.blit(background, (0, 0))

    for i in block_cls:
        i.draw_all(screen)
    BounceObj.draw_all(screen)
    PaddelObj.draw_all(screen)

    dirties.extend(BounceObj.dirty)
    for i in block_cls:
        dirties.extend(i.dirty)
    dirties.extend(PaddelObj.dirty)

    NmbrObj.draw_all(screen)
    pygame.display.update(dirties)

    dirties, BounceObj.dirty, PaddelObj.dirty = [], [], []
    for i in block_cls:
        i.dirty = []
