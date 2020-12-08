def parse_instruction(instruction):
    opcode, val = instruction.split(" ")
    return {'opcode': opcode, 'value': int(val)}

def main():
    instructions = [i.strip() for i in open('input8.txt', 'r').readlines()]

    instruction_pointer = 0
    accumulator = 0
    history = []

    while True:
        inst = parse_instruction(instructions[instruction_pointer])

        if instruction_pointer in history:
            break
        history.append(instruction_pointer)
        #print("Opcode: %s Value: %s IP: %d ACC: %d" % (inst['opcode'], inst['value'], instruction_pointer, accumulator))
        if inst['opcode'] == 'acc':
            accumulator += inst['value']
            instruction_pointer += 1
        elif inst['opcode'] == 'jmp':
            instruction_pointer += inst['value']
        elif inst['opcode'] == 'nop':
            instruction_pointer += 1
    print(accumulator)
if __name__ == '__main__':
    main()
