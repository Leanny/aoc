import re 
from itertools import product
import json 

def convert_data(data):
    d = data.splitlines()
    y_coords = {}
    for y in range(len(d)):
        x_coords = {}
        for x in range(len(d[0])):
            if "#" == d[y][x]:
                x_coords[x] = True
        if len(x_coords) > 0:
            y_coords[y] = x_coords
    coords = {0: y_coords}
    return coords

def part1(inp):
    def new_iteration(coords):
        c = {}
        candidates = []
        for z in coords:
            for y in coords[z]:
                for x in coords[z][y]:
                    for x1, y1, z1 in product([-1, 0, 1], repeat=3):
                        candidates.append((x+x1, y+y1, z+z1))
        for x, y, z in candidates:
            neighbours = 0
            for x1, y1, z1 in product([-1, 0, 1], repeat=3):
                if (x1 != 0 or y1 != 0 or z1 != 0) and coords.get(z1+z, {}).get(y1+y, {}).get(x1+x, False):
                        neighbours += 1
                        
            if coords.get(z, {}).get(y, {}).get(x, False):
                if neighbours in [2, 3]:
                    if z not in c:
                        c[z] = {}
                    if y not in c[z]:
                        c[z][y] = {}
                    c[z][y][x] = True 
            elif neighbours == 3:
                if z not in c:
                    c[z] = {}
                if y not in c[z]:
                    c[z][y] = {}
                c[z][y][x] = True 
        return c
        
    coords = inp 
    for i in range(6):
        coords = new_iteration(coords)
    
    res = 0
    for z in coords:
        for y in coords[z]:
            for x in coords[z][y]:
                res += 1

    return res
    
def part2(inp):
    def new_iteration(coords):
        c = {}
        candidates = []
        for w in coords:
            for z in coords[w]:
                for y in coords[w][z]:
                    for x in coords[w][z][y]:
                        for w1, x1, y1, z1 in product([-1, 0, 1], repeat=4):
                            candidates.append((x+x1, y+y1, z+z1, w+w1))

        for x, y, z, w in candidates:
            neighbours = 0
            for x1, y1, z1, w1 in product([-1, 0, 1], repeat=4):
                if (x1 != 0 or y1 != 0 or z1 != 0 or w1 != 0) and coords.get(w1+w, {}).get(z1+z, {}).get(y1+y, {}).get(x1+x, False):
                        neighbours += 1
                        
            if coords.get(w, {}).get(z, {}).get(y, {}).get(x, False):
                if neighbours in [2, 3]:
                    if w not in c:
                        c[w] = {}
                    if z not in c[w]:
                        c[w][z] = {}
                    if y not in c[w][z]:
                        c[w][z][y] = {}
                    c[w][z][y][x] = True 
            elif neighbours == 3:
                if w not in c:
                    c[w] = {}
                if z not in c[w]:
                    c[w][z] = {}
                if y not in c[w][z]:
                    c[w][z][y] = {}
                c[w][z][y][x] = True 
        return c
        
    coords = {0: inp}
    for i in range(6):
        coords = new_iteration(coords)
    res = 0
    for w in coords:
        for z in coords[w]:
            for y in coords[w][z]:
                for x in coords[w][z][y]:
                    res += 1
    return res
        
from time import time 

with open("test_input1.txt") as f:
    content = f.read()
    data = convert_data(content)
    p1 = part1(data)
    assert p1 == 112, p1
    p2 = part2(data)
    assert p2 == 848, p2
    
with open("input.txt") as f:
    content = f.read()
    data = convert_data(content)
    print("Part 1", part1(data))
    print("Part 2", part2(data))