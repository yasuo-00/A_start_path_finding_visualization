import screen as scr
import pygame

from classes.game import Game
from controllers import event_controller

def main():
    screen = scr.init()
    game= Game()
    while True:
        event_controller.event_controller(screen, game)
        pygame.display.update()

if __name__=='__main__':
    main()