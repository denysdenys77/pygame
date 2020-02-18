from paddle import Paddle
from ball import Ball
from single_pong_game import SingleGame

paddle = Paddle
ball = Ball
game = SingleGame

game.run(paddle, ball)