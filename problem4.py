def valid_birth(year):
  return 1920 <= int(year) <= 2002

def valid_issue_year(year):
  return 2010 <= int(year) <= 2020

def valid_expiration_year(year):
  return 2020 <= int(year) <= 2030

def valid_height(height):
    if height[-2:] == 'cm':
        return 150 <= int(height[:-2]) <= 193
    elif height[-2:] == 'in':
        return 59 <= int(height[:-2]) <= 76
    else:
        return False

def valid_hair_colour(colour):
    if len(colour) != 7 or colour[0] != '#':
        return False
    return all([x in '0123456789ABCDEFabcdef' for x in colour[1:]])

def valid_eye_colour(colour):
    return len(colour) == 3 and colour in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def valid_pid(pid):
    return all([x in '0123456789' for x in pid]) and len(pid) == 9

def valid_cid(cid):
    return True

def valid_keys(keys, check_keys):
    for key in check_keys:
        if key not in keys:
            return False
    return True

def parse_passport(passport):
    checks = {
        'byr': valid_birth,
        'iyr': valid_issue_year,
        'eyr': valid_expiration_year,
        'hgt': valid_height,
        'hcl': valid_hair_colour,
        'ecl': valid_eye_colour,
        'pid': valid_pid,
        'cid': valid_cid,
    }
    passport = ' '.join(passport.split("\r\n")).split(" ")
    pairs = [(i.split(':')[0], i.split(':')[1]) for i in passport if len(i) > 1]
    if not valid_keys([i[0] for i in pairs], [i for i in checks.keys() if i != 'cid']):
        return False
    for pair in pairs:
        if checks[pair[0]](pair[1]) == False:
            return False
    return True

def main():
  passports = open('input4.txt', 'r').read().split("\r\n\r\n")
  valid_passports = [i for i in [parse_passport(passport) for passport in passports] if i == True]
  print("Valid Passports: %d" % len(valid_passports))

if __name__ == '__main__':
  main()
