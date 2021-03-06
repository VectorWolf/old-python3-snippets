import sys, pygame, time
pygame.init()

start_time = time.time()

size = width, height = 740, 900
color = 40, 20, 20

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

ball = pygame.image.load("eckball.png")
ballrect = ball.get_rect()

paddel = pygame.image.load("paddel.png")
paddelrect = paddel.get_rect()

paddelrect.bottom = height - 15
paddelrect.left = 250

paddel2 = pygame.image.load("paddel.png")
paddel2rect = paddel2.get_rect()

paddel2rect.top = 15
paddel2rect.left = 250

maxspeed = 30
speed = [maxspeed/2,maxspeed/2]

paddel_speed = 0
paddel2_speed = 0

#pygame.key.set_repeat(1, 30)

while True:
  
    clock.tick(30) 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
        	sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
            #if event.key == pygame.K_LEFT and paddel_speed > -maxspeed:
            #    paddel_speed -= 3                             
            #if event.key == pygame.K_RIGHT and paddel_speed < maxspeed:
            #    paddel_speed += 3
            #if event.key == pygame.K_a and paddel2_speed > -maxspeed:
            #    paddel2_speed -= 3                             
            #if event.key == pygame.K_d and paddel2_speed < maxspeed:
            #    paddel2_speed += 3
    
    presslist = pygame.key.get_pressed()
    
    if presslist[pygame.K_LEFT] and paddel_speed > -maxspeed:
        paddel_speed -= 3
    if presslist[pygame.K_RIGHT] and paddel_speed < maxspeed:
        paddel_speed += 3
    if presslist[pygame.K_a] and paddel2_speed > -maxspeed:
        paddel2_speed -= 3
    if presslist[pygame.K_d] and paddel2_speed < maxspeed:
        paddel2_speed += 3
        
    if paddel_speed > 0:
    	paddel_speed -= 1
    elif paddel_speed < 0:
    	paddel_speed += 1
    if paddel2_speed > 0:
    	paddel2_speed -= 1
    elif paddel2_speed < 0:
    	paddel2_speed += 1

    if paddelrect.left < 0 and paddel_speed < 0:
        paddel_speed = -paddel_speed/2
        
    if paddelrect.right > width and paddel_speed > 0:
        paddel_speed = -paddel_speed/2
        
    if paddel2rect.left < 0 and paddel2_speed < 0:
        paddel2_speed = -paddel2_speed/2
        
    if paddel2rect.right > width and paddel2_speed > 0:
        paddel2_speed = -paddel2_speed/2
    	                  
    ballrect = ballrect.move(speed)
    paddelrect = paddelrect.move(paddel_speed,0)
    paddel2rect = paddel2rect.move(paddel2_speed,0)
    
    if ballrect.left < 0 and speed[0] < 0:
        speed[0] = -speed[0]
        
    if ballrect.right > width and speed[0] > 0:
        speed[0] = -speed[0]
        
    if ballrect.top < 0 and speed[1] < 0:
        ballrect.top = height / 2
        ballrect.left = width / 2        
        #speed[1] = -speed[1]
        
    if ballrect.bottom > height and speed[1] > 0:
        #speed[1] = -speed[1]
        ballrect.top = height / 2
        ballrect.left = width / 2
    
        
    if ballrect.bottom in range(860,870) and speed[1] > 0:
        paddel_set = set(range(paddelrect.left,paddelrect.right))
        ball_set = set(range(ballrect.left,ballrect.right))
        if not paddel_set.isdisjoint(ball_set):
            #speed = [-(maxspeed-abs(paddel_speed))+3,paddel_speed-3]
            speed[1] = -speed[1]
            
    if ballrect.top in range(30,40) and speed[1] < 0:
        paddel_set = set(range(paddel2rect.left,paddel2rect.right))
        ball_set = set(range(ballrect.left,ballrect.right))
        if not paddel_set.isdisjoint(ball_set):
            #speed = [-(maxspeed-abs(paddel_speed))+3,paddel_speed-3]
            speed[1] = -speed[1]            
            
        
        
    screen.fill(color)
    screen.blit(ball, ballrect)
    screen.blit(paddel, paddelrect)
    screen.blit(paddel2, paddel2rect)
    pygame.display.flip()
