import re 

def convert_data(data):
    arr = data.splitlines()
    res = []
    for line in arr:
        cmd, n = line.split(" ")
        res.append((cmd, int(n)))
    return res


def part1(inp):
    visited = [False] * len(inp)
    acc = 0
    ptr = 0
    while ptr < len(inp) and not visited[ptr]:
        com, num = inp[ptr]
        visited[ptr] = True
        if com == "nop":
            ptr += 1
        elif com == "acc":
            ptr += 1
            acc += num
        elif com == "jmp":
            ptr += num 
        else:
            exit("invalid code")
    return acc, ptr == len(inp)
    
    
def part2(inp):
    for i in range(len(inp)):
        if inp[i][0] in ["nop", "jmp"]:
            # nop -> jmp 
            if inp[i][0] == "nop":
                if inp[i][1] != 0: #fast fix infinite loop
                    inp[i] = ("jmp", inp[i][1])
                    acc, t = part1(inp)
                    if t:
                        return acc 
                    inp[i] = ("nop", inp[i][1])
            elif inp[i][0] == "jmp":
                if inp[i][1] != 0: #fast fix infinite loop
                    inp[i] = ("nop", inp[i][1])
                    acc, t = part1(inp)
                    if t:
                        return acc 
                    inp[i] = ("jmp", inp[i][1])
    

with open("test_input1.txt") as f:
    content = f.read()
    data = convert_data(content)
    p1, t1 = part1(data)
    assert p1 == 5
    assert t1 == False 
    p2 = part2(data)
    assert p2 == 8

with open("input.txt") as f:
    content = f.read()
    data = convert_data(content)
    print("Part 1", part1(data))
    print("Part 2", part2(data))