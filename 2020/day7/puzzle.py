import re 

def convert_data(data):
    arr = data.replace("bags", "bag").splitlines()
    res = {}
    for a in arr:
        bag, content = a.split("bag contain")
        tmp = []
        if content[1] != "n": # no other bag
            for c in content.split(","):
                tmp_split = c.strip().split(" ", 1)
                num, col = int(tmp_split[0]), tmp_split[1][:-4].strip()
                tmp.append((num, col))
        res[bag.strip()] = tmp 
    return res


def part1(inp):
    # filter for shiny gold
    need_contain = set(["shiny gold"])
    res = set()
    last_size = -1
    while len(res) != last_size:
        last_size = len(res)
        for k,v in inp.items():
            for _, c in v:
                if c in need_contain:
                    need_contain.add(k)
                    res.add(k)
                    
    return len(res)
    
    
def part2(inp):
    def get_num_of_bags(bag):
        s = 0
        for k, v in inp[bag]:
            s += k
            s += k * get_num_of_bags(v)
            
        return s 
        
    return get_num_of_bags("shiny gold") 
    

with open("test_input1.txt") as f:
    content = f.read()
    data = convert_data(content)
    p1 = part1(data)
    assert p1 == 4
    p2 = part2(data)
    assert p2 == 32
    
with open("test_input2.txt") as f:
    content = f.read()
    data = convert_data(content)
    p2 = part2(data)
    assert p2 == 126

with open("input.txt") as f:
    content = f.read()
    data = convert_data(content)
    print("Part 1", part1(data))
    print("Part 2", part2(data))