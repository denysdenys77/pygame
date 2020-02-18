import pygame, random, time


class Snake:

    list_of_directions = ['UP', 'DOWN', 'RIGHT', 'LEFT']

    def __init__(self):
        self.body = [[500, 500], [520, 500], [540, 500]]  # [x, y]
        self.direction = 'UP'


    def move_up(self):
        new_head = self.body.pop()
        old_head_x = self.body[0][0]
        old_head_y = self.body[0][1]

        new_head[0] = old_head_x
        new_head[1] = old_head_y - 20
        self.body.insert(0, new_head)

    def move_down(self):
        new_head = self.body.pop()
        old_head_x = self.body[0][0]
        old_head_y = self.body[0][1]

        new_head[0] = old_head_x
        new_head[1] = old_head_y + 20
        self.body.insert(0, new_head)

    def move_right(self):
        new_head = self.body.pop()
        old_head_x = self.body[0][0]
        old_head_y = self.body[0][1]

        new_head[0] = old_head_x + 20
        new_head[1] = old_head_y
        self.body.insert(0, new_head)

    def move_left(self):
        new_head = self.body.pop()
        old_head_x = self.body[0][0]
        old_head_y = self.body[0][1]

        new_head[0] = old_head_x - 20
        new_head[1] = old_head_y
        self.body.insert(0, new_head)

    def check_wall(self):
        if snake.body[0][0] < 0:
            snake.body[0][0] = 980
        if snake.body[0][1] < 0:
            snake.body[0][1] = 980
        if snake.body[0][0] > 1000:
            snake.body[0][0] = 0
        if snake.body[0][1] > 1000:
            snake.body[0][1] = 0

    def add_tail(self):
        """to do before move method"""
        old_tail_x = self.body[-1][0]
        old_tail_y = self.body[-1][1]

        new_tail_x = old_tail_x
        new_tail_y = old_tail_y
        self.body.append([new_tail_x, new_tail_y])


class Apple:

    @staticmethod
    def get_new_position():
        x = random.randrange(0, 500, 20)
        y = random.randrange(0, 500, 20)
        return [x, y]


class Game:

    def run(self, snake, apple):
        pygame.init()
        screen = pygame.display.set_mode((1000, 1000))

        apple_position = apple.get_new_position()

        speed = 0.1

        while True:

            time.sleep(speed)

            # quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            # stop game
            for elem in snake.body[1:]:
                if snake.body[0] == elem:
                    return False

            # apple eating
            if snake.body[0] == apple_position:
                snake.add_tail()
                apple_position = apple.get_new_position()
                # if speed != 0.1:
                #     speed -= 0.01


            # change direction
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] and snake.direction is not 'DOWN':
                snake.direction = 'UP'
            elif keys[pygame.K_DOWN] and snake.direction is not 'UP':
                snake.direction = 'DOWN'
            elif keys[pygame.K_RIGHT] and snake.direction is not 'LEFT':
                snake.direction = 'RIGHT'
            elif keys[pygame.K_LEFT] and snake.direction is not 'RIGHT':
                snake.direction = 'LEFT'

            # moving
            keys = pygame.key.get_pressed()
            if snake.direction is 'UP':
                snake.move_up()
            elif snake.direction is 'DOWN':
                snake.move_down()
            elif snake.direction is 'RIGHT':
                snake.move_right()
            elif snake.direction is 'LEFT':
                snake.move_left()

            snake.check_wall()

            # redraw
            screen.fill((0, 0, 0))
            for elem in snake.body:
                pygame.draw.rect(screen, (255, 255, 255), (elem[0], elem[1], 20, 20))
            pygame.draw.rect(screen, (255, 255, 255), (apple_position[0], apple_position[1], 20, 20))
            pygame.display.update()


if __name__ == '__main__':
    snake = Snake()
    apple = Apple()
    game = Game()

    game.run(snake, apple)




