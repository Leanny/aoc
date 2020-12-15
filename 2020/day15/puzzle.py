from itertools import product

def convert_data(data):
    return [int(i) for i in data.split(",")]

def sol(inp, limit):
    res = {}
    last = None 
    for i, n in enumerate(inp):
        last = n 
        res[n] = [i+1, i+1]
        
    i += 1
    while i < limit:
        last = res[last][-1] - res[last][-2]
        tmp = res.get(last, [i+1])
        tmp.append(i+1)
        res[last] = tmp
        i += 1
        
    return last 
    
def part1(inp):
    return sol(inp, 2020)
    
def part2(inp):
    return sol(inp, 30000000)
        
from time import time 

with open("test_input0.txt") as f:
    content = f.read()
    data = convert_data(content)
    p1 = part1(data)
    assert p1 == 436
    p2 = part2(data)
    assert p2 == 175594
  
with open("test_input1.txt") as f:
    content = f.read()
    data = convert_data(content)
    p1 = part1(data)
    assert p1 == 1
    p2 = part2(data)
    assert p2 == 2578
    
with open("test_input2.txt") as f:
    content = f.read()
    data = convert_data(content)
    p1 = part1(data)
    assert p1 == 10
    p2 = part2(data)
    assert p2 == 3544142

with open("test_input3.txt") as f:
    content = f.read()
    data = convert_data(content)
    p1 = part1(data)
    assert p1 == 27
    p2 = part2(data)
    assert p2 == 261214
    
with open("test_input4.txt") as f:
    content = f.read()
    data = convert_data(content)
    p1 = part1(data)
    assert p1 == 78
    p2 = part2(data)
    assert p2 == 6895259
    
with open("test_input5.txt") as f:
    content = f.read()
    data = convert_data(content)
    p1 = part1(data)
    assert p1 == 438
    p2 = part2(data)
    assert p2 == 18
    
with open("test_input6.txt") as f:
    content = f.read()
    data = convert_data(content)
    p1 = part1(data)
    assert p1 == 1836
    p2 = part2(data)
    assert p2 == 362

with open("input.txt") as f:
    content = f.read()
    data = convert_data(content)
    print("Part 1", part1(data))
    print("Part 2", part2(data))