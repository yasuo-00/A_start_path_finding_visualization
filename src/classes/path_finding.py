import numpy as np
import sys
import time
import pygame
from constants import constants
from numpy.core.fromnumeric import partition
from utils import distance
from classes.node import Node
import painter


class Path_finding:

    def __init__(self):
        self.__graph=np.full((constants.BOARD_SIZE, constants.BOARD_SIZE), None, dtype=np.object)
        self.__open_nodes= list()
        self.__closed_nodes=list()
    
    #initialize graph with board information
    def init_graph(self, board):
        for row in range(constants.BOARD_SIZE):
            for col in range(constants.BOARD_SIZE):
                if board.board_at((row, col))==-1:
                    node = Node((row,col), ntype='Wall')
                elif board.board_at((row, col))==-2:
                    node = Node((row,col),0,distance.euclidean_dist((row,col),board.dest_pos), ntype='Origin')
                elif board.board_at((row, col))==-3:
                    node = Node((row,col),distance.euclidean_dist((row,col),board.origin_pos),0, ntype='dest')
                else:
                    node = Node((row,col))
                self.__graph[row][col]=node
    
    def set_graph_nodes_neighbours(self):
        for row in range(len(self.__graph)):
            for col in range(len(self.__graph[0])):
                if self.__graph[row][col].ntype!='Wall':
                    '''
                    if (row-1)>=0:
                        if self.__graph[row-1][col].ntype!='Wall':
                            self.__graph[row][col].neighbour_list.append(self.__graph[row-1][col])
                    if (row+1<len(self.__graph)):
                        if self.__graph[row+1][col].ntype!='Wall':
                            self.__graph[row][col].neighbour_list.append(self.__graph[row+1][col])
                    if (col-1)>=0:
                        if self.__graph[row][col-1].ntype!='Wall':
                            self.__graph[row][col].neighbour_list.append(self.__graph[row][col-1])
                    if (col+1)<len(self.__graph):
                        if self.__graph[row][col+1].ntype!='Wall':
                            self.__graph[row][col].neighbour_list.append(self.__graph[row][col+1])
                    '''
                    for i in range(row-1,row+2):
                        for j in range(col-1,col+2):
                            if (i)>=0 and (j)>=0 and (i+1)<=len(self.__graph) and (j+1)<=len(self.__graph) and (i,j)!=(row,col):
                                if self.__graph[i][j].ntype!='Wall':
                                    self.__graph[row][col].neighbour_list.append(self.__graph[i][j])        
                    
    
    def find_path(self, board, screen):
        
        dest_node=self.__graph[board.dest_pos[0]][board.dest_pos[1]]
        curr_node=self.__graph[board.origin_pos[0]][board.origin_pos[1]]

        while dest_node not in self.__closed_nodes:
            for node in curr_node.neighbour_list:
                if node is not dest_node and node.pos!= board.origin_pos:
                    board.set_square(curr_node.pos,2)
                    time.sleep(constants.DELAY_TIME)
                    painter.draw_square(screen, node.pos, constants.NEIGHBOUR_COLOR)
                    pygame.display.update()
                
                #if node not expanded (didn't visited all neighbours yet)
                if node not in self.__closed_nodes:
                    #if node not in open_nodes list (not visited)
                    if node not in self.__open_nodes:
                        node.parent_node=curr_node
                        node.g=curr_node.g+1
                        #print(node.g)
                        #node.g=distance.euclidean_dist(node.pos, board.origin_pos)
                        node.h=distance.euclidean_dist(node.pos, board.dest_pos)
                        print(node.h)
                        self.__open_nodes.append(node)
                    #if it was already visited
                    else:
                        g=curr_node.g+1
                        #g=distance.euclidean_dist(node.pos, board.origin_pos)
                        h=distance.euclidean_dist(node.pos, board.dest_pos)
                        if (g+h)<(node.g+node.h):
                            node.parent_node=curr_node
                            node.g=g
                            node.h=h
            
            self.__closed_nodes.append(curr_node)
            #board.set_square(node.pos,1)
            if len(self.__open_nodes)>0:
                self.__open_nodes.sort(key=lambda node: node.g+node.h)
                #for e in self.__open_nodes:
                #    print(e.g+e.h)
                #print('finished sorting')
                curr_node=self.__open_nodes[0]
                self.__open_nodes.pop(0)
                if curr_node is not self.__graph[board.origin_pos[0]][board.origin_pos[1]] and curr_node is not dest_node:
                    board.set_square(curr_node.pos,2)
                    time.sleep(constants.DELAY_TIME)
                    painter.draw_square(screen, curr_node.pos, constants.NEIGHBOUR_COLOR)
                    pygame.display.update()
            else:
                print('No Path Found')
                break
            
        print('finished')

        return dest_node