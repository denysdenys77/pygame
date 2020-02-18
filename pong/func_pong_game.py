import pygame
import random

pygame.init()
screen = pygame.display.set_mode((600, 400))


# padlle
paddle_x = 500
paddle_y = 285
paddle_width = 100
paddle_height = 30
paddle_speed = 5
paddle_color = (255, 255, 255)


# ball
ball_x = 200
ball_y = 300
ball_radius = 40
ball_speed = 5
ball_color = (255, 255, 255)

# выбор изначального направления
ball_direction = random.choice(['move_up_and_left', 'move_down_and_right',
                                'move_up_and_right', 'move_down_and_left'])

# main loop
while True:

    pygame.time.delay(30)

    # выход из игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    # управление ракеткой
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        paddle_y = paddle_y - paddle_speed
    elif keys[pygame.K_DOWN]:
        paddle_y = paddle_y + paddle_speed

    # движение мяча
    if ball_direction is 'move_up_and_left':
        ball_x = ball_x - ball_speed
        ball_y = ball_y - ball_speed
    elif ball_direction is 'move_down_and_right':
        ball_x = ball_x + ball_speed
        ball_y = ball_y + ball_speed
    elif ball_direction is 'move_up_and_right':
        ball_x = ball_x + ball_speed
        ball_y = ball_y - ball_speed
    elif ball_direction is 'move_down_and_left':
        ball_x = ball_x - ball_speed
        ball_y = ball_y + ball_speed

    # изменение траектории при столкновении со стеной
    if ball_x - ball_radius <= 0 and ball_direction is 'move_up_and_left':
        ball_direction = 'move_up_and_right'
    elif ball_x - ball_radius <= 0 and ball_direction is 'move_down_and_left':
        ball_direction = 'move_down_and_right'


    elif ball_y - ball_radius <= 0 and ball_direction is 'move_up_and_right':
        ball_direction = 'move_down_and_right'
    elif ball_y - ball_radius <= 0 and ball_direction is 'move_up_and_left':
        ball_direction = 'move_down_and_left'

    elif ball_y + ball_radius >= 400 and ball_direction is 'move_down_and_right':
        ball_direction = 'move_up_and_right'
    elif ball_y + ball_radius >= 400 and ball_direction is 'move_down_and_left':
        ball_direction = 'move_up_and_left'

    # изменение траектории при столкновении с ракеткой
    if ball_x + ball_radius == paddle_x and ball_y in range(paddle_y, paddle_y + paddle_height) and \
            ball_direction is 'move_up_and_right':
        ball_direction = 'move_up_and_left'
    elif ball_x + ball_radius == paddle_x and ball_y in range(paddle_y, paddle_y + paddle_height) and \
            ball_direction is 'move_down_and_right':
        ball_direction = 'move_down_and_left'

    # # касание верхнего края ракетки
    # if ball_x + ball_radius > paddle_x and ball_y + ball_radius == paddle_y and \
    #         ball_direction == 'move_down_and_right':
    #     ball_direction = 'move_up_and_right'
    #
    # # касание нижнего края ракетки
    # elif ball_x + ball_radius > paddle_x and ball_y == paddle_y + paddle_height and \
    #         ball_direction == 'move_up_and_right':
    #     ball_direction = 'move_down_and_right'


    if paddle_y < 0:
        paddle_y = 0
    if paddle_y + paddle_height > 400:
        paddle_y = 400 - paddle_height

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, paddle_color, (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)
    pygame.display.update()

