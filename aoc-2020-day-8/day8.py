# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% Read input

with open("input.txt", "r") as input_file:
    inp = input_file.read().strip().split('\n') 

# %% Parse input
ops, args = [], []

for line in inp:
    a, b = line.split()
    ops.append(a)
    args.append(int(b))

# %% Functions

def acc(accumulator, value):
    accumulator = accumulator + value
    return accumulator

def jmp(pointer, value):
    pointer = pointer + value
    return pointer

def nop():
    return
# %% Read instructions

def read_instruction(pointer, operation, argument, accumulator):
    if operation != 'jmp': # increment pointer
        pointer += 1
    # operations
    if operation == 'acc':
        return acc(accumulator, argument), pointer
    elif operation == 'jmp':
        return accumulator, jmp(pointer, argument)
    elif operation == 'nop':
        return accumulator, pointer

# %% Run

def run(ops, args, part):
    pointer = 0 # incrementer that runs through the list of instructions
    argument = 0 # 
    accumulator = 0
    visited = set()
    running = True
    result = "We failed"

    while running:
        try: 
            operation, argument = ops[pointer], args[pointer]
            if pointer == (len(ops) - 1):
                result = "Part 2"
                running = False
                return result, accumulator, pointer
            if pointer in visited:
                if part == 1:
                    result = "Part 1"
                running = False
                return result, accumulator, pointer
            else:
                visited.add(pointer)
                accumulator, pointer = read_instruction(pointer, operation, argument, accumulator)
        except IndexError:
            result = "IndexError"
            running = False
            return result, accumulator, pointer
        continue

# %% part 1
part = 1
result, accumulator, pointer = run(ops, args, part)

print(result + ": accumulator %s, pointer %s" % (accumulator, pointer))

# %% part 2
import copy
jmps = [i for i, x in enumerate(ops) if x == 'jmp']
nops = [i for i, x in enumerate(ops) if x == 'nop']
part = 2

for j in jmps:
    mod_ops = copy.deepcopy(ops)
    mod_ops[j] = 'nop'
    result, accumulator, pointer = run(mod_ops, args, part)
    if result == "Part 2":
        print(result + ": accumulator %s, pointer %s" % (accumulator, pointer))

for n in nops:
    mod_ops = copy.deepcopy(ops)
    mod_ops[j] = 'jmp'
    result, accumulator, pointer = run(mod_ops, args, part)
    if result == "Part 2":
        print(result + ": accumulator %s, pointer %s" % (accumulator, pointer))
