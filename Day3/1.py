#!/usr/bin/env python3

from pathlib import Path

def main():
    data = Path("data.txt").read_text().split("\n")
    data.remove('')
    part2(data)

def get_priority(common):
    common = str(common)[2]
    if common.isupper():
        return(ord(common)-38)
    return(ord(common)-96)

def part1(data):
    sumvar = 0
    for i in data:
        isize = len(i)//2
        c1 = set(i[:isize])
        c2 = set(i[isize:])
        common = c1.intersection(c2)
        sumvar += get_priority(common)
    print(sumvar)

def part2(data):
    sumvar = 0
    i=0
    while(i<len(data)):
          common = set(data[i]).intersection(set(data[i+1]).intersection(set(data[i+2])))
          sumvar+=get_priority(common)
          i +=3
    print(sumvar)

main()
