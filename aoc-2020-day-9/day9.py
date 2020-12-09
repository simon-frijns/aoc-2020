# %% Read input
with open("input.txt", "r") as input_file:
    inp = input_file.readlines()
    inp = [int(line.strip()) for line in inp]
# %% part 1
from itertools import permutations as prmt

pream = 25
pointer = pream + 1
options = set()

lastnum = len(inp)
for i in range(lastnum):
    pointer = i + pream
    options.clear()
    perm = prmt(inp[i:i+pream], 2)
    for i in list(perm):
        options.add(sum(i))
    if inp[pointer] not in options:
        part_1 = inp[pointer]
        break

print("Part 1: %s" % part_1)

# %% part 2
for i in range(lastnum):
    for j in range(i+2, lastnum):
        if sum(inp[i:j]) == part_1:
            low = min(inp[i:j])
            high = max(inp[i:j])
            part_2 = low + high

print("Part 2: %s with %s as lowest and %s as highest" % (part_2, low, high))
# %%
