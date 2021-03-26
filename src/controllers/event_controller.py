import pygame
import sys
import painter
from constants import constants
from utils import distance
from classes.path_finding import Path_finding

def event_controller(screen, board):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            #get clicked position
            clicked_x = event.pos[1]//constants.ROW_WIDTH
            clicked_y = event.pos[0]//constants.COL_HEIGHT
            pos=(clicked_x, clicked_y)
            
            if not board.is_origin_set:
                #draw square on the clicked position
                painter.draw_square(screen, pos, constants.ORIGIN_COLOR)
                board.origin_pos=pos
                board.is_origin_set=True

            elif not board.is_dest_set:  
                #draw square on the clicked position
                painter.draw_square(screen, pos, constants.dest_COLOR)
                board.is_dest_set=True
                board.dest_pos=pos
                dist = distance.euclidean_dist(board.origin_pos, board.dest_pos)
                print(dist)
        
        if pygame.mouse.get_pressed()[0] and board.is_origin_set and board.is_dest_set:
            try:
                clicked_x = event.pos[1]//constants.ROW_WIDTH
                clicked_y = event.pos[0]//constants.COL_HEIGHT
                pos=(clicked_x, clicked_y)

                if not board.is_pos_occupied(pos):
                    painter.draw_square(screen, pos, constants.WALL_COLOR)
                    board.set_wall(pos)
            except AttributeError:
                pass
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_s:
                path_finding = Path_finding()
                path_finding.init_graph(board)
                path_finding.set_graph_nodes_neighbours()
                print("start pathing")
                dest = path_finding.find_path(board.origin_pos, board.dest_pos)

                dest = dest.parent_node
                print(dest.pos)

                while(dest.parent_node is not None):
                    painter.draw_square(screen, dest.pos,constants.VISITED_COLOR)
                    dest = dest.parent_node