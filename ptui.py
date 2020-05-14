#setup
import numpy as np

w, h = 7, 6;
board = [[0 for x in range(w)] for y in range(h)]

def main():
    print(board)
    print_board(board)

def print_board(board):
    print(np.matrix(board))



if __name__ == "__main__":
        main()