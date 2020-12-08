def parse_instruction(instruction):
    opcode, val = instruction.split(" ")
    return {'opcode': opcode, 'value': int(val)}

def test_run(index, substitution):
    instructions = [i.strip() for i in open('input8.txt', 'r').readlines()]
    instructions[index] = substitution +" "+ instructions[index].split(" ")[1]
    instruction_pointer = accumulator = 0
    history = []
    for i in range(250):
        if instruction_pointer >= len(instructions):
            break
        inst = parse_instruction(instructions[instruction_pointer])

        #print("%d Opcode: %s Value: %s IP: %d ACC: %d" % (i, inst['opcode'], inst['value'], instruction_pointer, accumulator))
        if inst['opcode'] == 'acc':
            accumulator += inst['value']
            instruction_pointer += 1
        elif inst['opcode'] == 'jmp':
            instruction_pointer += inst['value']
        elif inst['opcode'] == 'nop':
            instruction_pointer += 1

    return (accumulator, i, instruction_pointer)

def main():
    instructions = enumerate([i.strip() for i in open('input8.txt', 'r').readlines()])
    jmp_instructions = [i for i, x in instructions if x.split(" ")[0] == 'jmp']
    nop_instructions = [i for i, x in instructions if x.split(" ")[0] == 'nop']
    results = [test_run(jmp, 'nop') for jmp in jmp_instructions]
    results.extend([test_run(nop, 'jmp') for nop in nop_instructions])
    print([(result[0],result[2]) for result in results if result[1] != 250 and result[2] == 605])

if __name__ == '__main__':
    main()
