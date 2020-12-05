# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.

import re


def isrgbcolor(rgb_str_input):
    _rgbstring = re.compile(r'#[a-fA-F0-9]{6}$')
    return bool(_rgbstring.match(rgb_str_input))


def ispid(pid_str_input):
    _pidstring = re.compile(r'[0-9]{9}$')
    return bool(_pidstring.match(pid_str_input))


byr_list = [str(year) for year in range(1920, 2002 + 1)]
iyr_list = [str(year) for year in range(2010, 2020 + 1)]
eyr_list = [str(year) for year in range(2020, 2030 + 1)]
hgt_list = [f'{str(height)}cm' for height in range(150, 193 + 1)]
hgt_list.extend([f'{str(height)}in' for height in range(59, 76 + 1)])

ecl_list = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

input = open('day_4_input', mode='r')

passport = {}
valid = 0

for line in input:
    if len(line) > 1:
        pairs = line.split()
        for pair in pairs:
            info = pair.split(':')
            item, value = info[0], info[1]
            passport[item] = value
    else:
        print(len(passport.keys()), passport.keys())
        if len(passport.keys()) < 7:
            print('<7\n')
            passport = {}
            continue
        if len(passport.keys()) == 7 and 'cid' in passport.keys():
            print('<7\n')
            passport = {}
            continue
        byr = passport['byr']
        iyr = passport['iyr']
        eyr = passport['eyr']
        hgt = passport['hgt']
        ecl = passport['ecl']
        if byr not in byr_list:
            print(f'byr:{byr}\n')
            passport = {}
            continue
        if iyr not in iyr_list:
            print(f'iyr:{iyr}\n')
            passport = {}
            continue
        if eyr not in eyr_list:
            print(f'eyr:{eyr}\n')
            passport = {}
            continue
        if hgt not in hgt_list:
            print(f'hgt:{hgt}\n')
            passport = {}
            continue
        if ecl not in ecl_list:
            print(f'ecl:{ecl}\n')
            passport = {}
            continue
        hcl = passport['hcl']
        pid = passport['pid']
        if not isrgbcolor(hcl):
            print(f'hcl:{hcl}\n')
            passport = {}
            continue
        if not ispid(pid):
            print(f'pid:{pid}\n')
            passport = {}
            continue
        valid += 1
        print('***********\n')
        passport = {}
print(valid)
