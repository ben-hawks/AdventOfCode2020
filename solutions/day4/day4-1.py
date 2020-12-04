if __name__ == '__main__':
    valid = 0
    with open('../../data/day4/input-p1.txt') as in_data:
        passports = in_data.read().split('\n\n')
        for entry in passports:
            entry = entry.replace('\n', ' ')
            fields = entry.split(' ')
            if 'cid' not in entry:
                if len(fields) == 7:
                    valid += 1
            elif len(fields) ==8:
                valid += 1
    print(valid)