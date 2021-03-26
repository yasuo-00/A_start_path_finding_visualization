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
    screen.fill(constants.BG_COLOR)
    painter.draw_lines(screen)
    pygame.display.update()