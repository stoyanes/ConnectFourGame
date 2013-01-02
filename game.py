import random
import copy
import sys
import pygame
from constants import *
from functions import *
from pygame.locals import *

def main():
    init_global_vars()
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Connect Four')
    REDPILERECT = pygame.Rect(int(SPACE_SIZE / 2), WINDOW_HEIGHT - int(3 * SPACE_SIZE / 2), SPACE_SIZE, SPACE_SIZE)
    BLACKPILERECT = pygame.Rect(WINDOW_WIDTH - int(3 * SPACESIZE / 2), WINDOW_HEIGHT - int(3 * SPACE_SIZE / 2), SPACE_SIZE, SPACE_SIZE)
    REDTOKENIMG = pygame.image.load('4row_red.png')
    REDTOKENIMG = pygame.transform.smoothscale(REDTOKENIMG, (SPACESIZE, SPACESIZE))
    BLACKTOKENIMG = pygame.image.load('4row_black.png')
    BLACKTOKENIMG = pygame.transform.smoothscale(BLACKTOKENIMG, (SPACESIZE, SPACESIZE))
    BOARDIMG = pygame.image.load('4row_board.png')
    BOARDIMG = pygame.transform.smoothscale(BOARDIMG, (SPACESIZE, SPACESIZE))
if __name__ == '__main__':
    main()