from functools import reduce
import operator

def convert_data(data):
    l1, l2 = data.splitlines()
    return int(l1), l2.split(",")
    

def part1(inp):
    earliest, ids = inp[0], [int(l) for l in inp[1] if l != "x"]
    res = min([(i - earliest%i, i) for i in ids])
    return res[0] * res[1]
    
def part2(inp):
    def prod(iterable):
        res = 1
        for i, _ in iterable:
            res *= i 
        return res
        
    def mul_inv(a, b):
        b0 = b
        x0, x1 = 0, 1
        if b == 1: return 1
        while a > 1:
            q = a // b
            a, b = b, a%b
            x0, x1 = x1 - q * x0, x0
        if x1 < 0: x1 += b0
        return x1
        
    nums = [(int(inp[1][i]), -i) for i in range(len(inp[1])) if inp[1][i] != "x"]
    s = 0
    N = prod(nums)
    for n_i, a_i in nums:
        p = N // n_i
        s += a_i * mul_inv(p, n_i) * p
    return s % N

with open("test_input1.txt") as f:
    content = f.read()
    data = convert_data(content)
    p1 = part1(data)
    assert p1 == 295
    p2 = part2(data)
    assert p2 == 1068781
    
with open("test_input2.txt") as f:
    content = f.read()
    data = convert_data(content)
    p2 = part2(data)
    assert p2 == 3417
    
with open("test_input3.txt") as f:
    content = f.read()
    data = convert_data(content)
    p2 = part2(data)
    assert p2 == 754018
    
with open("test_input4.txt") as f:
    content = f.read()
    data = convert_data(content)
    p2 = part2(data)
    assert p2 == 779210
    
with open("test_input5.txt") as f:
    content = f.read()
    data = convert_data(content)
    p2 = part2(data)
    assert p2 == 1261476
    
with open("test_input6.txt") as f:
    content = f.read()
    data = convert_data(content)
    p2 = part2(data)
    assert p2 == 1202161486

with open("input.txt") as f:
    content = f.read()
    data = convert_data(content)
    print("Part 1", part1(data))
    print("Part 2", part2(data))