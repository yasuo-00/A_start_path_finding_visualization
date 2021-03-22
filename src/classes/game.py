from sys import setdlopenflags
from constants import constants
import numpy as np
class Game:
    def __init__(self):
        self.__is_origin_set = False
        self.__is_destination_set = False
        self.__origin_pos = (0, 0)
        self.__destination_pos = (0, 0)
        self.__board=np.zeros((constants.BOARD_SIZE,constants.BOARD_SIZE))

    @property
    def is_origin_set(self):
        return self.__is_origin_set

    @property
    def is_destination_set(self):
        return self.__is_destination_set

    @property
    def origin_pos(self):
        return self.__origin_pos

    @property
    def destination_pos(self):
        return self.__destination_pos

    @property
    def board(self):
        return self.__board

    @is_origin_set.setter
    def is_origin_set(self, value):
        self.__is_origin_set=value

    @is_destination_set.setter
    def is_destination_set(self,value):
        self.__is_destination_set=value

    @origin_pos.setter
    def origin_pos(self, pos):
        self.__origin_pos=pos
        self.__board[pos[0]][pos[1]]=-2
    
    @destination_pos.setter
    def destination_pos(self, pos):
        self.__destination_pos=pos
        self.__board[pos[0]][pos[1]]=-3

    def set_wall(self,pos):
        if not self.is_pos_occupied(pos):
            self.__board[pos[0]][pos[1]]=-1

    def is_pos_occupied(self, pos):
        return self.__board[pos[0]][pos[1]] != 0