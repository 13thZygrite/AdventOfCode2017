#!/usr/bin/env python
import re


with open("input_day12") as f:
    input = f.readlines()
    
cleaned = [re.sub(r'.*> ', '', line.strip()).split(", ") for line in input]
cleaned = [map(int, line) for line in cleaned]

total = len(cleaned)
so_far = 0
# Part 1

stack = []
visited = set();
for prog in cleaned[0]:
    stack.append(prog)
cleaned[0] = []
visited.add(0)
while len(stack) != 0:
    curr = stack.pop()
    visited.add(curr)
    for prog in cleaned[curr]:
        if prog in visited:
            continue
        stack.append(prog)
    cleaned[curr] = []

print "Part 1: ", len(visited)
    
groups = [visited]
so_far += len(visited)

# Part 2. One day I'll be forced to do real graph processing. TODAY IS NOT THAT DAY
while so_far < total:
    start = 0
    for i in range(len(cleaned)):
        if cleaned[i] == []:
            continue
        start = i
        break
    stack = []
    visited = set();
    for prog in cleaned[start]:
        stack.append(prog)
    cleaned[start] = []
    visited.add(start)
    while len(stack) != 0:
        curr = stack.pop()
        visited.add(curr)
        for prog in cleaned[curr]:
            if prog in visited:
                continue
            stack.append(prog)
        cleaned[curr] = []
    groups.append(visited)
    so_far += len(visited)

print "Part 2:", len(groups)