from constants import constants
import painter
import pygame

def init():
    pygame.init()

    screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
    pygame.display.set_caption('A* Path Finding Visualization')

    painter.draw_init_board(screen)

    return screen