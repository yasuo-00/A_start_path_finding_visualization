import painter

from utils import distance

#returns last node (destination_node)
def a_star(origin_node, dest_node, board, screen):
    #put origin node on open_nodes_list (first to be expanded)
    open_nodes=list()
    closed_nodes=list()
    open_nodes.append(origin_node)
    open_nodes.sort(key=lambda node: node.g+node.h)
    curr_node=open_nodes[0]
    open_nodes.pop(0)

    #should change board_set_square from function (may not be following SOLID)
    #while dest_node hasn't been chosen to be expanded
    while dest_node not in closed_nodes:
        for node in curr_node.neighbour_list:
            if node is not dest_node and node.pos!= board.origin_pos:                 
                painter.paint_search(screen, node.pos)
            
            #if node not expanded (didn't visited all neighbours yet)
            if node not in closed_nodes:
                #if node not in open_nodes list (not visited)
                if node not in open_nodes:
                    node.parent_node=curr_node
                    node.g=curr_node.g+1
                    #node.g=distance.euclidean_dist(node.pos, board.origin_pos)
                    node.h=distance.euclidean_dist(node.pos, board.dest_pos)
                    open_nodes.append(node)
                #if it was already visited
                else:
                    #if it's on the list update value if new_value<curr_value
                    g=curr_node.g+1
                    #g=distance.euclidean_dist(node.pos, board.origin_pos)
                    h=distance.euclidean_dist(node.pos, board.dest_pos)
                    if (g+h)<(node.g+node.h):
                        node.parent_node=curr_node
                        node.g=g
                        node.h=h
        
        closed_nodes.append(curr_node)
        #board.set_square(node.pos,1)
        #sort open_nodes_list to get nearest node from destination
        open_nodes.sort(key=lambda node: node.g+node.h)
        curr_node=open_nodes[0]
        open_nodes.pop(0)

        #if open_nodes_list is empty == every possible node was searched
        #so there's no possible path between origin and destination point
        if len(open_nodes)==0:
            print('No Path Found')
            break
        
    print('finished')

    return dest_node