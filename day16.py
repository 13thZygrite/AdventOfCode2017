#!/usr/bin/env python
import collections
import copy

with open("input_day16") as f:
    input = f.readlines()
    
moves = input[0].split(",");

original_state = collections.deque("abcdefghijklmnop")
state = collections.deque("abcdefghijklmnop");

for move in moves:
    if (move[0] == "s"):
        state.rotate(int(move[1:]))
    elif (move[0] == "x"):
        first, second = move[1:].split("/")
        state[int(first)] , state[int(second)] = state[int(second)], state[int(first)]
    elif (move[0] == "p"):
        first, second = move[1:].split("/")
        # Slow as balls, should have used python 3
        first_index = list(state).index(first)
        second_index = list(state).index(second)
        state[first_index] , state[second_index] = state[second_index], state[first_index]
print "Part 1: ", state

state = collections.deque("abcdefghijklmnop");

states = [state]
while(True):
    for move in moves:
        if (move[0] == "s"):
            state.rotate(int(move[1:]))
        elif (move[0] == "x"):
            first, second = move[1:].split("/")
            state[int(first)] , state[int(second)] = state[int(second)], state[int(first)]
        elif (move[0] == "p"):
            first, second = move[1:].split("/")
            # Slow as balls, should have used python 3
            first_index = list(state).index(first)
            second_index = list(state).index(second)
            state[first_index] , state[second_index] = state[second_index], state[first_index]
    states.append(copy.deepcopy(state))
    if (state == original_state):
        break
print "Part 2: ", states[1000000000 % (len(states) - 1)] 