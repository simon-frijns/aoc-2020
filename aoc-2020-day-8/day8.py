# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% Read input

with open("input.txt", "r") as input_file:
    inp = input_file.read().strip().split('\n') 

# %%
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
# %% Read_instructions

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

    while running:
        try: 
            operation, argument = ops[pointer], args[pointer]
            if pointer == (len(ops) - 1):
                print("Terminated on %s" % accumulator)
            if pointer in visited:
                if part == 1:
                    print("Errored out on %s at %s" % (accumulator, pointer))
                running = False
            else:
                visited.add(pointer)
                accumulator, pointer = read_instruction(pointer, operation, argument, accumulator)
        except IndexError:
            print("Pointer too high on %s at %s" % (accumulator, pointer))
            running = False
        continue

# %% part 1
run(ops, args, 1)

# %% part 2
import copy
jmps = [i for i, x in enumerate(ops) if x == 'jmp']
nops = [i for i, x in enumerate(ops) if x == 'nop']

for j in jmps:
    mod_ops = copy.deepcopy(ops)
    mod_ops[j] = 'nop'
    run(mod_ops, args, 2)

for n in nops:
    mod_ops = copy.deepcopy(ops)
    mod_ops[j] = 'jmp'
    run(mod_ops, args, 2)