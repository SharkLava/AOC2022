#!/usr/bin/env python3
from pathlib import Path

def main():
    data = Path("data.txt").read_text().split("\n")
    score = 0
    Win = {
        'A':'Y',
        'B':'Z',
        'C':'X'
    }
    Draw = {
        'A':'X',
        'B':'Y',
        'C':'Z'
    }
    Score = {
        'X':1,
        'Y':2,
        'Z':3
    }
    data.remove('')
    for i in data:
        score+= my_turn(i[2],i[0])
    print(score)

def my_turn(my_choice,play):
    strategy = {}
    if my_choice == "Y":
        strategy = {"A": 4, "B": 5, "C": 6}

    if my_choice == "X":
        strategy = {"A": 3, "B": 1, "C": 2}

    if my_choice == "Z":
        strategy = {"A": 8, "B": 9, "C": 7}

    return strategy[play]

main()
