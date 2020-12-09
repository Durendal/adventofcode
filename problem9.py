def part1(data):
    check = 0
    for i in range(25, len(data)):
      previous = data[i-25:i]
      results = [(element, data[i]-element) for element in previous if data[i]-element in previous and data[i] != 2*element]
      if len(results) == 0:
        break
    return data[i]

def part2(data, find):
    check = 0
    for i in range(len(data)):
      if check == find:
        break
      for j in range(i, len(data)):
        check = sum(data[i:j])
        if check >= find:
          break
    return min(data[i:j])+max(data[i:j])

def main():
    data = [int(i.strip()) for i in open("input9.txt", "r").readlines()]
    find = part1(data)
    print(find, part2(data, find))

if __name__ == '__main__':
    main()
