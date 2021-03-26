import sys
from utils import distance
from numpy.lib.function_base import select


class Node:

    def __init__(self, pos, g=sys.maxsize, h=sys.maxsize, parent_node=None, ntype=''):
        self.__g=g
        self.__h=h
        self.__pos=pos
        self.__ntype=ntype
        self.__parent_node=parent_node
        self.__neighbour_list=[]


    def set_node_value(self, pos, origin_pos, dest_pos):
        g = distance.euclidean_dist(pos, dest_pos)
        h = distance.euclidean_dist(pos, origin_pos)
        self.__g=g
        self.__h=h

    @property
    def g(self):
        return self.__g
    
    @property
    def h(self):
        return self.__h
    
    @property
    def pos(self):
        return self.__pos
    
    @property
    def ntype(self):
        return self.__ntype

    @property
    def parent_node(self):
        return self.__parent_node
    
    @property
    def neighbour_list(self):
        return self.__neighbour_list
    
    @g.setter
    def g(self, value):
        self.__g=value
    
    @h.setter
    def h(self, value):
        self.__h=value

    @parent_node.setter
    def parent_node(self, parent):
        self.__parent_node=parent
    
