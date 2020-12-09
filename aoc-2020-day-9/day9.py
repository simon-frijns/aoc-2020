# %% Read input
with open("input.txt", "r") as input_file:
    inp = input_file.readlines()
    inp = [int(line.strip()) for line in inp]
# %% part 1
from itertools import permutations as prmt

pream = 25
pointer = pream + 1
options = set()
running = True

while running:
    options.clear()
    pointer += 1
    perm = prmt(inp[pointer-pream:pointer], 2)
    for i in list(perm):
        options.add(sum(i))
    if inp[pointer] not in options:
        part_1 = inp[pointer]
        print("Part 1 : %s" % part_1)
        running = False
# %% part 2
options = []
window = 0
lastnum = len(inp)
for i in range(lastnum):
    for j in range(i+2, lastnum):
        if sum(inp[i:j]) == part_1:
            part_2 = min(inp[i:j]) + max(inp[i:j])

print(part_2)
# %%
