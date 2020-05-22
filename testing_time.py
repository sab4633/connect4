import time
import pygame

print("haha left your computer on")
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
width = COL_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE

size = (width, height)

screen = pygame.display.set_mode(size)
pygame.display.update()
time.sleep(1)
print("lol jk")

