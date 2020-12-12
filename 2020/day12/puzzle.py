def convert_data(data):
    return [(d[0], int(d[1:])) for d in data.splitlines()]
    

def part1(inp):
    dir_to_idx = {"N": 0, "S": 2, "E": 1, "W": 3}
    dir_mul = {"R": 1, "L": -1}
    dirs = [(1, 0), #north
            (0, 1), #east
            (-1, 0), #south
            (0, -1)] #west
    start_dir = 1
    x, y = 0, 0
    for d, m in inp:
        if d in ["N", "S", "E", "W"]:
            xd, yd = dirs[dir_to_idx[d]]
            x += xd * m 
            y += yd * m 
        elif d == "F":
            xd, yd = dirs[start_dir]
            x += xd * m 
            y += yd * m 
        elif d in ["L", "R"]:
            mul = dir_mul[d]
            start_dir = (start_dir + 4 + mul * m // 90) & 3
        else:
            exit(f"invalid input {d}{m}")
            
    return abs(x) + abs(y)
        
    
def part2(inp):
    dir_to_idx = {"N": 0, "S": 2, "E": 1, "W": 3}
    dir_mul = {"R": 1, "L": -1}
    dirs = [(1, 0), #north
            (0, 1), #east
            (-1, 0), #south
            (0, -1)] #west

    x, y = 0, 0
    wx, wy = 1, 10
    for d, m in inp:
        if d in ["N", "S", "E", "W"]:
            xd, yd = dirs[dir_to_idx[d]]
            wx += xd * m 
            wy += yd * m 
        elif d == "F":
            xp = wx * m 
            yp = wy * m 
            x += xp 
            y += yp 
        elif d in ["L", "R"]:
            mul = dir_mul[d]
            start_dir = (4 + mul * m // 90) & 3
            # reflecting the waypoint
            if start_dir == 1:
                wx, wy = -wy, wx
            elif start_dir == 2:
                wx, wy = -wx, -wy
            elif start_dir == 3:
                wx, wy = wy, -wx
        else:
            exit(f"invalid input {d}{m}")
            
    return abs(x) + abs(y)

with open("test_input1.txt") as f:
    content = f.read()
    data = convert_data(content)
    p1 = part1(data)
    assert p1 == 25
    p2 = part2(data)
    assert p2 == 286

with open("input.txt") as f:
    content = f.read()
    data = convert_data(content)
    print("Part 1", part1(data))
    print("Part 2", part2(data))