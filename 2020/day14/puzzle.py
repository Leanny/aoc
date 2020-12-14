from itertools import product

def convert_data(data):
    res = []
    for d in data.splitlines():
        t, v = d.split(" = ")
        if t == "mask":
            i1 = int(v.replace("X", "0"), 2) # or mask
            i2 = int(v.replace("X", "1"), 2) # and mask 
            res.append((t, i1, i2, v))
        else:
            res.append((int(t[4:-1]), int(v)))            
    return res
    

def part1(inp):
    mem = {}
    mask1 = 0
    mas2 = -1
    for l in inp:
        if l[0] == "mask":
            mask1, mask2 = l[1], l[2]
        else:
            mem[l[0]] = l[1] & mask2 | mask1
    return sum(mem.values())
    
def part2(inp):
    mem = {}
    mask = []
    fluctual_bits = []
    for i in inp:
        if i[0] == "mask":
            mask = i[1:]
            fluctual_bits = [n for n, v in enumerate(mask[2]) if v == "X"]
        else:
            s = list(bin(i[0])[2:].zfill(36))
            val = [s[v] if mask[2][v] == '0' else '1' for v in range(len(s))]
            for perm in product("01", repeat=len(fluctual_bits)):
                for n, v in zip(fluctual_bits, perm):
                    val[n] = v 
                mem["".join(val)] = i[1]
    return sum(mem.values())
        
with open("test_input1.txt") as f:
    content = f.read()
    data = convert_data(content)
    p1 = part1(data)
    assert p1 == 165
    
with open("test_input2.txt") as f:
    content = f.read()
    data = convert_data(content)
    p2 = part2(data)
    assert p2 == 208

with open("input.txt") as f:
    content = f.read()
    data = convert_data(content)
    print("Part 1", part1(data))
    print("Part 2", part2(data))