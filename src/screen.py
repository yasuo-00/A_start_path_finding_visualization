from constants import constants
import painter
import pygame

def init():
    pygame.init()

    screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
    pygame.display.set_caption('A* Path Finding Visualization')
    screen.fill(constants.BG_COLOR)
    painter.draw_lines(screen)

    return screen


def reset_screen(screen, board):
    for row in range(len(board.board)):
        for col in range(len(board.board)):
            if board.board_at((row,col))==-1 or board.board_at((row,col))==-4:
                board.set_square((row,col),0)
                painter.draw_square(screen,(row,col), constants.BG_COLOR)
    painter.draw_lines(screen)
    pygame.display.update()