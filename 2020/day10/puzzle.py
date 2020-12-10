from collections import Counter 

def convert_data(data):
    return list(map(int, data.splitlines()))

def part1(inp):
    n = sorted([0] + inp)
    diff = Counter([n[i+1] - n[i] for i in range(len(inp))])
    return diff[1] * (1 + diff[3])
    
def part2(inp):
    nums = sorted([0] + inp + [3 + max(inp)], reverse=True)
    reachable = {i: 0 for i in nums}
    reachable[max(inp)] = 1
    for n in nums:
        for i in range(1, 4):
            if n - i in reachable:
                reachable[n-i] += reachable[n]
    return reachable[0]

with open("test_input1.txt") as f:
    content = f.read()
    data = convert_data(content)
    p1 = part1(data)
    assert p1 == 7*5
    p2 = part2(data)
    assert p2 == 8
    
with open("test_input2.txt") as f:
    content = f.read()
    data = convert_data(content)
    p1 = part1(data)
    assert p1 == 22*10
    p2 = part2(data)
    assert p2 == 19208

with open("input.txt") as f:
    content = f.read()
    data = convert_data(content)
    print("Part 1", part1(data))
    print("Part 2", part2(data))