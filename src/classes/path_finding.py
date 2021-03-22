import numpy as np
from constants import constants
from utils import distance

class Path_finding:

    def __init__(self, origin_pos, dest_pos, board):
        self.__graph=board
        self.__open_nodes=[]
        self.__closed_nodes=[]
        print(self.__graph)
    

    def set_node_value(self, pos, origin_pos, dest_pos):
        g = distance.euclidean_dist(pos, dest_pos)
        h = distance.euclidean_dist(pos, origin_pos)
        self.__graph[pos[0]][pos[1]]=(g,h)
    
    def find_path(self, origin_pos, dest_pos):
        starting_pos = origin_pos
        curr_pos=starting_pos
        while dest_pos not in self.__closed_nodes:
            for i in range(curr_pos[0]-1, curr_pos[0]+2):
                for j in range(curr_pos[1]-1, curr_pos[1]+2):
                    try:
                        g = distance((i,j),origin_pos)
                        h = distance((i,j),dest_pos)
                        self.__graph[i][j]=(g,h)
                    except:
                        print('failed')