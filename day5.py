#!/usr/bin/env python
# Part 1
with open("input_day5") as f:
    input = f.readlines()

input = [x.strip() for x in input]
    
input1 = map(int, input)
count = 0
index = 0
while(1):
    current = input1[index]
    input1[index] += 1
    index += current
    count += 1
    if (index < 0 or index > len(input1) - 1):
        break
print count


# Part 2
input2 = map(int, input)
count = 0
index = 0
while(1):
    current = input2[index]
    if (current > 2):
        input2[index] -= 1
    else:
        input2[index] += 1
    index += current
    count += 1
    if (index < 0 or index > len(input2) - 1):
        break
print count