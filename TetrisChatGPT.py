import random
import os
import time
import keyboard

WIDTH = 10
HEIGHT = 20
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 1]],
]

def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in board:
        print(' '.join(map(lambda cell: str(cell) if cell != 2 else '■', row)))

def create_board():
    return [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]

def rotate_shape(shape):
    return [list(row) for row in zip(*shape[::-1])]

def can_move(board, shape, x, y):
    for i in range(len(shape)):
        for j in range(len(shape[i])):
            if shape[i][j] == 1:
                if (
                    x + j < 0
                    or x + j >= WIDTH
                    or y + i >= HEIGHT
                    or board[y + i][x + j] != 0
                ):
                    return False
    return True

def clear_rows(board):
    full_rows = [i for i, row in enumerate(board) if all(cell != 0 for cell in row)]
    for row_idx in full_rows:
        del board[row_idx]
        board.insert(0, [0 for _ in range(WIDTH)])

def main():
    board = create_board()
    current_shape = random.choice(SHAPES)
    x, y = WIDTH // 2 - len(current_shape[0]) // 2, 0
    score = 0

    while True:
        if can_move(board, current_shape, x, y + 1):
            y += 1
        else:
            for i in range(len(current_shape)):
                for j in range(len(current_shape[i])):
                    if current_shape[i][j] == 1:
                        board[y + i][x + j] = 2
            clear_rows(board)
            x, y = WIDTH // 2 - len(current_shape[0]) // 2, 0
            current_shape = random.choice(SHAPES)

        print_board(board)
        print(f"Score: {score}")
        time.sleep(0.5)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("¡Juego terminado!")