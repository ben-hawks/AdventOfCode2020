import numpy as np


if __name__ == '__main__':
    in_data = np.loadtxt('../../data/day3/input-p1.txt', dtype=str, comments='*')
    h_pos = 0
    trees = 0
    width = len(in_data[0])
    for i, line in enumerate(in_data):
        if line[h_pos] == '#':
            trees +=1
            pos = line[:h_pos] + "X" + line[h_pos + 1:]
            print(pos + " HIT! +1, {}".format(trees))
        else:
            pos = line[:h_pos] + "O" + line[h_pos + 1:]
            print(pos)
        h_pos = (h_pos +3) % width
        #print(h_pos)
    print(trees)