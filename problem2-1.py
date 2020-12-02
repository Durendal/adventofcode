def parse_input(line):
  info, data = line.split(":")
  min, max = info.split('-')
  max, char = max.split(' ')
  return int(min) <= data.count(char) <= int(max)

def main():
  data = [x.strip() for x in open('input2.txt', 'r').readlines()]
  valid = [i for i in range(len(data)) if parse_input(data[i])]

  #print(valid)
  print("%d valid passwords found" % len(valid))

if __name__ == '__main__':
  main()
