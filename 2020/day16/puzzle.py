import re 
def convert_data(data):
    res = [[], [], []]
    desc, you, other = data.split("\n\n")
    for d in desc.splitlines():
        tmp = re.match("(.*): (\d+)-(\d+) or (\d+)-(\d+)", d).groups()
        res[0].append([tmp[0], [int(tmp[1]), int(tmp[2])], [int(tmp[3]), int(tmp[4])]])
    
    res[1] = list(map(int, you.split(":")[1].strip().split(",")))
    res[2] = [list(map(int, x.split(","))) for x in other.splitlines()[1:]]
    return res

def part1(inp):
    invalid = []
    for i in inp[2]:
        for k in i:
            inv = True
            for x in inp[0]:
                for mi,ma in x[1:]:
                    if mi <= k <= ma:
                        inv = False 
                        break 
            if inv:
                invalid.append(k)
        
    return sum(invalid)
    
def part2(inp):
    work_with = []
    for i in inp[2]:
        all_inv = False 
        for k in i:
            inv = True
            for x in inp[0]:
                for mi,ma in x[1:]:
                    if mi <= k <= ma:
                        inv = False 
                        break 
            if inv:
                all_inv = True 
                break 
        if not all_inv:
            work_with.append(i)

    candidate_map = {}
    candidates = [[1]]
    used_candidates = set()

    while len(used_candidates) < len(work_with[0]):
        candidates = [[] for _ in range(len(work_with[0]))]
        for i in range(len(inp[0])):
            c1, c2 = inp[0][i][1:]
            for k in range(len(work_with[0])):
                if k in used_candidates: continue
                if len([w for w, v in enumerate(work_with) if c1[0] <= v[k] <= c1[1] or c2[0] <= v[k] <= c2[1]]) == len(work_with):
                    candidates[i].append(k)
            
        for i, c in enumerate(candidates):
            if len(c) == 1:
                candidate_map[i] = c[0]
                used_candidates.add(c[0])
        
    res = 1
    for s in [i for i,v in enumerate(inp[0]) if "departure" in v[0]]:
        res *= inp[1][candidate_map[s]]
    return res
        
        
from time import time 

with open("test_input1.txt") as f:
    content = f.read()
    data = convert_data(content)
    p1 = part1(data)
    assert p1 == 71
    
with open("test_input2.txt") as f:
    content = f.read()
    data = convert_data(content)
    p2 = part2(data)
    assert p2 == 12*13
 
with open("input.txt") as f:
    content = f.read()
    data = convert_data(content)
    print("Part 1", part1(data))
    print("Part 2", part2(data))