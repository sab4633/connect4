#setup
import random

import numpy as np
import pygame
import sys
import math
import time

ROW_COUNT = 6
COL_COUNT = 7

BLUE = (52,194,253)
BLACK = (0,0,0)
RED = (228,52,52)
YELLOW = (251,255,102)

PLAYER = 0
AI = 1

pygame.init()

SQUARESIZE = 100

RADIUS = int(SQUARESIZE/2 - 5)

width = COL_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE

size = (width, height)

screen = pygame.display.set_mode(size)

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
    pygame.display.update()
    draw_board(board)
    while not game_over:
        #print_board(board)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                sys.exit()


            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
                posx = event.pos[0]
                if turn%2 == 0:
                    pygame.draw.circle(screen,RED, (posx, int(SQUARESIZE/2)), RADIUS)
                else:
                    pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE / 2)), RADIUS)
            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
                #ask for p1
                if turn == PLAYER:
                    posx = event.pos[0]
                    col = int(math.floor(posx/SQUARESIZE))
                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 1)
                       # pygame.display.update()
                        draw_board(board)
                        #pygame.display.update()

                        if winning_move(board, 1):
                            print("PLAYER 1 WINS!!!!")
                            game_over = True

                        turn += 1
                        turn %= 2
                        print_board(board)
                        print("updating")
                        draw_board(board)



        #ask for p2
        if turn == AI and not game_over:

            col = random.randint(0, COL_COUNT-1)
            if is_valid_location(board, col):
                time.sleep(1)
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 2)
                draw_board(board)

                if winning_move(board, 2):
                    print("PLAYER 2 WINS!!!!")
                    game_over = True
                print_board(board)
                draw_board(board)


                turn += 1
                turn %= 2

    if game_over:
        #print_board(board)
        draw_board(board)



def create_board():
    board = np.zeros((6,7))
    return board;

def draw_board(board):
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)

    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW,(int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)),RADIUS)

    pygame.display.update()

if __name__ == "__main__":
        main()

