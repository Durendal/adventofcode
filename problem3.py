def calculate_move(x, y, right, down, width):
    x = (x + right) % width
    y += down
    return x, y

def count_trees(map, mright, mdown):
    x = y = trees = 0
    height = len(map)
    width = len(map[0])
    for i in range(height):
      x, y = calculate_move(x, y, mright, mdown, width)
      if y < height and map[y][x] == '#':
          trees += 1
    return trees

def main():
    map = [i.strip() for i in open('input3.txt', 'r').readlines()]
    inputs = [(3, 1), (1, 1), (5, 1), (7, 1), (1, 2)]
    product = 1
    for input in inputs:
        trees = count_trees(map, *input)
        product *= trees
        print("Right: %d Down: %d Trees: %d" % (input[0], input[1], trees))
    print("Product: %d" % product)

if __name__ == '__main__':
    main()
