def main():
  groups = [len(set(group.replace("\r\n", ""))) for group in [i for i in open('input6.txt').read().split("\r\n\r\n")]]
  print("Sum: %d" % sum(groups))

if __name__ == '__main__':
  main()
