from constants import constants
import numpy as np

#should implement weight for weighted algorithms
class Board:
    def __init__(self):
        self.__is_origin_set = False
        self.__is_dest_set = False
        self.__origin_pos = (0, 0)
        self.__dest_pos = (0, 0)
        self.__board=np.zeros((constants.BOARD_SIZE,constants.BOARD_SIZE))

    @property
    def is_origin_set(self):
        return self.__is_origin_set

    @property
    def is_dest_set(self):
        return self.__is_dest_set

    @property
    def origin_pos(self):
        return self.__origin_pos

    @property
    def dest_pos(self):
        return self.__dest_pos

    @property
    def board(self):
        return self.__board

    @is_origin_set.setter
    def is_origin_set(self, value):
        self.__is_origin_set=value

    @is_dest_set.setter
    def is_dest_set(self,value):
        self.__is_dest_set=value

    @origin_pos.setter
    def origin_pos(self, pos):
        self.__origin_pos=pos
        self.__board[pos[0]][pos[1]]=-2
    
    @dest_pos.setter
    def dest_pos(self, pos):
        self.__dest_pos=pos
        self.__board[pos[0]][pos[1]]=-3

    def set_wall(self,pos):
        if not self.is_pos_occupied(pos):
            self.__board[pos[0]][pos[1]]=-1
    
    def set_visited(self,pos):
        if not self.is_pos_occupied(pos):
            self.__board[pos[0]][pos[1]]=-4

    def is_pos_occupied(self, pos):
        return self.__board[pos[0]][pos[1]] != 0

    def board_at(self,pos):
        return self.__board[pos[0]][pos[1]]

    def set_square(self, pos, value):
        self.__board[pos[0]][pos[1]]=value