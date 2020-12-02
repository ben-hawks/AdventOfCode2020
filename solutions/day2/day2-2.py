import numpy as np
import re

if __name__ == '__main__':
    in_data = np.loadtxt('../../data/day2/input-p1.txt', dtype=str, delimiter=':')
    valid = 0
    invalid = 0
    for rule, pwd in in_data:
        rule_range = re.findall(r"(\d+)", rule) # get indexes to check
        rule_char = re.findall(r'[a-z]', rule)[0] # get rule char
        pos1 = pwd[int(rule_range[0])] == rule_char
        pos2 = pwd[int(rule_range[1])] == rule_char
        if pos1 ^ pos2: #rule check
            valid += 1
        else:
            invalid += 1
    print('Valid:{}'.format(valid))