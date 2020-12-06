def parse_group(group):
    group = set(group.replace("\r\n", ""))
    return len(group)

def main():
  data = [i for i in open('input6.txt').read().split("\r\n\r\n")]
  groups = [parse_group(group) for group in data]
  print("Sum: %d" % sum(groups))
  print("Number of groups: %d" % len(data))

if __name__ == '__main__':
  main()