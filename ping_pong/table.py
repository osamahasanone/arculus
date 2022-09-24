import turtle

from ping_pong.constants import (
    TABLE_SIDE_LENGTH,
    TABLE_TITLE,
    TABLE_BG_COLOR,
    TABLE_BORDER_SIZE,
)

# init main screen
table = turtle.Screen()
table.title(TABLE_TITLE)
table.bgcolor(TABLE_BG_COLOR)
table.setup(width=1.0, height=1.0)  # full screen

# draw borders
border_pen = turtle.Turtle()
border_pen.penup()
border_pen.setposition(-TABLE_SIDE_LENGTH, -TABLE_SIDE_LENGTH)
border_pen.pendown()
border_pen.pensize(TABLE_BORDER_SIZE)
for side in range(4):
    border_pen.forward(TABLE_SIDE_LENGTH * 2)
    border_pen.left(90)
border_pen.hideturtle()
