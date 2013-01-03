import pygame
from pygame.locals import *
from constants import *

def new_board():
    board = []
    for i in range(BOARD_WIDTH):
        board.append([EMPTY] * BOARD_HEIGHT)
    return board
    
def get_random_player():
    if random.randint(0, 1) == 0:
        return COMPUTER
    else:
        return HUMAN

def is_board_full(board):
    for i in range(BOARD_WIDTH):
        for j in range(BOARD_HEIGHT):
            if board[i][j] == EMPTY:
                return False
    return True

def get_lowest_empty_space(board, column):
    for y in range(BOARD_HEIGHT-1, -1, -1):
        if board[column][y] == EMPTY:
            return y
    return -1
    

def is_valid_mode(board, column):
    if column < 0 or column >= BOARD_WIDTH or board[column][0] != EMPTY:
        return False
    return True
    
def is_winner(board, tile):
    # check horizontal spaces
    for x in range(BOARD_WIDTH - 3):
        for y in range(BOARD_HEIGHT):
            if board[x][y] == tile and board[x+1][y] == tile and board[x+2][y] == tile and board[x+3][y] == tile:
                return True
    # check vertical spaces
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT - 3):
            if board[x][y] == tile and board[x][y+1] == tile and board[x][y+2] == tile and board[x][y+3] == tile:
                return True
    # check / diagonal spaces
    for x in range(BOARD_WIDTH - 3):
        for y in range(3, BOARD_HEIGHT):
            if board[x][y] == tile and board[x+1][y-1] == tile and board[x+2][y-2] == tile and board[x+3][y-3] == tile:
                return True
    # check \ diagonal spaces
    for x in range(BOARD_WIDTH - 3):
        for y in range(BOARD_HEIGHT - 3):
            if board[x][y] == tile and board[x+1][y+1] == tile and board[x+2][y+2] == tile and board[x+3][y+3] == tile:
                return True
    return False
    
def initial_game_settings():
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Connect Four')