import numpy as np
import re

if __name__ == '__main__':
    in_data = np.loadtxt('../../data/day2/input-p1.txt', dtype=str, delimiter=':')
    valid = 0
    invalid = 0
    for rule, pwd in in_data:
        rule_range = re.findall(r"(\d+)", rule) # get min and max counts
        rule_char = re.findall(r'[a-z]', rule)[0] # get rule char
        if int(rule_range[0]) <= pwd.count(rule_char) <= int(rule_range[1]): #rule check
            valid += 1
        else:
            invalid += 1
    print('Valid:{} \n Invalid:{}'.format(valid, invalid))