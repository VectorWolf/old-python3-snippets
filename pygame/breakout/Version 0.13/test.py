def ball_generator():

    balls = ["Ball" + str(x) + ".png" for x in range(1, 13)]
    while True:
        ball = balls.pop(0)
        yield ball
        balls.append(ball)
