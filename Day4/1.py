#!/usr/bin/env python3
from pathlib import Path

def main():
    data = Path("data.txt").read_text().split("\n")
    data.remove("")
    assignments = [i.rsplit(',') for i in data]
    for x in assignments:
        for i,j in enumerate(x):
            k = j.split('-')
            x[i] = set(range(int(k[0]), int(k[1])+1))
    count_1 = 0
    count_2 = 0
    for i in assignments:
        if i[0].issubset(i[1]) or i[1].issubset(i[0]):
            count_1 += 1
        if not i[0].isdisjoint(i[1]):
            count_2 += 1
    print(count_1)    #Part 1
    print(count_2)    #Part 2
main()
