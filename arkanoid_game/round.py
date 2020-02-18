
class Round:

    def __init__(self):
        self.set = None

    def create_first_round(self):
        round = []
        y = 0
        level = 1
        while level is not 4:
            if level % 2 == 0:
                list_of_x = list(range(60, 600, 120))
                for x in list_of_x:
                    new_block_pos = (x, y)
                    round.append(new_block_pos)
                y += 40
                level += 1
            else:
                list_of_x = list(range(0, 600, 120))
                for x in list_of_x:
                    new_block_pos = (x, y)
                    round.append(new_block_pos)
                y += 40
                level += 1
        self.set = round

    def create_second_round(self):
        round = []
        y = 0
        level = 1
        while level is not 6:
            if level % 2 == 0:
                list_of_x = list(range(60, 600, 120))
                for x in list_of_x:
                    new_block_pos = (x, y)
                    round.append(new_block_pos)
                y += 40
                level += 1
            else:
                list_of_x = list(range(0, 600, 120))
                for x in list_of_x:
                    new_block_pos = (x, y)
                    round.append(new_block_pos)
                y += 40
                level += 1
        self.set = round

    def create_third_round(self):
        round = []
        y = 0
        level = 1
        while level is not 6:
            list_of_x = list(range(0, 600, 60))
            for x in list_of_x:
                new_block_pos = (x, y)
                round.append(new_block_pos)
            y += 40
            level += 1
        self.set = round

    def del_block(self, block):
        for in_block in self.set:
            if in_block[0] == block[0] and in_block[1] == block[1]:
                self.set.remove(in_block)

    def check_ball_contact(self, ball):
        for block in self.set:
            if ball.ball_y + ball.ball_radius == block[1] + 40 and ball.ball_x in range(block[0], block[0] + 60) and ball.ball_direction == 'move_up_and_left':
                ball.ball_direction = 'move_down_and_left'
                self.del_block(block)
            elif ball.ball_y + ball.ball_radius == block[1] + 40 and ball.ball_x in range(block[0], block[0] + 60) and ball.ball_direction == 'move_up_and_right':
                ball.ball_direction = 'move_down_and_right'
                self.del_block(block)

            elif ball.ball_x + ball.ball_radius == block[0] and ball.ball_y in range(block[1], block[1] + 40) and ball.ball_direction is 'move_up_and_right':
                ball.ball_direction = 'move_up_and_left'
                self.del_block(block)
            elif ball.ball_x + ball.ball_radius == block[0] + 60 and ball.ball_y in range(block[1], block[1] + 40) and ball.ball_direction is 'move_up_and_left':
                ball.ball_direction = 'move_up_and_right'
                self.del_block(block)

            elif ball.ball_x + ball.ball_radius == block[0] and ball.ball_y in range(block[1], block[1] + 40) and ball.ball_direction is 'move_down_and_right':
                ball.ball_direction = 'move_down_and_left'
                self.del_block(block)
            elif ball.ball_x + ball.ball_radius == block[0] + 60 and ball.ball_y in range(block[1], block[1] + 40) and ball.ball_direction is 'move_down_and_left':
                ball.ball_direction = 'move_down_and_right'
                self.del_block(block)

            elif ball.ball_y + ball.ball_radius == block[1] and ball.ball_x in range(block[0], block[0] + 60) and ball.ball_direction is 'move_down_and_right':
                ball.ball_direction = 'move_up_and_right'
                self.del_block(block)
            elif ball.ball_y + ball.ball_radius == block[1] and ball.ball_x in range(block[0], block[0] + 60) and ball.ball_direction is 'move_down_and_left':
                ball.ball_direction = 'move_up_and_left'
                self.del_block(block)