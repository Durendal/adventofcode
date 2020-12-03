from operator import mul

def calculate_move(coord, slope, width):
    coord['x'] = (coord['x'] + slope['right']) % width
    coord['y'] += slope['down']
    return coord

def count_trees(map, slope, dim):
    coord = {'x': 0, 'y': 0}
    trees = 0
    for i in range(dim['height']):
        coord = calculate_move(coord, slope, dim['width'])
        if (coord['y'] < dim['height']) and (map[coord['y']][coord['x']] == '#'):
            trees += 1
    return trees

def main():
    map = [i.strip() for i in open('input3.txt', 'r').readlines()]
    dim = {'width': len(map[0]), 'height': len(map)}
    slopes = [{'right': i[0], 'down': i[1]} for i in [(int(i), int(j)) for i, j in [tuple(i.strip().split(", ")) for i in open('input3-1.txt', 'r').readlines()]]]
    trees = [count_trees(map, slope, dim) for slope in slopes]
    print('\n'.join(["Right: %d Down: %d Trees: %d" % (slopes[i]['right'], slopes[i]['down'], trees[i]) for i in range(len(trees))]))
    print("Product: %d" % reduce(mul, trees, 1))

if __name__ == '__main__':
    main()
