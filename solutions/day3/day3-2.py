import numpy as np


if __name__ == '__main__':
    in_data = np.loadtxt('../../data/day3/input-p1.txt', dtype=str, comments='*')
    h_pos = 0
    trees = []
    width = len(in_data[0])
    slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
    for slope in slopes:
        tree_cnt = 0
        print('~~~~~~~~~~~~ Slope of {} ~~~~~~~~~~~~'.format(slope))
        h_pos = 0
        for i, line in enumerate(in_data):
            if i % slope[1] == 0:
                if line[h_pos] == '#':
                    tree_cnt += 1
                    pos = line[:h_pos] + "X" + line[h_pos + 1:]
                    print(pos + " HIT! +1, {}".format(tree_cnt))
                else:
                    pos = line[:h_pos] + "O" + line[h_pos + 1:]
                    print(pos)
                h_pos = (h_pos + slope[0]) % width
            else:
                print(line)
        trees.append(tree_cnt)
    print("Tree Cnts: {}".format(trees))
    print("Ans: {}".format((np.prod(trees, dtype=np.double))))
