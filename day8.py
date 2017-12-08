#!/usr/bin/env python

with open("input_day8") as f:
    input = f.readlines()
    
input = [x.strip() for x in input]

split = [line.split(" ") for line in input]

registers = {}

for instruction in split:
    registers[instruction[0]] = 0
max_value = 0
# Part 1 and 2
for instruction in split:
    condition_holds = False
    if (instruction[5] == "=="):
        condition_holds = (registers[instruction[4]] == int(instruction[6]))
    elif (instruction[5] == "!="):
        condition_holds = (registers[instruction[4]] != int(instruction[6]))
    elif (instruction[5] == ">"):
        condition_holds = (registers[instruction[4]] > int(instruction[6]))
    elif (instruction[5] == ">="):
        condition_holds = (registers[instruction[4]] >= int(instruction[6]))
    elif (instruction[5] == "<"):
        condition_holds = (registers[instruction[4]] < int(instruction[6]))
    elif (instruction[5] == "<="):
        condition_holds = (registers[instruction[4]] <= int(instruction[6]))
    if (not condition_holds):
        continue
    
    if (instruction[1] == "dec"):
        registers[instruction[0]] -= int(instruction[2])
    elif (instruction[1] == "inc"):
        registers[instruction[0]] += int(instruction[2])
        
    if (registers[instruction[0]] > max_value):
        max_value = registers[instruction[0]]

print "Part 1:", max(registers.values())
print "Part 2:", max_value