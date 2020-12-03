def calculate_move(x, y, right, down, width):
    x = (x + right) % width
    y += down
    return x, y

def count_trees(map, mright, mdown):
    x = y = trees = 0
    for i in range(0, len(map)-1):
      x, y = calculate_move(x, y, mright, mdown, len(map[0]))
      if y < len(map) and map[y][x] == '#':
          trees += 1
    print("Right: %d Down: %d Trees: %d" % (mright, mdown, trees))
    return trees

def main():
    map = [i.strip() for i in open('input3.txt', 'r').readlines()]
    inputs = [(3, 1), (1, 1), (5, 1), (7, 1), (1, 2)]
    product = 1
    for input in inputs:
        product *= count_trees(map, *input)

    print("Product: %d" % product)

if __name__ == '__main__':
    main()
