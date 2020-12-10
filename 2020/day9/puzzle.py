import re 

def convert_data(data):
    return list(map(int, data.splitlines()))

def part1(inp, preemble = 25):
    def sum_possible(arr, n):
        sarr = set(arr)
        for a in sarr:
            if (n - a) in sarr:
                return True
        return False 
            
    for i in range(preemble, len(inp)):
        if not sum_possible(inp[i - preemble: i], inp[i]):
            return inp[i]
    
def part2(inp, preemble = 25):
    num = part1(inp, preemble)
    idx = inp.index(num)
    for i in range(idx):
        for j in range(i+1, idx):
            if sum(inp[i:j]) == num:
                return max(inp[i:j]) + min(inp[i:j])
    

with open("test_input1.txt") as f:
    content = f.read()
    data = convert_data(content)
    p1 = part1(data, 5)
    assert p1 == 127
    p2 = part2(data, 5)
    assert p2 == 62

with open("input.txt") as f:
    content = f.read()
    data = convert_data(content)
    print("Part 1", part1(data))
    print("Part 2", part2(data))