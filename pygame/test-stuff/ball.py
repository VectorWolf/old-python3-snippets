import sys, pygame
pygame.init()


size = width, height = 800, 600
speed = [1, 1]
bg_color = 0, 255, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("Dick.gif")
ballrect = ball.get_rect()

frames = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(bg_color)
    screen.blit(ball, ballrect)
    pygame.display.flip()
