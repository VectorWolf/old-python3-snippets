import sys, pygame, time
pygame.init()

start_time = time.time()

size = width, height = 1280, 900
color = 255, 0, 0

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

while True:

    clock.tick(30) 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        
    if color == (255, 0 ,0):
        color = 0,255,0
    elif color == (0,255,0):
        color = 0,0,255
    elif color == (0,0,255):
        color = 255,0,0
        
    screen.fill(color)
    pygame.display.flip()
