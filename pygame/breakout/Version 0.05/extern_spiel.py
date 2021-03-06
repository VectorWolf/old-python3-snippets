import sys
import pygame
import time

from StdKlasse import BounceObj
from StdKlasse import StaticObj
from StdKlasse import PaddelObj

pygame.init()

start_time = time.time()

size = width, height = 600, 800

BounceObj.SetBorders([0,width],[0,height])

color = 40, 20, 20

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()         

Balls = []
Balls.append(BounceObj("grauball.png",340,420,0,-6))
Balls.append(BounceObj("grauball.png",360,420,0,-4))


Blocks = []
for i in range(0,200,25):
    for j in range (0,width,60):
        if i >= 50 and i < 150 and j >= 120 and j < 480:
            continue
        Blocks.append(StaticObj("block.png",j,i))
                
Paddels = []
Paddels.append(PaddelObj("paddel.png", 300,710,0,width))
Paddels.append(PaddelObj("paddelsmall.png", 300,680,0,width))

while True:
  
    clock.tick(60) 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
            if event.key == pygame.K_SPACE:
                Balls.pop().Destroy()
            if event.key == pygame.K_c:
                Balls.append(BounceObj("grauball.png",360,420,0,-4))
            if event.key == pygame.K_v:
                for i in range(len(Blocks)):
                    Blocks.pop().Destroy()
            if event.key == pygame.K_b:
                for i in range(0,200,25):
                    for j in range (0,width,60):
                        if i >= 50 and i < 150 and j >= 120 and j < 480:
                            continue
                        Blocks.append(StaticObj("block.png",j,i))
                print(len(StaticObj.GetOblist()))
            if event.key == pygame.K_n:
                Paddels.pop().Destroy()
        
    presslist = pygame.key.get_pressed()

    if presslist[pygame.K_LEFT]:
        PaddelObj.GetOblist()[0].MoveLeft()
    if presslist[pygame.K_RIGHT]:
        PaddelObj.GetOblist()[0].MoveRight()
    if presslist[pygame.K_a]:
        PaddelObj.GetOblist()[1].MoveLeft()
    if presslist[pygame.K_d]:
        PaddelObj.GetOblist()[1].MoveRight()

    BounceObj.Collide()
    BounceObj.Collide(StaticObj.GetOblist())
    BounceObj.Collide(PaddelObj.GetOblist())            
        
    BounceObj.UpdatePos()
    PaddelObj.UpdatePos()
        
    StaticObj.Cleanup()
    BounceObj.Cleanup()
    PaddelObj.Cleanup()
        
    screen.fill(color) 
           
    BounceObj.DrawAll(screen)
    StaticObj.DrawAll(screen)
    PaddelObj.DrawAll(screen)
    
    
    pygame.display.flip()
