def parse_group(group):
    group = [set(i.strip()) for i in group.split("\r\n") if len(i) > 0]
    return len(set.intersection(*group))

def main():
  data = [i for i in open('input6.txt').read().split("\r\n\r\n")]
  groups = [parse_group(group) for group in data]
  print("Sum: %d" % sum(groups))
  print("Number of groups: %d" % len(groups))

if __name__ == '__main__':
  main()
