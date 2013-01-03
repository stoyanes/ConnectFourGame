from constants import *

#def init_global_vars():
    #global FPSCLOCK, DISPLAYSURF, REDPILERECT, BLACKPILERECT, REDTOKENIMG
    #global BLACKTOKENIMG, BOARDIMG, ARROWIMG, ARROWRECT, HUMANWINNERIMG
    #global COMPUTERWINNERIMG, WINNERRECT, TIEWINNERIMG
    
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
    
