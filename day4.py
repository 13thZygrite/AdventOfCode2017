#!/usr/bin/env python
with open("input_day4") as f:
    input = f.readlines()

input = [x.strip() for x in input]
    
print len(input)
# Part 1
count = 0
for phrase in input:
    split = phrase.split( )
    split.sort()
    for i in range(len(split) - 1):
        if split[i] == split[i + 1]:
            break
        if i == len(split) - 2:
            count += 1
    
print count
# Part 2
count = 0
for phrase in input:
    split = phrase.split( )
    sort_split = []
    for word in split:
        word = "".join(sorted(word))
        sort_split.append(word)
    sort_split.sort()
    for i in range(len(sort_split) - 1):
        if sort_split[i] == sort_split[i + 1]:
            break
        if i == len(sort_split) - 2:
            count += 1
print count