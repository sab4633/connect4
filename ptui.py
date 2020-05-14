#setup
import numpy as np

ROW_COUNT = 6
COL_COUNT = 7

def drop_piece(board,row, col, piece):
    board[row][col] = piece



def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0


def get_next_open_row(board, col):
    for i in range(ROW_COUNT):
        if board[i][col] == 0:
            return i

def print_board(board):
    print(np.flip(board, 0))

def winning_move(board,piece):
    # horizontals
    for c in range(COL_COUNT-3):
        for r in range(ROW_COUNT):
             if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    #Vertical
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT-3):
             if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    #positively sloped
    for c in range(COL_COUNT-3):
        for r in range(ROW_COUNT-3):
             if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    #negatively sloped
    for c in range(COL_COUNT-3):
        for r in range(3, ROW_COUNT):
             if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

def main():
    game_over = False
    board = create_board()

    turn = 0


    while not game_over:
        print_board(board)
        #ask for p1
        if turn ==0:
            col = int(input("Player 1 Marker your selection(0,6):"))
            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 1)

                if winning_move(board, 1):
                    print("PLAYER 1 WINS!!!!")
                    game_over = True
        #ask for p2
        else:
            col = int(input("Player 2 Marker your selection(0,6):"))
            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 2)

                if winning_move(board, 2):
                    print("PLAYER 2 WINS!!!!")
                    game_over = True
        turn += 1
        turn %= 2
    print_board(board)

def create_board():
    board = np.zeros((6,7))
    return board;



if __name__ == "__main__":
        main()