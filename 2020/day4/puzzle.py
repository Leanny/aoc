import re 

def convert_data(data):
    arr = data.splitlines()
    i = 0
    res = []
    tmp = {}
    while i < len(arr):
        if len(arr[i].strip()) == 0:
            res.append(tmp)
            tmp = {}
        else:
            for e in arr[i].split(" "):
                k, v = e.split(":")
                tmp[k] = v
        i += 1
    if len(tmp.values()) > 0:
        res.append(tmp)
    return res

fields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"])

def part1(inp):
    def is_valid(data):
        data["cid"] = 0
        return len(data.keys()) == len(fields)

    return len([1 for i in inp if is_valid(i)])
    
def part2(inp):
    def is_valid(data):
        data["cid"] = 0
        if len(data.keys()) != len(fields):
            return False 
        try:
            if not (1920 <= int(data["byr"]) <= 2002):
                return False 
            if not (2010 <= int(data["iyr"]) <= 2020):
                return False 
            if not (2020 <= int(data["eyr"]) <= 2030):
                return False
            hgt, mes = re.match("([0-9]+)([a-z]+)", data["hgt"]).groups()
            if not (mes == "cm" and 150 <= int(hgt) <= 193 or mes == "in" and 59 <= int(hgt) <= 76):
                return False 
            if not re.match("#[0-9a-f]{6}", data["hcl"]):
                return False 
            if data["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                return False    
            if not re.match("^[0-9]{9}$", data["pid"]):
                return False
        except:
            return False 
            
        return True
        
    return len([1 for i in inp if is_valid(i)])

with open("test_input1.txt") as f:
    content = f.read()
    data = convert_data(content)
    p1 = part1(data)
    assert p1 == 2
    
with open("test_input2.txt") as f:
    content = f.read()
    data = convert_data(content)
    p2 = part2(data)
    assert p2 == 0
    
with open("test_input3.txt") as f:
    content = f.read()
    data = convert_data(content)
    p2 = part2(data)
    assert p2 == 4

with open("input.txt") as f:
    content = f.read()
    data = convert_data(content)
    print("Part 1", part1(data))
    print("Part 2", part2(data))