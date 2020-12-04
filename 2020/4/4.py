#!/usr/bin/env python3

required = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])


def solveA(passports):
    return sum(1 if p.keys() >= required else 0 for p in passports)


def solveB(passports):
    valid = 0
    for p in passports:
        if not required.issubset(p.keys()):
            continue
        try:
            if not (1920 <= int(p["byr"]) <= 2002):
                continue
            if not (2010 <= int(p["iyr"]) <= 2020):
                continue
            if not (2020 <= int(p["eyr"]) <= 2030):
                continue
            hgt = int(p["hgt"][:-2])
            if not (
                (p["hgt"][-2:] == "cm" and 150 <= hgt <= 193)
                or (p["hgt"][-2:] == "in" and 59 <= hgt <= 76)
            ):
                continue
            hcl = p["hcl"]
            if not (
                hcl[0] == "#"
                and len(hcl) == 7
                and set(hcl[1:]).issubset("abcdef0123456789")
            ):
                continue
            if p["ecl"] not in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
                continue
            if not (len(p["pid"]) == 9 and set(p["pid"]).issubset("0123456789")):
                continue
            valid += 1
        except ValueError:
            pass

    return valid


lines = [l.strip().split() for l in open("input")]
lines.append([])
passports = []
current = []
for l in lines:
    if not l and current:
        passports.append(dict(kv.split(":") for kv in current))
        current = []
    current.extend(l)

print("A", solveA(passports))
print("B", solveB(passports))
