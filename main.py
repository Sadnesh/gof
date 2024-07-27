"""
Any live cell with fewer than two live neighbours dies, as if by underpopulation.
Any live cell with two or three live neighbours lives on to the next generation.
Any live cell with more than three live neighbours dies, as if by overpopulation.
Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

"""

import os
import time

ALIVE = "⬜"
DEAD = "⬛"

matrix = [
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
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


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def display(rows: int, cols: int) -> None:
    global matrix
    clear_screen()
    for y in range(rows):
        for x in range(cols):
            print(ALIVE if matrix[y][x] else DEAD, end="")
        print()


def next_step():
    global matrix
    print(" i was inside next_step")


def main():
    for _ in range(100):
        display(rows=5, cols=5)
        next_step()
        time.sleep(1)


if __name__ == "__main__":
    main()
