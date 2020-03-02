import turtle
from math import *

# Fibonacci
from time import sleep


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# Initiate the turtle pen
t = turtle.Pen()
print("Initiated the Turtle pen!")


def draw_fib(num):
    draw_num = num*10

    # Square
    for side in range(4):
        t.forward(draw_num)
        t.right(90)

    # Circle
    for degree in range(90):
        t.forward((2*draw_num*pi)/360) # 5.75 with times 10
        t.right(1)

    # Quart-circle
    # def circfunc(x):
    #     return sqrt((draw_num**2)-(x**2))
    #
    # print("0 - " + str(t.position()))
    # for x in range(draw_num):
    #     x += 1
    #     t.goto(t.position()[0]+1, circfunc(x)-circfunc(1))
    #     print(str(x) + " - " + str(t.position()))
    # t.right(90)


# Reset the turtle
t.reset()
t.speed(10)
t.goto(0, 0)
print("Turtle reset and speed is set!\n\n")

# FIBONACCI
print("Starting Fibonacci...\n")
i = 0
fib_num = None
while True:
    fib_num = fib(i)
    print("Result from Fibonacci iteration " + str(i) + ": " + str(fib_num))
    i += 1
    draw_fib(fib_num)

# Keep window open
# print("Fibonacci done running, keeping window open!")
# turtle.done()
