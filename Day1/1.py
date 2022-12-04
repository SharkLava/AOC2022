#!/usr/bin/env python3
from pathlib import Path

data = [(int(x) if len(x)>0 else x) for x in Path("data.txt").read_text().split("\n")]
x = 0
r = []
for i in data:
    if i == "":
        if x:
            r.append(x)
            x = 0
        r.append(i)
    else:
        x += i
r=list(set(r))
r.remove("")
r.sort(reverse=True)
print(sum(r[:3]))
