from ball import Ball
from paddle import Paddle
from round import Round
from game import Game


if __name__ == '__main__':
    paddle = Paddle()
    ball = Ball()
    this_round = Round()
    game = Game()
    game.run(this_round, paddle, ball)