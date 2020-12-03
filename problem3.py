from operator import mul

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
    trees = [count_trees(map, *input) for input in inputs]
    for i in range(len(inputs)):
        print("Right: %d Down: %d Trees: %d" % (inputs[i][0], inputs[i][1], trees[i]))
    print("Product: %d" % reduce(mul, trees, 1))

if __name__ == '__main__':
    main()
