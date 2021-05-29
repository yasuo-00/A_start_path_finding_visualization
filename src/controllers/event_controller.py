import pygame
import sys
import painter
import screen as scr
from constants import constants
from utils import distance
from classes.graph import Graph


def event_controller(screen, board, use_manhattan_distance, use_diagonal):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # get clicked position
            clicked_x = event.pos[1]//constants.ROW_WIDTH
            clicked_y = event.pos[0]//constants.COL_HEIGHT
            pos = (clicked_x, clicked_y)

            if not board.is_origin_set:
                # draw square on the clicked position
                painter.draw_square(screen, pos, constants.ORIGIN_COLOR)
                board.origin_pos = pos
                board.is_origin_set = True

            elif not board.is_dest_set:
                # draw square on the clicked position
                painter.draw_square(screen, pos, constants.DEST_COLOR)
                board.is_dest_set = True
                board.dest_pos = pos
                dist = distance.euclidean_dist(
                    board.origin_pos, board.dest_pos)
                print(dist)

        if pygame.mouse.get_pressed()[0] and board.is_origin_set and board.is_dest_set:
            try:
                clicked_x = event.pos[1]//constants.ROW_WIDTH
                clicked_y = event.pos[0]//constants.COL_HEIGHT
                pos = (clicked_x, clicked_y)

                if board.board_at(pos) == 0:
                    painter.draw_square(screen, pos, constants.WALL_COLOR)
                    painter.draw_lines(screen)
                    board.set_wall(pos)
            except AttributeError:
                pass
        if event.type == pygame.KEYDOWN:
            # reset board (won't reset during any algorithm execution)
            if event.key == pygame.K_r:
                board.reset()
                scr.reset_screen(screen, board)

            # press 'a' to start A* algorithm
            elif event.key == pygame.K_a:
                graph = Graph()
                graph.init_graph(board)
                graph.set_graph_nodes_neighbours(use_diagonal)
                print("start pathing")
                dest = graph.find_path(board, screen, 'A*', use_manhattan_distance)
                dest = dest.parent_node
                if dest is None:
                    print('No Path Found')
                    break
                print(dest.pos)

                while(dest.parent_node is not None):
                    painter.draw_square(screen, dest.pos, constants.PATH_COLOR)
                    dest = dest.parent_node

            # press 'd' to start DFS algorithm
            elif event.key == pygame.K_d:
                graph = Graph()
                graph.init_graph(board)
                graph.set_graph_nodes_neighbours(use_diagonal)
                print("start pathing")
                dest = graph.find_path(board, screen, 'DFS', use_manhattan_distance)
                dest = dest.parent_node
                print('Final node')
                if dest is None:
                    print('No Path Found')
                    break
                print(dest.pos)
                

                # print path (from dest to origin)
                while(dest.parent_node is not None):
                    painter.draw_square(screen, dest.pos, constants.PATH_COLOR)
                    dest = dest.parent_node

            # press 'b' to start BFS algorithm
            elif event.key == pygame.K_b:
                graph = Graph()
                graph.init_graph(board)
                graph.set_graph_nodes_neighbours(use_diagonal)
                print("start pathing")
                dest = graph.find_path(board, screen, 'BFS', use_manhattan_distance)
                dest = dest.parent_node
                print('Final node')
                if dest is None:
                    print('No Path Found')
                    break
                
                print(dest.pos)

                while(dest.parent_node is not None):
                    painter.draw_square(screen, dest.pos, constants.PATH_COLOR)
                    dest = dest.parent_node
            
            #set heuristic to manhattan distance
            elif event.key == pygame.K_m:
                use_manhattan_distance=True
                print('Using manhattan distance')

            #set heuristic to euclidean distance
            elif event.key == pygame.K_e:
                use_manhattan_distance=False
                print('Using euclidean distance')
            
            #enable/disable diagonal move
            elif event.key == pygame.K_g:
                use_diagonal^= True
                print(use_diagonal)
    return use_manhattan_distance, use_diagonal