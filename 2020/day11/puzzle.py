from collections import Counter 

seat_map = {".": "0", "L": "1", "#": "2"}

def convert_data(data):
    lines = data.splitlines()
    res = [["3"] * (len(lines) + 2)]
    for line in lines:
        res.append(["3"] + [seat_map.get(c) for c in line] + ["3"])
    res.append(["3"] * (len(lines) + 2))
    return res 

def part1(inp):
    def nextSeats(state):
        res = [s.copy() for s in state]
        for x in range(1, len(state) - 1): 
            for y in range(1, len(state[x]) - 1):
                if state[x][y] != "0":
                    tmp = ""
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            if i != 0 or j != 0:
                                tmp += state[x + i][y + j]
                    if state[x][y] == "1" and tmp.count("2") == 0:
                        res[x][y] = "2"
                    elif state[x][y] == "2" and tmp.count("2") >= 4:
                        res[x][y] = "1"
        return res 
        
    oldS = []
    newS = inp.copy()
    while oldS != newS:
        oldS = newS
        newS = nextSeats(newS)
    return str(newS).count("2")
        
    
def part2(inp):
    def printa(qq):
        for a in qq[1:-1]:
            print("".join(a[1:-1]).replace("0", ".").replace("1", "L").replace("2", "#"))
            
    def nextSeats(state):
        res = [s.copy() for s in state]
        for x in range(1, len(state) - 1): 
            for y in range(1, len(state[x]) - 1):
                if state[x][y] != "0":
                    tmp = ""
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            if i != 0 or j != 0:
                                k = 1
                                while state[x + k * i][y + k * j] == "0":
                                    k += 1
                                tmp += state[x + k * i][y + k * j]
                    if state[x][y] == "1" and tmp.count("2") == 0:
                        res[x][y] = "2"
                    elif state[x][y] == "2" and tmp.count("2") >= 5:
                        res[x][y] = "1"
        return res 
        
    oldS = []
    newS = inp.copy()
    while oldS != newS:
        oldS = newS
        newS = nextSeats(newS)

    return str(newS).count("2")

with open("test_input1.txt") as f:
    content = f.read()
    data = convert_data(content)
    p1 = part1(data)
    assert p1 == 37
    p2 = part2(data)
    assert p2 == 26


with open("input.txt") as f:
    content = f.read()
    data = convert_data(content)
    print("Part 1", part1(data))
    print("Part 2", part2(data))