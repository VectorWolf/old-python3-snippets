import sys, pygame, time
pygame.init()

start_time = time.time()

size = width, height = 1280, 900
color = 1, 1, 1

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

ball = pygame.image.load("ball.gif")
ballrect = ball.get_rect()

rspeed = [20, 20]
speed = [20, 20]

radd = 5
gadd = 1
badd = 2

while True:
  
    clock.tick(60) 
    
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
        
    for i in range(2):
    	if speed[i] < 0:
    		speed[i] = -rspeed[i] * (color[i] / 255)
    	else:
    		speed[i] = rspeed[i] * (color[i] / 255)
                
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 and speed[0] < 0:
        speed[0] = -speed[0]
        
    if ballrect.right > width and speed[0] > 0:
        speed[0] = -speed[0]
        
    if ballrect.top < 0 and speed[1] < 0:
        speed[1] = -speed[1]
        
    if ballrect.bottom > height and speed[1] > 0:
        speed[1] = -speed[1]
        
    screen.fill(color)
    screen.blit(ball, ballrect)
    pygame.display.flip()
