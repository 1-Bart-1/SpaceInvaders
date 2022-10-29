
def objects_overlap(pos_down, pos_up):
    pos1 = [int(i) for i in pos_down]
    pos2 = [int(i) for i in pos_up]
    if pos1[0] == pos2[0] and pos1[1] <= pos2[1]:
        print("passed")
        return True
    return False

def list_and_object_overlap(list, pos2):
    for pos1 in list:
        overlapping = objects_overlap(pos1, pos2)
        if overlapping: return True
    return False

def in_bounds(pos):
    if 0 <= pos <= 7:
        return True
    return False