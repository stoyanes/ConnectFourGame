import random
import copy
import sys
import pygame
from constants import *
from functions import *
from pygame.locals import *

def main():
    global FPSCLOCK, DISPLAYSURF, REDPILERECT, BLACKPILERECT, REDTOKENIMG
    global BLACKTOKENIMG, BOARDIMG, ARROWIMG, ARROWRECT, HUMANWINNERIMG
    global COMPUTERWINNERIMG, WINNERRECT, TIEWINNERIMG
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Connect Four')
    REDPILERECT = pygame.Rect(int(SPACE_SIZE / 2), WINDOW_HEIGHT - int(3 * SPACE_SIZE / 2), SPACE_SIZE, SPACE_SIZE)
    BLACKPILERECT = pygame.Rect(WINDOW_WIDTH - int(3 * SPACE_SIZE / 2), WINDOW_HEIGHT - int(3 * SPACE_SIZE / 2), SPACE_SIZE, SPACE_SIZE)
    REDTOKENIMG = pygame.image.load('images/red_player.png')
    REDTOKENIMG = pygame.transform.smoothscale(REDTOKENIMG, (SPACE_SIZE, SPACE_SIZE))
    BLACKTOKENIMG = pygame.image.load('images/yellow_player.png')
    BLACKTOKENIMG = pygame.transform.smoothscale(BLACKTOKENIMG, (SPACE_SIZE, SPACE_SIZE))
    BOARDIMG = pygame.image.load('images/board.png')
    BOARDIMG = pygame.transform.smoothscale(BOARDIMG, (SPACE_SIZE, SPACE_SIZE))
    

    
    # TODO loading winner images

    while True:
        run()
    

def run():
    #turn = get_random_player()
    turn = HUMAN
    board = new_board()
    
    while True:
        if turn == HUMAN:
            get_human_move(board)
            if isWinner(mainBoard, RED):
                winnerImg = HUMANWINNERIMG
                break
            turn = COMPUTER
        else:
            pass
        if is_board_full(board):
            pass
    while True:
        #TODO implement the game over logic
        pass
       
def draw_board(board, extra_pars=None):
    DISPLAYSURF.fill(BGCOLOR)
    
    rect = pygame.Rect(0, 0, SPACE_SIZE, SPACE_SIZE)
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            rect.topleft = (X_DISTANCE + (x * SPACE_SIZE), Y_DISTANCE + (y * SPACE_SIZE))
            if board[x][y] == RED:
                DISPLAYSURF.blit(REDTOKENIMG, rect)
            elif board[x][y] == BLACK:
                DISPLAYSURF.blit(BLACKTOKENIMG, rect)
    
    if extra_pars != None:
        if extra_pars['color'] == RED:
            DISPLAYSURF.blit(REDTOKENIMG, (extra_pars['x'], extra_pars['y'], SPACE_SIZE, SPACE_SIZE))
        elif extra_pars['color'] == BLACK:
            DISPLAYSURF.blit(BLACKTOKENIMG, (extra_pars['x'], extra_pars['y'], SPACE_SIZE, SPACE_SIZE))
            
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_WIDTH):
            rect.topleft = (X_DISTANCE + (x * SPACE_SIZE), Y_DISTANCE + (y * SPACE_SIZE))
            DISPLAYSURF.blit(BOARDIMG, rect)
    
    DISPLAYSURF.blit(REDTOKENIMG, REDPILERECT) # red on the left
    DISPLAYSURF.blit(BLACKTOKENIMG, BLACKPILERECT) # black on the right
    
def get_human_move(board):
    draggingToken = False
    tokenx, tokeny = None, None
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN and not draggingToken and REDPILERECT.collidepoint(event.pos):
                draggingToken = True
                tokenx, tokeny = event.pos
            elif event.type == MOUSEMOTION and draggingToken:
                tokenx, tokeny = event.pos
            elif event.type == MOUSEBUTTONUP and draggingToken:
                # let go of the token being dragged
                if tokeny < Y_DISTANCE and tokenx > X_DISTANCE and tokenx < WINDOW_WIDTH - X_DISTANCE:
                    # let go at the top of the screen.
                    column = int((tokenx - X_DISTANCE) / SPACE_SIZE)
                    if isValidMove(board, column):
                        animateDroppingToken(board, column, RED)
                        board[column][getLowestEmptySpace(board, column)] = RED
                        draw_board(board)
                        pygame.display.update()
                        return
                tokenx, tokeny = None, None
                draggingToken = False
        if tokenx != None and tokeny != None:
            draw_board(board, {'x':tokenx - int(SPACE_SIZE / 2), 'y':tokeny - int(SPACE_SIZE / 2), 'color':RED})
        else:
            draw_board(board)

        pygame.display.update()
        FPSCLOCK.tick()
    
if __name__ == '__main__':
    main()