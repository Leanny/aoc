import re 

def convert_data(data):
    arr = data.splitlines()
    return arr

def part1(inp):
    x = 0
    res = 0
    for y in inp:
        res += y[x] == "#"
        x += 3
        x %= len(y)
    return res 
    
def part2(inp):
    x1, x2, x3, x4, x5 = 0, 0, 0, 0, 0
    y_c = 0
    res1, res2, res3, res4, res5 = 0, 0, 0, 0, 0
    for y in inp:
        res1 += y[x1] == "#"
        res2 += y[x2] == "#"
        res3 += y[x3] == "#"
        res4 += y[x4] == "#"
        if y_c&1 == 0:
            res5 += y[x5] == "#"
            x5 += 1
        
        x1 += 1
        x2 += 3
        x3 += 5
        x4 += 7
        x1 %= len(y)
        x2 %= len(y)
        x3 %= len(y)
        x4 %= len(y)
        x5 %= len(y)
        y_c += 1
    
    return res1 * res2 * res3 * res4 * res5

with open("test_input1.txt") as f:
    content = f.read()
    data = convert_data(content)
    p1 = part1(data)
    assert p1 == 7
    p2 = part2(data)
    assert p2 == 336

with open("input.txt") as f:
    content = f.read()
    data = convert_data(content)
    print("Part 1", part1(data))
    print("Part 2", part2(data))