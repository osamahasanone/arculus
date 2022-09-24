# core
TURTLE_DEFAULT_PIXELS = 20

# table
TABLE_SIDE_LENGTH = 400
TABLE_TITLE = "Ping Pong"
TABLE_BG_COLOR = "lightgray"
TABLE_BORDER_SIZE = 4

# ball
BALL_COLOR = "orange"
BALL_SPEED = 6  # normal
BALL_INITIAL_X = 0
BALL_INITIAL_Y = 0
BALL_X_PER_MOVE = 3
BALL_Y_PER_MOVE = 2
BALL_ENABLE_RANDOM_MOVEMENT = False

# zero excluded below. Otherwise, ball will stick at point (0,0) or keep moving between two facing paddels
# => [-3, -2, -1, 1, 2, 3]
BALL_RANDOM_MOVEMENT_X = list(range(-3, 4))  # has effect on x_per_move
BALL_RANDOM_MOVEMENT_X.remove(0)
BALL_RANDOM_MOVEMENT_Y = list(range(-3, 4))  # hass effect on y_per_move
BALL_RANDOM_MOVEMENT_Y.remove(0)

# paddel
PADDLE_SHORT_SIDE = 2  # 40 px
PADDLE_LONG_SIDE = 4  # 80 px
PADDLE_PIXELS_PER_MOVE = 10
PADDLE_COLOR = "black"
PADDLE_SPEED = 0  # fastest

LEFT_PADDLE_DOWN = "z"
LEFT_PADDLE_UP = "q"

RIGHT_PADDLE_DOWN = "m"
RIGHT_PADDLE_UP = "o"

BOTTOM_PADDLE_LEFT = "v"
BOTTOM_PADDLE_RIGHT = "b"

TOP_PADDLE_LEFT = "r"
TOP_PADDLE_RIGHT = "t"

# score
SCORE_SKETCH_OFFSET = {
    "LEFT": {"x": -70, "y": 0},
    "RIGHT": {"x": 75, "y": 0},
    "BOTTOM": {
        "x": 0,
        "y": -60,
    },
    "TOP": {
        "x": 0,
        "y": 30,
    },
}
