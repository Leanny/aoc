def part1(inp):
    for i in inp:
        for b in inp:
            if i + b == 2020:
                print("part 1", i*b) 
                return 
                
def part2(inp):
    for i in inp:
        for a in inp:
            for b in inp:
                if a + i + b == 2020:
                    print("Part 2", a*i*b) 
                    return 

with open("input.txt") as f:
    content = f.readlines()
    nums = list(map(int, content))
    part1(nums)
    part2(nums)