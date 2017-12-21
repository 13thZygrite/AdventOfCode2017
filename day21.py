#!/usr/bin/env python
from operator import itemgetter

with open("input_day21") as f:
    input = f.readlines()
    
patterns = {}
for line in input:
    before, after = line.strip().split(" => ")
    patterns[tuple(before.split("/"))] = after.split("/")
    
def rotate(pattern):
    temp = [row.split() for row in pattern]
    # Thanks stack overflow
    return ["".join(list(tup)) for tup in zip(*pattern[::-1])]

def vert_flip(pattern):
    return pattern[::-1]
    
def possible(pattern):
    return [pattern, rotate(pattern), rotate(rotate(pattern)), rotate(rotate(rotate(pattern))), vert_flip(pattern), rotate(vert_flip(pattern)), rotate(rotate(vert_flip(pattern))), rotate(rotate(rotate(vert_flip(pattern))))]

def combine(rows_of_patterns):
    output = []
    for row in rows_of_patterns:
        row_lines = ["" for _ in range(len(row[0]))]
        for pattern in row:
            for i in range(len(pattern)):
                row_lines[i] = row_lines[i] + pattern[i]
        output = output + row_lines
    return output

def split(pattern):
    output = []
    if len(pattern) % 2 == 0:
        for i in range(len(pattern) / 2):
            row = []
            for j in range(len(pattern) / 2):
                row.append([pattern[2*i][2*j:2*(j+1)], pattern[2*i + 1][2*j:2*(j+1)]])
            output.append(row)
    else:
        assert(len(pattern) % 3 == 0)
        for i in range(len(pattern) / 3):
            row = []
            for j in range(len(pattern) / 3):
                row.append([pattern[3*i][3*j:3*(j+1)], pattern[3*i + 1][3*j:3*(j+1)], pattern[3*i + 2][3*j:3*(j+1)]])
            output.append(row)
    # Sanity check
    assert(len(output) == len(output[0]))
    return output
    

current_pattern = [".#.", "..#", "###"]

for _ in range(5):
    row_of_patterns = split(current_pattern)
    for i in range(len(row_of_patterns)):
        for j in range(len(row_of_patterns[0])):
            for pattern in possible(row_of_patterns[i][j]):
                if tuple(pattern) in patterns:
                    row_of_patterns[i][j] = patterns[tuple(pattern)]
                    break
    current_pattern = combine(row_of_patterns)
count = 0
for row in current_pattern:
    count += row.count("#")
print "Part 1:", count

for _ in range(13):
    row_of_patterns = split(current_pattern)
    for i in range(len(row_of_patterns)):
        for j in range(len(row_of_patterns[0])):
            for pattern in possible(row_of_patterns[i][j]):
                if tuple(pattern) in patterns:
                    row_of_patterns[i][j] = patterns[tuple(pattern)]
                    break
    current_pattern = combine(row_of_patterns)
count = 0
for row in current_pattern:
    count += row.count("#")
print "Part 2:", count
