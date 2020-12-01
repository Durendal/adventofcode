import operator

def sum(solutions):
    return reduce(operator.add, solutions)

def prod(solutions):
    return reduce(operator.mul, solutions, 1)

def check_values(solutions, *args):
  if sum(args) == 2020:
    solutions.append(args)

def print_results(solutions):
    print "%s = %d" % (" * ".join([str(x) for x in solutions]), prod(solutions))

def main():
    input_data = [int(x.strip()) for x in open("input1.txt", "r").readlines()]

    sols = {
        2: [],
        3: []
    }

    for i in range(len(input_data)):
        for j in range(i, len(input_data)):
            check_values(sols[2], input_data[i], input_data[j])
            for k in range(j, len(input_data)):
                check_values(sols[3], input_data[i], input_data[j], input_data[k])

    for solution in sols[2]:
        print_results(solution)
    for solution in sols[3]:
        print_results(solution)

if __name__ == '__main__':
  main()
