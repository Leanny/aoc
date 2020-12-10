import re 

def convert_data(data):
    arr = data.splitlines()
    tmp = []
    res = []
    for a in arr:
        if len(a.strip()) == 0:
            res.append(tmp)
            tmp = []
        else:
            tmp.append(a)
    
    if len(tmp) > 0:
        res.append(tmp)
    return res


def part1(inp):
    def conv(i):
        return set("".join(i))
    return sum(map(len, map(conv, inp)))
    
def part2(inp):
    def conv(i):
        res = set(i[0])
        for a in i:
            res &= set(a)
        return res
    return sum(map(len, map(conv, inp)))
    

with open("test_input1.txt") as f:
    content = f.read()
    data = convert_data(content)
    p1 = part1(data)
    assert p1 == 6
    
with open("test_input2.txt") as f:
    content = f.read()
    data = convert_data(content)
    p1 = part1(data)
    assert p1 == 11
    p2 = part2(data)
    assert p2 == 6
   

with open("input.txt") as f:
    content = f.read()
    data = convert_data(content)
    print("Part 1", part1(data))
    print("Part 2", part2(data))