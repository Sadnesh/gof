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
    [0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
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


def isalive(cols: int, rows: int, x: int, y: int, index: int) -> bool:
    global matrix
    new_x = (x + cols + directions[index][0]) % cols
    new_y = (y + rows + directions[index][1]) % rows
    return matrix[new_y][new_x] == 1


def next_step(rows: int, cols: int) -> None:
    global matrix
    new_matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    for y in range(rows):
        for x in range(cols):
            alive = 0
            for index in range(8):
                if isalive(cols, rows, x, y, index):
                    alive += 1

            # if two neighbours alive, then alive
            if matrix[y][x] == 1:
                if alive < 2 or alive > 3:
                    new_matrix[y][x] = 0
                else:
                    new_matrix[y][x] = 1

            # if more alive or less alive, then dead
            else:
                if alive == 3:
                    new_matrix[y][x] = 1

    matrix = new_matrix


def main():
    rows = 9
    cols = 9
    for _ in range(100):
        display(rows, cols)
        next_step(rows, cols)
        time.sleep(0.2)


if __name__ == "__main__":
    main()
