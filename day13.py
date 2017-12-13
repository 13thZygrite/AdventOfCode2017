#!/usr/bin/env python

with open("input_day13") as f:
    input = f.readlines()
    
split = [map(int, line.split(": ")) for line in input]
state = [[] for i in range(split[-1][0] + 1)]
for line in split:
    state[line[0]] = [line[1], 1, 0] # Length, direction (1 down, -1 up), current pos

# Part 1
severity = 0
for line in split:
    if line[0] % ((line[1] - 2)* 2 + 2) == 0:
        severity += line[0]* line[1]
print "Part 1: ", severity

# Part 2
delay = 0
while (1):
    severity = 0
    failed = False
    for line in split:
        if (line[0] + delay) % ((line[1] - 2)* 2 + 2) == 0:
            failed = True
    if not failed:
        print "Part 2: ", delay
        break
    delay += 1
