# -- independent functions, that are used multiple times in different locations --

def objects_overlap(pos_down, pos_up):
    pos1 = [int(i) for i in pos_down]
    pos2 = [int(i) for i in pos_up]
    if pos1[0] == pos2[0] and pos1[1] <= pos2[1]:
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

def update_file(score_num):
    file = open("score.txt", "w")
    file.write("Your current score is: " + str(score_num))
    file.close()

def speed_up(angriness, direction = "right"):
    if direction == "right" and 0 < angriness + 1 < 10: angriness += 1
    if direction == "left" and 0 < angriness - 1 < 10: angriness -= 1
    return(int(angriness))
