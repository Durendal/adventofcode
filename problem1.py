from operator import mul

def prod(solutions):
    return reduce(mul, solutions, 1)

def check_values(solutions, *args):
    if sum(args) == 2020:
        solutions.extend(args)

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

    for solution_set in sols.items():
        print_results(solution_set[1])

if __name__ == '__main__':
    main()
