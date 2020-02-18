import pygame

class Game:



    def run(self, round, paddle, ball):

        SCREEN_WIDTH = 600
        SCREEN_HIGHT = 800

        current_round = 1

        while True:

            pygame.init()
            screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))


            if current_round == 1:
                round.create_first_round()
            elif current_round == 2:
                round.create_second_round()
            elif current_round == 3:
                round.create_third_round()
            else:
                quit()

            while len(round.set) is not 0:
                pygame.time.delay(30)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quit()

                if ball.ball_y > 800:
                    quit()

                round.check_ball_contact(ball)

                ball.check_screen_borders(SCREEN_WIDTH)
                ball.move()
                ball.check_paddle_hit(paddle)

                paddle.move()
                paddle.check_screen_borders(SCREEN_WIDTH)

                screen.fill((0, 0, 0))

                for block in round.set:
                    pygame.draw.rect(screen, (255, 255, 255), (block[0], block[1], 60, 40))
                    pygame.draw.rect(screen, (230, 230, 230), (block[0] + 1, block[1] + 1, 58, 38))

                pygame.draw.rect(screen, paddle.collor, (paddle.paddle_x, paddle.paddle_y, paddle.paddle_width, paddle.paddle_height))
                pygame.draw.circle(screen, ball.color, (ball.ball_x, ball.ball_y), ball.ball_radius)
                pygame.display.update()

            current_round += 1
            ball.ball_x = 200
            ball.ball_y = 300