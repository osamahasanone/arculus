from ping_pong.moving_object import Paddle, VerticalPaddle, HorizontalPaddle
from ping_pong.enums import TabelSide
from typing import List, Optional
from ping_pong.constants import TABLE_SIDE_LENGTH, PADDLE_SHORT_SIDE, PADDLE_LONG_SIDE


def create_paddles(sides: List[TabelSide]) -> List[Optional[Paddle]]:
    left_paddle = None
    right_paddle = None
    bottom_paddle = None
    top_paddle = None

    for side in sides:
        if side == TabelSide.LEFT:
            left_paddle = VerticalPaddle(
                x=-TABLE_SIDE_LENGTH,
                y=0,
                width=PADDLE_LONG_SIDE,
                length=PADDLE_SHORT_SIDE,
                side=side,
            )
        elif side == TabelSide.RIGHT:
            right_paddle = VerticalPaddle(
                x=TABLE_SIDE_LENGTH,
                y=0,
                width=PADDLE_LONG_SIDE,
                length=PADDLE_SHORT_SIDE,
                side=side,
            )
        elif side == TabelSide.BOTTOM:
            bottom_paddle = HorizontalPaddle(
                x=0,
                y=-TABLE_SIDE_LENGTH,
                width=PADDLE_SHORT_SIDE,
                length=PADDLE_LONG_SIDE,
                side=side,
            )
        elif side == TabelSide.TOP:
            top_paddle = HorizontalPaddle(
                x=0,
                y=TABLE_SIDE_LENGTH,
                width=PADDLE_SHORT_SIDE,
                length=PADDLE_LONG_SIDE,
                side=side,
            )

    return [left_paddle, right_paddle, bottom_paddle, top_paddle]


def link_paddles(
    left_paddle: Paddle, right_paddle: Paddle, bottom_paddle: Paddle, top_paddle: Paddle
) -> None:
    for paddle in (left_paddle, right_paddle):
        if paddle:
            paddle.ahead_neighbour = top_paddle
            paddle.back_neighbour = bottom_paddle
    for paddle in (bottom_paddle, top_paddle):
        if paddle:
            paddle.ahead_neighbour = right_paddle
            paddle.back_neighbour = left_paddle
