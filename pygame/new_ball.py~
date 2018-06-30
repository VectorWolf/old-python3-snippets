import sys, pygame, time
pygame.init()

start_time = time.time()

size = width, height = 1280, 900
speed = [10, 10]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.gif")
ballrect = ball.get_rect()

frames = 0

clock = pygame.time.Clock()

while True:

    clock.tick(30) 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    #print (speed)
    #frames += 1
    #print("Frames = " + str(frames))
    #print(str(time.time() - start_time) + " seconds")
    #print(str(frames / (time.time() - start_time)) +" fps") 

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
