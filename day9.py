#!/usr/bin/env python

with open("input_day9") as f:
    input = f.readlines()
    
input = input[0].strip()


# State
score = 0
garbage_count = 0
depth = 0
garbage = False
ignore = False

for char in input:
    print char, depth, garbage, ignore
    if ignore:
        ignore = False
        continue
    if garbage:
        if char == '>':
            garbage = False
            continue
        elif char == '!':
            ignore = True
            continue
        else:
            garbage_count += 1
            continue
    if char == '<':
        garbage = True
        continue
    if char == '{':
        depth += 1
        continue
    if char == '}':
        score += depth
        depth -= 1
        assert (depth > -1)
        continue

print "Part 1:", score
print "Part 2:", garbage_count