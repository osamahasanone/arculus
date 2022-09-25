# arculus

This project uses some python built in libraries such as turtle, tk and argparser. It should run without installing any library.

If it didn't, please run it in a VM.

```
pipenv install
```

To include all paddels in the game:

```
python main.py -l -r -b -t
```

-l = add left paddel

-r = add right paddel

-b = add bottom paddel

-t = add top paddel


To include only left and top paddels:

```
python main.py -l -t
```

To make the ball move randomly after each reset, update the constants file with:

```
BALL_ENABLE_RANDOM_MOVEMENT = True
```


To move left paddel, use q and z

To move right paddel, use o and m

To move bottom paddel, use r and t

To move top paddel, use v and b

