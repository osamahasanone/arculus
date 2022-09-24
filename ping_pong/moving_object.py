import turtle
from ping_pong.constants import (
    TURTLE_DEFAULT_PIXELS,
    TABLE_SIDE_LENGTH,
    BALL_COLOR,
    BALL_SPEED,
    BALL_X_PER_MOVE,
    BALL_Y_PER_MOVE,
    PADDLE_PIXELS_PER_MOVE,
    PADDLE_COLOR,
    PADDLE_SPEED,
    BALL_INITIAL_X,
    BALL_INITIAL_Y,
    SCORE_SKETCH_OFFSET,
    BALL_ENABLE_RANDOM_MOVEMENT,
    BALL_RANDOM_MOVEMENT_X,
    BALL_RANDOM_MOVEMENT_Y,
)
from random import choice


class MovingObject:
    def __init__(self, shape: str, color: str, x: int, y: int, speed: int):
        self.object = turtle.Turtle()
        self.object.speed(speed)
        self.object.shape(shape)
        self.object.color(color)
        self.object.penup()
        self.object.goto(x, y)

    @property
    def x(self) -> int:
        return self.object.xcor()

    @x.setter
    def x(self, value: int) -> None:
        self.object.setx(value)

    @property
    def y(self) -> int:
        return self.object.ycor()

    @y.setter
    def y(self, value: int) -> None:
        self.object.sety(value)


class Ball(MovingObject):
    def __init__(self):
        super(Ball, self).__init__(
            "circle",
            color=BALL_COLOR,
            x=BALL_INITIAL_X,
            y=BALL_INITIAL_Y,
            speed=BALL_SPEED,
        )
        self.x_per_move = BALL_X_PER_MOVE
        self.y_per_move = BALL_Y_PER_MOVE

    def move(self) -> None:
        self.x += self.x_per_move
        self.y += self.y_per_move

    def reset(self) -> None:
        self.x = 0
        self.y = 0
        if BALL_ENABLE_RANDOM_MOVEMENT:
            self.x_per_move = choice(BALL_RANDOM_MOVEMENT_X)
            self.y_per_move = choice(BALL_RANDOM_MOVEMENT_Y)
        else:
            self.x_per_move = BALL_X_PER_MOVE
            self.y_per_move = BALL_Y_PER_MOVE
        print(f"Ball Direction: ({self.x_per_move},{self.y_per_move})")


class Paddle(MovingObject):
    def __init__(self, x, y, width, length, side):
        super(Paddle, self).__init__("square", PADDLE_COLOR, x, y, PADDLE_SPEED)
        self.width = width
        self.length = length
        self.object.shapesize(stretch_wid=width, stretch_len=length)

        self.side = side

        self.ahead_neighbour = None
        self.back_neighbour = None

        self.__score = 0

        # score display
        self.score_sketch = turtle.Turtle()
        self.score_sketch.speed(0)
        self.score_sketch.color("blue")
        self.score_sketch.penup()
        self.score_sketch.hideturtle()
        self.score_sketch.goto(
            x + SCORE_SKETCH_OFFSET[self.side.name]["x"] if x else x,
            y + SCORE_SKETCH_OFFSET[self.side.name]["y"] if y else y,
        )
        self.update_score_sketch()

    def __str__(self) -> str:
        return f"{self.side.name.title()}: {self.__score}"

    @property
    def width_in_pixels(self) -> int:
        return self.width * TURTLE_DEFAULT_PIXELS

    @property
    def length_in_pixels(self) -> int:
        return self.length * TURTLE_DEFAULT_PIXELS

    @property
    def neighbour_offset(self) -> int:
        return (self.width_in_pixels + self.length_in_pixels) / 2

    @property
    def score(self) -> int:
        return self.__score

    def update_score_sketch(self) -> None:
        self.score_sketch.clear()
        self.score_sketch.write(self, align="center", font=("Helvetica", 18, "normal"))

    def decrease_score(self) -> None:
        self.__score -= 1
        self.update_score_sketch()


class VerticalPaddle(Paddle):
    def up(self) -> None:
        new_y = self.y + PADDLE_PIXELS_PER_MOVE
        if (
            self.ahead_neighbour
            and new_y + self.neighbour_offset <= self.ahead_neighbour.y
        ) or (
            not self.ahead_neighbour
            and (new_y + self.neighbour_offset <= TABLE_SIDE_LENGTH)
        ):
            self.y = new_y

    def down(self) -> None:
        new_y = self.y - PADDLE_PIXELS_PER_MOVE
        if (
            self.back_neighbour
            and new_y - self.neighbour_offset >= self.back_neighbour.y
        ) or (
            not self.back_neighbour
            and (new_y - self.neighbour_offset >= -TABLE_SIDE_LENGTH)
        ):
            self.y = new_y


class HorizontalPaddle(Paddle):
    def right(self) -> None:
        new_x = self.x + PADDLE_PIXELS_PER_MOVE
        if (
            self.ahead_neighbour
            and (new_x + self.neighbour_offset <= self.ahead_neighbour.x)
            or (
                not self.ahead_neighbour
                and (new_x + self.neighbour_offset <= TABLE_SIDE_LENGTH)
            )
        ):
            self.x = new_x

    def left(self) -> None:
        new_x = self.x - PADDLE_PIXELS_PER_MOVE
        if (
            self.back_neighbour
            and new_x - self.neighbour_offset >= self.back_neighbour.x
        ) or (
            not self.back_neighbour
            and (new_x - self.neighbour_offset >= -TABLE_SIDE_LENGTH)
        ):
            self.x = new_x
