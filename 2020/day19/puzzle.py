import re 

def convert_data(data):
    return [d.splitlines() for d in data.split("\n\n")]

def part1(inp):
    res = {}
    for l in inp[0]:
        k, v = l.split(":")
        v = "|".join([f"({' '.join([f'({q})' for q in n.strip().split(' ')])})" for n in v.strip().replace('"', '').split("|")]).replace(" ", "")
        res[k.strip()] = v

    nums = re.findall("\(\d+\)", res["0"])
    while len(nums) > 0:
        s = res["0"]        
        for n in nums:
            s = s.replace(n, f"({res[n[1:-1]]})")
        nums = re.findall("\(\d+\)", res["0"])
        res["0"] = s
    res["0"] = "^" + res["0"].replace(" ", "") + "$"
    c = re.compile(res["0"])
    return len([1 for i in inp[1] if c.match(i)])
            
def part2(inp):
    res = {}
    for l in inp[0]:
        k, v = l.split(":")
        v = "|".join([f"({' '.join([f'({q})' for q in n.strip().split(' ')])})" for n in v.strip().replace('"', '').split("|")]).replace(" ", "")
        res[k.strip()] = v

    res["8"] = "((42)+)"
    res["11"] = "(" + "|".join([f"({''.join(['(42)']*(i+1))}{''.join(['(31)']*(i+1))})" for i in range(5)]) + ")" # note: 5 yields the biggest results. For 6 this is unchanged
    
    nums = re.findall("\(\d+\)", res["0"])
    while len(nums) > 0:
        s = res["0"]        
        for n in nums:
            s = s.replace(n, f"({res[n[1:-1]]})")
        nums = re.findall("\(\d+\)", res["0"])
        res["0"] = s
    res["0"] = "^" + res["0"].replace(" ", "") + "$"
    c = re.compile(res["0"])
    return len([1 for i in inp[1] if c.match(i)])
        
with open("test_input1.txt") as f:
    content = f.read()
    data = convert_data(content)
    p1 = part1(data)
    assert p1 == 2, p1
    
with open("test_input2.txt") as f:
    content = f.read()
    data = convert_data(content)
    p1 = part1(data)
    assert p1 == 3, p1
    p2 = part2(data)
    assert p2 == 12, p1
    
with open("input.txt") as f:
    content = f.read()
    data = convert_data(content)
    print("Part 1", part1(data))
    print("Part 2", part2(data))