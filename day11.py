#!/usr/bin/env python

import math

with open("input_day11") as f:
    input = f.readlines()
    
input = input[0].strip()

dirs = input.split(",");

def dist(north, east):
    # north moves increase north by 1, north-east etc by 0.5 where we then round towards negative infinity
    # east behaves as expected
    north = math.floor(north)
    if (abs(north) * 2 < abs(east)):
        return abs(east)
    else: 
        return math.floor(abs(north) - 0.5 * abs(east)) + abs(east)
        


# Part 1 and 2
n_ord = 0
e_ord = 0
max_dist = 0
for dir in dirs:
    if dir == 'n':
        n_ord += 1
    elif dir == 's':
        n_ord -= 1
    elif dir == 'ne':
        n_ord += 0.5
        e_ord += 1
    elif dir == 'sw':
        n_ord -= 0.5
        e_ord -= 1
    elif dir == 'nw':
        n_ord += 0.5
        e_ord -= 1
    elif dir == 'se':
        n_ord -= 0.5
        e_ord += 1
    if max_dist < dist(n_ord, e_ord):
        max_dist = dist(n_ord, e_ord)

print "Part 1: ", dist(n_ord, e_ord)
print "Part 2: ", max_dist

