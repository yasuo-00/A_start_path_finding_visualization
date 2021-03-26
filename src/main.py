import screen as scr
import pygame

from classes.board import Board
from controllers import event_controller

def main():
    screen = scr.init()
    board= Board()
    while True:
        event_controller.event_controller(screen, board)
        pygame.display.update()

if __name__=='__main__':
    main()