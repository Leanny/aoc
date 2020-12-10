import re 

def part1(inp):
    print("Part 1", len([i for i in inp if int(i[0]) <= i[3].count(i[2]) <= int(i[1])]))
    
def part2(inp):
    print("Part 2", len([i for i in inp if (i[3][int(i[0])-1] + i[3][int(i[1])-1]).count(i[2]) == 1]))

with open("input.txt") as f:
    content = f.read()
    res = re.findall("([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)\n*", content, flags=0)
    assert len(res) == 1000
    part1(res)
    part2(res)