def main():
  groups = [len(set.intersection(*[set(i.strip()) for i in group.split("\r\n") if len(i) > 0])) for group in [i for i in open('input6.txt').read().split("\r\n\r\n")]]
  print("Sum: %d" % sum(groups))

if __name__ == '__main__':
  main()
