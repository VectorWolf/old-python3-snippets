import sys, pygame, time
pygame.init()

start_time = time.time()

size = width, height = 666, 450
color = 40, 20, 20

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

ball = pygame.image.load("eckball.png")
ballrect = ball.get_rect()

ball2 = pygame.image.load("eckball.png")
ball2rect = ball.get_rect()

ball2rect.top = 180
ball2rect.right = 460

speed = [5, 5]
speed2 = [5, 5]

paddel_speed = 0

while True:
  
    clock.tick(120) 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
                
    ballrect = ballrect.move(speed)
    ball2rect = ball2rect.move(speed2)
    
    if ballrect.left < 0 and speed[0] < 0:
        speed[0] = -speed[0]
        
    if ballrect.right > width and speed[0] > 0:
        speed[0] = -speed[0]
        
    if ballrect.top < 0 and speed[1] < 0:
        speed[1] = -speed[1]
        
    if ballrect.bottom > height and speed[1] > 0:
        speed[1] = -speed[1]
        
    if ball2rect.left < 0 and speed2[0] < 0:
        speed2[0] = -speed2[0]
        
    if ball2rect.right > width and speed2[0] > 0:
        speed2[0] = -speed2[0]
        
    if ball2rect.top < 0 and speed2[1] < 0:
        speed2[1] = -speed2[1]
        
    if ball2rect.bottom > height and speed2[1] > 0:
        speed2[1] = -speed2[1]
    
    
    if ballrect.colliderect(ball2rect):
        ballho = set(range(ballrect.top,ballrect.bottom))
        ballbr = set(range(ballrect.left,ballrect.right))
        ball2ho = set(range(ball2rect.top,ball2rect.bottom))
        ball2br = set(range(ball2rect.left,ball2rect.right))
        if len(ballho.intersection(ball2ho)) > len(ballbr.intersection(ball2br)):
            speed[0] = -speed[0]
            speed2[0] = -speed2[0]
        else:
            speed[1] = -speed[1]
            speed2[1] = -speed2[1]
    
    screen.fill(color)
    screen.blit(ball, ballrect)
    #screen.blit(paddel, paddelrect)
    screen.blit(ball2, ball2rect)
    pygame.display.flip()
