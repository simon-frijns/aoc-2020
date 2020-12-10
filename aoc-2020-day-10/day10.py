# %% Read input
with open("input.txt", "r") as input_file:
    inp = input_file.readlines()
    inp = [int(line.strip()) for line in inp]

inp.append(max(inp) + 3)
inp.append(0)
inp.sort()
# %% part 1
from collections import deque 

onejolt = threejolt = joltage = 0
queue = deque(inp)

while len(queue) > 0:
    nextjolt = queue.popleft()
    if nextjolt - joltage == 1:
        onejolt += 1
    elif nextjolt - joltage == 3:
        threejolt += 1
    joltage = nextjolt
print(onejolt * threejolt)
# %% part 2

lastnum = len(inp) - 1
pathdict = {} # dictionary ->  set of i's, with value of paths stored for that i

def num_paths(i):
    paths = 0 
    if i in pathdict:
        paths = pathdict[i]
        return paths
    for p in range(i+1, len(inp)):
        if inp[p] - inp[i] <= 3:
            paths += num_paths(p)
    if paths == 0:
        paths = 1
    pathdict[i] = paths
    return paths
num_paths(0)
# %%
