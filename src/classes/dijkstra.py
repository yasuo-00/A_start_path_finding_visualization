import numpy as np
import sys
import time
import pygame
from constants import constants
from numpy.core.fromnumeric import partition
from utils import distance
from classes.node import Node
import painter

def find_path(self, origin_pos, dest_pos, board, screen):
        
        dest_node=self.__graph[dest_pos[0]][dest_pos[1]]
        curr_node=self.__graph[origin_pos[0]][origin_pos[1]]

        while dest_node not in self.__closed_nodes:
            for node in curr_node.neighbour_list:
                #if node not expanded (didn't visited all neighbours yet)
                if node not in self.__closed_nodes:
                    #if node not in open_nodes list (not visited)
                    if node not in self.__open_nodes:
                        node.parent_node=curr_node
                        node.g=curr_node.g+1
                        #node.g=distance.euclidean_dist(node.pos, origin_pos)
                        node.h=distance.euclidean_dist(node.pos, dest_pos)
                        self.__open_nodes.append(node)
                    #if it was already visited
                    else:
                        g=curr_node.g+1
                        #g=distance.euclidean_dist(node.pos, origin_pos)
                        h=distance.euclidean_dist(node.pos, dest_pos)
                        if (g+h)<(node.g+node.h):
                            node.parent_node=curr_node
                            node.g=g
                            node.h=h
            
            self.__closed_nodes.append(curr_node)
            if curr_node is not self.__graph[origin_pos[0]][origin_pos[1]] and curr_node is not dest_node:
                board.set_square(curr_node.pos,2)
                time.sleep(1)
                painter.draw_square(screen, curr_node.pos, constants.NEIGHBOUR_COLOR)
                pygame.display.update()
            #board.set_square(node.pos,1)
            if len(self.__open_nodes)>0:
                self.__open_nodes.sort(key=lambda node: node.g+node.h, reverse=True)
                curr_node=self.__open_nodes[0]
                self.__open_nodes.pop(0)
            else:
                print('No Path Found')
                break
            
        print('finished')

        return dest_node