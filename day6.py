#!/usr/bin/env python

input = "4 1 15 12 0 9 9 5 5 8 7 3 14 5 12 3"

# Part 1

state = map(int, input.split(" "))
length = len(state)
configs = set()
configs.add(tuple(state))
current_size = len(configs)
count = 0;
while (1):
    count += 1
    max_index = 0;
    for i in range(len(state)):
        if state[i] > state[max_index]:
            max_index = i
    redist = state[max_index]
    state[max_index] = 0
    for i in range(redist):
        state[(max_index + i + 1) % length] += 1
    configs.add(tuple(state))
    if current_size == len(configs):
        print "part 1:", count
        break
    current_size = len(configs)

# Part 2
count = 0
desired = tuple(state)
while (1):
    count += 1
    max_index = 0;
    for i in range(len(state)):
        if state[i] > state[max_index]:
            max_index = i
    redist = state[max_index]
    state[max_index] = 0
    for i in range(redist):
        state[(max_index + i + 1) % length] += 1
    if desired == tuple(state):
        print "part 2:", count
        break
