import sys, pygame, time
pygame.init()

start_time = time.time()

size = width, height = 1280, 900
color = 1, 1, 1

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

radd = 5
gadd = 10
badd = 20

while True:
  
    clock.tick(30) 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        
    color = color[0] + radd, color[1] + gadd, color[2] + badd

    if color[0] > 255 or color[0] < 0:
        radd *= -1
        color = color[0] + 2*radd,color[1],color[2]
        
    if color[1] > 255 or color[1] < 0:
        gadd *= -1  
        color = color[0],color[1] + 2*gadd,color[2]
                
    if color[2] > 255 or color[2] < 0:
        badd *= -1
        color = color[0],color[1],color[2] + 2*badd
        
    print(color)
    screen.fill(color)
    pygame.display.flip()
