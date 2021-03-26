import screen as scr
import pygame

from classes.board import Board
from controllers import event_controller

def main():
    screen = scr.init()
    board= Board()
    use_manhattan_distance=False
    use_diagonal=True
    while True:
        use_manhattan_distance, use_diagonal = event_controller.event_controller(screen, board, use_manhattan_distance, use_diagonal)
        pygame.display.update()

if __name__=='__main__':
    main()