"""
Any live cell with fewer than two live neighbours dies, as if by underpopulation.
Any live cell with two or three live neighbours lives on to the next generation.
Any live cell with more than three live neighbours dies, as if by overpopulation.
Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

"""

import time

ALIVE = "⬜"
DEAD = "⬛"

matrix = [
    ["0", "0", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "0", "0"],
]
directions = [
    [0, -1],
    [0, 1],
    [1, 1],
    [1, 0],
    [1, -1],
    [-1, 1],
    [-1, 0],
    [-1, -1],
]


def display(): ...


def nextstate(x, y):
    count = 0

    print(count)


def main():
    global matrix
    for x, outer in enumerate(matrix):
        for y, inner in enumerate(outer):
            if 0 < x < len(matrix) and 0 < y < len(outer):
                nextstate(x, y)
                time.sleep(2)


if __name__ == "__main__":
    main()
