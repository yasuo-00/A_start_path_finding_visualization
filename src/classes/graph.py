import numpy as np
import sys
import time
import pygame
from constants import constants
from numpy.core.fromnumeric import partition
from utils import distance
from classes.node import Node
import painter
from search_algorithm import a_star

#need to implement weight (should be on board.py)

class Graph:

    def __init__(self):
        self.__graph=np.full((constants.BOARD_SIZE, constants.BOARD_SIZE), None, dtype=np.object)
    
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
    
    #set graph nodes neighbours and if they can access diagonal nodes
    def set_graph_nodes_neighbours(self, enable_diagonal):
        for row in range(len(self.__graph)):
            for col in range(len(self.__graph[0])):
                if self.__graph[row][col].ntype!='Wall':
                    if enable_diagonal:
                        for i in range(row-1,row+2):
                            for j in range(col-1,col+2):
                                if (i)>=0 and (j)>=0 and (i+1)<=len(self.__graph) and (j+1)<=len(self.__graph) and (i,j)!=(row,col):
                                    if self.__graph[i][j].ntype!='Wall':
                                        self.__graph[row][col].neighbour_list.append(self.__graph[i][j])  
                    else:
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
    
    def find_path(self, board, screen, algorithm):
        origin_node=self.__graph[board.origin_pos[0]][board.origin_pos[1]]
        dest_node = self.__graph[board.dest_pos[0]][board.dest_pos[1]]
        
        if algorithm=='A*':
            dest_path = a_star.a_star(origin_node, dest_node, board, screen)
        

        return dest_path