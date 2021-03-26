from constants import constants
import pygame
import time

def draw_lines(screen):

    x=y=0

    for row in range(constants.BOARD_SIZE):
        x+=constants.ROW_WIDTH
        pygame.draw.line(screen, pygame.Color('white'), (x,0),(x,constants.HEIGHT))
    
    for col in range(constants.BOARD_SIZE):
        y+= constants.COL_HEIGHT
        pygame.draw.line(screen, pygame.Color('white'), (0,y),(constants.WIDTH,y))


def draw_square(screen, pos, color):

    pygame.draw.rect(screen, color, [ pos[1]*constants.COL_HEIGHT,pos[0]*constants.ROW_WIDTH, constants.ROW_WIDTH, constants.COL_HEIGHT])
    draw_lines(screen)

def paint_search(screen, pos, board):
    if not board.is_pos_occupied(pos):
        time.sleep(constants.DELAY_TIME)
        draw_square(screen, pos, constants.NEIGHBOUR_COLOR)
        draw_lines(screen)
        board.set_visited(pos)
        pygame.display.update()

def reset_screen(screen, board):
    for row in range(len(board.board)):
        for col in range(len(board.board)):
            if board.board_at((row,col))==-1 or board.board_at((row,col))==-4:
                board.set_square((row,col),0)
                draw_square(screen,(row,col), constants.BG_COLOR)
    draw_lines(screen)
    print(board.board)
    pygame.display.update()
