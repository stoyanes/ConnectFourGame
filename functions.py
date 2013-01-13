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
    

def is_valid_move(board, column):
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

def make_move(board, player, column):
    low = get_lowest_empty_space(board, column)
    if low != -1:
        board[column][low] = player
    
def draw_welcome_mess(screen):
        image = pygame.image.load('images/connect-four.png')
        screen.blit(image, (0, 0))
        pygame.display.flip()
        pygame.time.wait(2000)
        
def get_start_option(screen):
    image = pygame.image.load('images/connect-four-choice.png')
    screen.blit(image, (0, 0))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_s:
                return START_GAME
            if event.type == KEYDOWN and event.key == K_q:
                return QUIT_GAME
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        