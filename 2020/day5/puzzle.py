import re 

def convert_data(data):
    return data.replace("F", "0").replace("L", "0").splitlines()

def get_rc(s, m, n):
    if m == n:
        return m 
    mid = (m+n-1)//2
    if s[0] == "0":
        return get_rc(s[1:], m, mid)
    else:
        return get_rc(s[1:], mid+1, n)

def part1(inp):
    return max([get_rc(s[:7], 0, 127) * 8 + get_rc(s[7:], 0, 7) for s in inp])
    
def part2(inp):
    nums = set([get_rc(s[:7], 0, 127) * 8 + get_rc(s[7:], 0, 7) for s in inp])
    for i in range(127 * 8 + 7):
        if i not in nums and (i+1) in nums and (i-1) in nums:
            return i

with open("test_input1.txt") as f:
    content = f.read()
    data = convert_data(content)
    p1 = part1(data)
    assert p1 == 820

with open("input.txt") as f:
    content = f.read()
    data = convert_data(content)
    print("Part 1", part1(data))
    print("Part 2", part2(data))