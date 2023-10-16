import re

validPassports = 0
found = []

with open("4input.txt") as f:
    all_lines = f.readlines()
    for x in all_lines:
        if x == "\n":
            found = []
        if x != "\n":
            try:
                found.append(str(re.findall("byr:", x)[0]))
            except:
                pass
            try:
                found.append(str(re.findall("iyr:", x)[0]))
            except:
                pass
            try:
                found.append(str(re.findall("eyr:", x)[0]))
            except:
                pass
            try:
                found.append(str(re.findall("hgt:", x)[0]))
            except:
                pass
            try:
                found.append(str(re.findall("hcl:", x)[0]))
            except:
                pass
            try:
                found.append(str(re.findall("ecl:", x)[0]))
            except:
                pass
            try:
                found.append(str(re.findall("pid:", x)[0]))
            except:
                pass
            #found.append(str(re.findall("cid:", x)[0]))
            if "byr:" in found and "iyr:" in found and "eyr:" in found and "hgt:" in found and "hcl:" in found and "ecl:" in found and "pid:" in found:
                found = []
                validPassports += 1
print(validPassports)