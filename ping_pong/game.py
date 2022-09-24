from ping_pong.moving_object import Ball
from ping_pong.enums import TabelSide
from typing import List, Optional
from ping_pong.helpers import create_paddles, link_paddles
from ping_pong.constants import (
    TABLE_SIDE_LENGTH,
    TURTLE_DEFAULT_PIXELS,
    LEFT_PADDLE_DOWN,
    LEFT_PADDLE_UP,
    RIGHT_PADDLE_DOWN,
    RIGHT_PADDLE_UP,
    BOTTOM_PADDLE_LEFT,
    BOTTOM_PADDLE_RIGHT,
    TOP_PADDLE_LEFT,
    TOP_PADDLE_RIGHT,
)
from ping_pong.table import table


class Game:
    def __init__(self, sides: List[TabelSide]):

        self.paddles = create_paddles(sides)
        link_paddles(*self.paddles)
        (
            self.left_paddle,
            self.right_paddle,
            self.bottom_paddle,
            self.top_paddle,
        ) = self.paddles

        self.ball = Ball()

        self.table = table
        self._init_key_events()

    def _init_key_events(self) -> None:
        self.table.listen()
        if self.left_paddle:
            self.table.onkeypress(self.left_paddle.down, LEFT_PADDLE_DOWN)
            self.table.onkeypress(self.left_paddle.up, LEFT_PADDLE_UP)
        if self.right_paddle:
            self.table.onkeypress(self.right_paddle.down, RIGHT_PADDLE_DOWN)
            self.table.onkeypress(self.right_paddle.up, RIGHT_PADDLE_UP)
        if self.bottom_paddle:
            self.table.onkeypress(self.bottom_paddle.left, BOTTOM_PADDLE_LEFT)
            self.table.onkeypress(self.bottom_paddle.right, BOTTOM_PADDLE_RIGHT)
        if self.top_paddle:
            self.table.onkeypress(self.top_paddle.left, TOP_PADDLE_LEFT)
            self.table.onkeypress(self.top_paddle.right, TOP_PADDLE_RIGHT)

    def get_side_reached(self) -> Optional[TabelSide]:
        if self.ball.x < -TABLE_SIDE_LENGTH - TURTLE_DEFAULT_PIXELS / 2:
            return TabelSide.LEFT
        elif self.ball.x > TABLE_SIDE_LENGTH + TURTLE_DEFAULT_PIXELS / 2:
            return TabelSide.RIGHT
        elif self.ball.y < -TABLE_SIDE_LENGTH - TURTLE_DEFAULT_PIXELS / 2:
            return TabelSide.BOTTOM
        elif self.ball.y > TABLE_SIDE_LENGTH + TURTLE_DEFAULT_PIXELS / 2:
            return TabelSide.TOP

    def update_score(self, side_reached):
        paddle = next(
            (pad for pad in self.paddles if pad and pad.side == side_reached), None
        )
        if paddle:
            paddle.decrease_score()
            print(paddle)
            self.ball.reset()
        else:
            # to understand this condition:  update constants: BALL_X_PER_MOVE = 2, BALL_Y_PER_MOVE = 2, BALL_ENABLE_RANDOM_MOVEMENT = False
            if abs(self.ball.x_per_move) == abs(self.ball.y_per_move):
                self.ball.x_per_move *= -1
                self.ball.y_per_move *= -1
            elif side_reached in (TabelSide.LEFT, TabelSide.RIGHT):
                self.ball.x_per_move *= -1
            else:
                self.ball.y_per_move *= -1

    def vertical_pad_hits(self, paddle):
        ball_paddle_offset = (
            paddle.length_in_pixels / 2 + TURTLE_DEFAULT_PIXELS / 2
        )  # TURTLE_DEFAULT_PIXELS is pixels of ball square container
        hit_start = (
            paddle.x - int(ball_paddle_offset)
            if paddle.side == TabelSide.RIGHT
            else paddle.x - int(ball_paddle_offset)
        )
        hit_end = (
            paddle.x - int(ball_paddle_offset) + 5
            if paddle.side == TabelSide.RIGHT
            else paddle.x + int(ball_paddle_offset) - 5
        )

        if (
            self.ball.x
            in range(
                hit_start,
                hit_end,
            )
            and paddle.y - paddle.width_in_pixels / 2
            < self.ball.y
            < paddle.y + paddle.width_in_pixels / 2
        ):
            self.ball.x_per_move = -self.ball.x_per_move

    def horizontal_pad_hits(self, paddle):
        ball_paddle_offset = (
            paddle.width_in_pixels / 2 + TURTLE_DEFAULT_PIXELS / 2
        )  # TURTLE_DEFAULT_PIXELS is pixels of ball square container
        hit_start = (
            paddle.y - int(ball_paddle_offset)
            if paddle.side == TabelSide.TOP
            else paddle.y - int(ball_paddle_offset)
        )
        hit_end = (
            paddle.y - int(ball_paddle_offset) + 5
            if paddle.side == TabelSide.TOP
            else paddle.y + int(ball_paddle_offset) - 5
        )

        if (
            self.ball.y
            in range(
                hit_start,
                hit_end,
            )
            and paddle.x - paddle.length_in_pixels / 2
            < self.ball.x
            < paddle.x + paddle.length_in_pixels / 2
        ):
            self.ball.y_per_move = -self.ball.y_per_move

    def start(self):

        while True:
            self.table.update()

            self.ball.move()

            side_reached = self.get_side_reached()

            if side_reached:
                self.update_score(side_reached)

            if self.right_paddle:
                self.vertical_pad_hits(self.right_paddle)
            if self.left_paddle:
                self.vertical_pad_hits(self.left_paddle)
            if self.bottom_paddle:
                self.horizontal_pad_hits(self.bottom_paddle)
            if self.top_paddle:
                self.horizontal_pad_hits(self.top_paddle)
