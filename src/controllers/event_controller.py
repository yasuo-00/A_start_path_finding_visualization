import pygame
import sys
import painter
from constants import constants
from utils import distance
from classes.path_finding import Path_finding

def event_controller(screen, game):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            #get clicked position
            clicked_x = event.pos[1]//constants.ROW_WIDTH
            clicked_y = event.pos[0]//constants.COL_HEIGHT
            pos=(clicked_x, clicked_y)
            
            if not game.is_origin_set:
                #draw square on the clicked position
                painter.draw_square(screen, pos, constants.ORIGIN_COLOR)
                game.origin_pos=pos
                game.is_origin_set=True

            elif not game.is_destination_set:  
                #draw square on the clicked position
                painter.draw_square(screen, pos, constants.DESTINATION_COLOR)
                game.is_destination_set=True
                game.destination_pos=pos
                dist = distance.euclidean_dist(game.origin_pos, game.destination_pos)
                print(dist)
        
        if pygame.mouse.get_pressed()[0] and game.is_origin_set and game.is_destination_set:
            try:
                clicked_x = event.pos[1]//constants.ROW_WIDTH
                clicked_y = event.pos[0]//constants.COL_HEIGHT
                pos=(clicked_x, clicked_y)

                if not game.is_pos_occupied(pos):
                    painter.draw_square(screen, pos, constants.WALL_COLOR)
                    game.set_wall(pos)
            except AttributeError:
                pass
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_s:
                path_finding = Path_finding(game.origin_pos, game.destination_pos, game.board)
                
                print("start pathing")