import math

def euclidean_dist(curr_pos, dest_pos):
    if curr_pos==dest_pos:
        return 0
    else:
        print(curr_pos)
        print(dest_pos)
        sum = (curr_pos[0]-dest_pos[0])*(curr_pos[0]-dest_pos[0])+(curr_pos[1]-(dest_pos[1]))*(curr_pos[1]-(dest_pos[1]))
        return math.sqrt(sum)