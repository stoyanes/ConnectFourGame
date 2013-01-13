import random
import copy
import sys
import pygame
from constants import *
from functions import *
from pygame.locals import *

def main():
    global DISPLAYSURF, REDPILERECT, BLACKPILERECT, REDTOKENIMG
    global BLACKTOKENIMG, BOARDIMG, ARROWIMG, ARROWRECT, HUMANWINNERIMG
    global COMPUTERWINNERIMG, WINNERRECT, TIEWINNERIMG
    pygame.init()
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
    draw_welcome_mess(DISPLAYSURF)
    user_option = get_start_option(DISPLAYSURF)
    
    if user_option == QUIT_GAME:
        pygame.quit()
        sys.exit()
    
    turn = HUMAN
    main_board = new_board()
    
    while True:
        if turn == HUMAN:
            get_human_move(main_board)
            if is_winner(main_board, RED):
                pygame.quit()
                sys.exit()
            turn = COMPUTER
        else:
            #computer's logic here
            col = get_computer_move(main_board)
            animate_computer_moving(main_board, col)
            make_move(main_board, BLACK, col)
            if is_winner(main_board, BLACK):
                #TODO to be implemented
                #winnerImg = HUMANWINNERIMG
                break;
            turn = HUMAN
        if is_board_full(main_board):
            pass
    while True:
        pygame.quit()
        sys.exit()
       
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
    
def get_human_move(board):
    coord_x, coord_y = None, None
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                coord_x, coord_y = event.pos
            elif event.type == MOUSEBUTTONUP:
                column = int((coord_x - X_DISTANCE) / SPACE_SIZE)
                if is_valid_move(board, column):
                    animate_dropping_token(board, column, RED)
                    board[column][get_lowest_empty_space(board, column)] = RED
                    draw_board(board)
                    pygame.display.update()
                    return
                coord_x, coord_y = None, None
        draw_board(board)
        pygame.display.update()
        


def animate_dropping_token(board, column, color):
    x = X_DISTANCE + column * SPACE_SIZE
    y = Y_DISTANCE - SPACE_SIZE
    drop_speed = 1.0

    lowest_empty_space = get_lowest_empty_space(board, column)

    while True:
        y = y + int(drop_speed)
        drop_speed = drop_speed + 0.5
        if int((y - Y_DISTANCE) / SPACE_SIZE) >= lowest_empty_space:
            return
        draw_board(board, {'x':x, 'y':y, 'color':color})
        pygame.display.update()


def get_computer_move(board):
    moves = get_moves(board, BLACK, DIFFICULTY)
    
    best_move = -1
    for i in range(0, BOARD_WIDTH):
        if moves[i] > best_move and is_valid_move(board, i):
            best_move = moves[i]
    best_moves = []
    for i in range(len(moves)):
        if moves[i] == best_move and is_valid_move(board, i):
            best_moves.append(i)
    return random.choice(best_moves)
    
def get_moves(board, player, depth):
    if depth == 0 or is_board_full(board):
        return [0] * BOARD_WIDTH
        
    if player == RED:
        enemy = BLACK
    else:
        enemy = RED
        
    moves = [0] * BOARD_WIDTH
    for move in range(0, BOARD_WIDTH):
        board_copy = copy.deepcopy(board)
        if not is_valid_move(board_copy, move):
            continue
        make_move(board_copy, player, move)
        if is_winner(board_copy, player):
            moves[move] = 1
            break
        else:
            if is_board_full(board_copy):
                moves[move] = 0
            else:
                for counter_move in range(0, BOARD_WIDTH):
                    board_copy_2 = copy.deepcopy(board_copy)
                    if not is_valid_move(board_copy_2, counter_move):
                        continue
                    make_move(board_copy_2, enemy, counter_move)
                    if is_winner(board_copy_2, enemy):
                        moves[move] = -1
                        break
                    else:
                        result = get_moves(board_copy_2, player, depth - 1)
                        moves[move] += (sum(result) / BOARD_WIDTH) / BOARD_WIDTH
                    
    return moves

def animate_computer_moving(board, column):
    animate_dropping_token(board, column, BLACK)
    

if __name__ == '__main__':
    main()