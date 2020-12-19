import re 
from itertools import product
import json 

def convert_data(data):
    return data.splitlines()

def part1(inp):
    def evaluate(s):
        ret = 0
        current = 0
        last_operator = "+" 
        s = s.replace(" ", "")
        for p in s:
            if p.isnumeric():
                current = current * 10 + int(p)
            else:
                if last_operator == "+":
                    ret += current 
                else:
                    ret *= current 
                current = 0
                last_operator = p 
        if last_operator == "+":
            ret += current 
        else:
            ret *= current  
        return ret 
        
    res = []
    for i in inp:
        while "(" in i:
            r = i.index(")")
            l = i.rindex("(", 0, r)
            e = evaluate(i[l+1:r])
            i = i.replace(i[l:r+1], str(e))
        res.append(evaluate(i))
    return sum(res)
            
def part2(inp):
    def evaluate(s):
        ret = 0
        current = 0
        while "+" in s:
            parts = s.split(" ")
            x = parts.index("+")
            a = int(parts[x-1])
            b = int(parts[x+1])
            s = s.replace(f"{a} + {b}", str(a+b))
        return eval(s)
        
    res = []
    for i in inp:
        while "(" in i:
            r = i.index(")")
            l = i.rindex("(", 0, r)
            e = evaluate(i[l+1:r])
            i = i.replace(i[l:r+1], str(e))
        res.append(evaluate(i))
    return sum(res)
        
from time import time 

with open("test_input1.txt") as f:
    content = f.read()
    data = convert_data(content)
    p1 = part1(data)
    assert p1 == 26, p1
    p2 = part2(data)
    assert p2 == 46, p2
    
with open("test_input2.txt") as f:
    content = f.read()
    data = convert_data(content)
    p1 = part1(data)
    assert p1 == 437, p1
    p2 = part2(data)
    assert p2 == 1445, p2
    
with open("test_input3.txt") as f:
    content = f.read()
    data = convert_data(content)
    p1 = part1(data)
    assert p1 == 12240, p1
    p2 = part2(data)
    assert p2 == 669060, p2
    
with open("test_input4.txt") as f:
    content = f.read()
    data = convert_data(content)
    p1 = part1(data)
    assert p1 == 13632, p1
    p2 = part2(data)
    assert p2 == 23340, p2
    
with open("test_input6.txt") as f:
    content = f.read()
    data = convert_data(content)
    p2 = part2(data)
    assert p2 == 51, p2

with open("test_input5.txt") as f:
    content = f.read()
    data = convert_data(content)
    p1 = part1(data)
    assert p1 == 26 + 437 + 12240 + 13632, p1
    p2 = part2(data)
    assert p2 == 46 + 1445 + 669060 + 23340, p2

with open("input.txt") as f:
    content = f.read()
    data = convert_data(content)
    print("Part 1", part1(data))
    print("Part 2", part2(data))