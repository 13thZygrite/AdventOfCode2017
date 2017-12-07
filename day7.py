#!/usr/bin/env python
import re

with open("input_day7") as f:
    input = f.readlines()
    
input = [x.strip() for x in input]
# Part 1
split = [re.sub(r'\(.*\)', '', line).split("->") for line in input]
names = [line[0].strip(" ") for line in split]

loadbearing = [line for line in split if len(line) > 1]
loadbearing = [[line[0].strip(), line[1].strip().split(', ')] for line in loadbearing]
loadbearing_names = [line[0] for line in loadbearing]

loop_bottom = names[0]
current_bottom = names[0]

while(1):
    for i in range(len(loadbearing)):
        if current_bottom in loadbearing[i][1]:
            current_bottom = loadbearing[i][0]
    if loop_bottom == current_bottom:
        break
    loop_bottom = current_bottom
print loop_bottom

# Part 2
names_weights = [re.sub(r'\(|\)', '', line).split("->")[0].strip() for line in input]
names_weights = [line.split(" ") for line in names_weights]
names_weights_map = {}
for i in range(len(names_weights)):
    names_weights_map[names_weights[i][0]] = int(names_weights[i][1])
#This is dumb
names_done = {}

for name in names:
    if name in loadbearing_names:
        names_done[name] = False;
    else:
        names_done[name] = True;
while(1):
    for line in loadbearing:
        done = True;
        for name in line[1]:
            done = done and names_done[name]
        if done:
            unbalanced = False
            weight = names_weights_map[line[1][0]]
            for name in line[1]:
                unbalanced = (unbalanced or names_weights_map[name] != weight)
            if unbalanced:
                print line[0]
                for name in line[1]:
                    print name, names_weights_map[name]
                raise Exception()
            else:
                names_done[line[0]] = True
                names_weights_map[line[0]] = weight * len(line[1]) + names_weights_map[line[0]]
                loadbearing.remove(line)