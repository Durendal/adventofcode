def parse_input(line):
  info, data = line.split(": ")
  pos1, tail = info.split('-')
  pos2, char = tail.split(' ')
  positions = [pos+1 for pos, c in enumerate(data) if c == char]
  check = [int(pos1), int(pos2)]

  return len(set.intersection(set(check), set(positions))) == 1

def main():
  data = [x.strip() for x in open('input2.txt', 'r').readlines()]
  valid = [i for i in range(len(data)) if parse_input(data[i])]

  print("%d valid passwords found" % len(valid))

if __name__ == '__main__':
  main()
