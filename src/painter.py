from constants import constants
import pygame

def draw_init_board(screen):

    x=y=0

    for row in range(constants.BOARD_SIZE):
        x+=constants.ROW_WIDTH
        pygame.draw.line(screen, pygame.Color('white'), (x,0),(x,constants.HEIGHT))
    
    for col in range(constants.BOARD_SIZE):
        y+= constants.COL_HEIGHT
        pygame.draw.line(screen, pygame.Color('white'), (0,y),(constants.WIDTH,y))


def draw_square(screen, pos, color):

    pygame.draw.rect(screen, color, [ pos[1]*constants.COL_HEIGHT,pos[0]*constants.ROW_WIDTH, constants.ROW_WIDTH, constants.COL_HEIGHT])