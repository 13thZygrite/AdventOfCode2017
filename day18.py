#!/usr/bin/env python

with open("input_day18") as f:
    input = f.readlines()
    
input = [line.split() for line in input]
registers = {}
current = 0
last_played_sound = -1

def value(val):
    # Returns either the value of the register or the int value
    if val.isalpha():
        return registers[val]
    else:
        return int(val)
def value2(val, machine):
    # Returns either the value of the register or the int value
    if val.isalpha():
        return registers[machine][val]
    else:
        return int(val)
        

while(True):
    instr = input[current]
    if (instr[0] == "snd"):
        last_played_sound = registers[instr[1]]
        current += 1
        continue
    elif (instr[0] == "set"):
        registers[instr[1]] = value(instr[2])
        current += 1
        continue
    elif (instr[0] == "add"):
        if instr[1] in registers:
            registers[instr[1]] += value(instr[2])
        else:
            registers[instr[1]] = value(instr[2])
        current += 1
        continue
    elif (instr[0] == "mul"):
        if instr[1] in registers:
            registers[instr[1]] *= value(instr[2])
        else:
            registers[instr[1]] = 0
        current += 1
        continue
    elif (instr[0] == "mod"):
        if instr[1] in registers:
            registers[instr[1]] %= value(instr[2])
        else:
            registers[instr[1]] = 0
        current += 1
        continue
    elif (instr[0] == "rcv"):
        if value(instr[1]) > 0:
            print "Part 1: ", last_played_sound
            break
    else:
        assert((instr[0] == "jgz"))
        if value(instr[1]) > 0:
            current += value(instr[2])
            continue
        current += 1
        continue

def value2(val):
    # Returns either the value of the register or the int value
    if val.isalpha():
        return registers[current_machine][val]
    else:
        return int(val)
        
# Part 2
currents = [0, 1]
current_machine = 0
registers = [{"p":0}, {"p":1}]
queues = [[],[]]
sent = 0
locked =[False, False]
just_switched = False

while(True):
    instr = input[currents[current_machine]]
    print current_machine, instr
    if (instr[0] == "snd"):
        queues[1 - current_machine].append(registers[current_machine][instr[1]])
        currents[current_machine] += 1
        if current_machine == 1:
            sent += 1
        continue
    elif (instr[0] == "set"):
        registers[current_machine][instr[1]] = value2(instr[2])
        currents[current_machine] += 1
        continue
    elif (instr[0] == "add"):
        if instr[1] in registers[current_machine]:
            registers[current_machine][instr[1]] += value2(instr[2])
        else:
            registers[current_machine][instr[1]] = value2(instr[2])
        currents[current_machine] += 1
        continue
    elif (instr[0] == "mul"):
        if instr[1] in registers[current_machine]:
            registers[current_machine][instr[1]] *= value2(instr[2])
        else:
            registers[current_machine][instr[1]] = 0
        currents[current_machine] += 1
        continue
    elif (instr[0] == "mod"):
        if instr[1] in registers[current_machine]:
            registers[current_machine][instr[1]] %= value2(instr[2])
        else:
            registers[current_machine][instr[1]] = 0
        currents[current_machine] += 1
        continue
    elif (instr[0] == "rcv"):
        if queues[current_machine]:
            just_switched = False
            locked[current_machine] = False
            registers[current_machine][instr[1]] = queues[current_machine].pop(0)
            currents[current_machine] += 1
            continue
        elif just_switched:
            print "Part 2 :", sent
            break
        else:
            just_switched = True
            current_machine = 1 - current_machine
            continue
    else:
        assert((instr[0] == "jgz"))
        if value2(instr[1]) > 0:
            currents[current_machine] += value2(instr[2])
            continue
        currents[current_machine] += 1
        continue