#!/usr/bin/env python

with open("input_day19") as f:
    input = f.readlines()
position = [0, input[0].index("|")] #[0, 27]

up = (-1, 0)
down = (1, 0)
left = (0, -1)
right = (0, 1)

direction = down
answer=""
count = 0
while(True):
    count += 1
    position[0] += direction[0]
    position[1] += direction[1]
    if input[position[0]][position[1]] == " ":
        break
    elif input[position[0]][position[1]].isalpha():
        answer += input[position[0]][position[1]]
    elif input[position[0]][position[1]] == "+":
        # Change direction
        if direction == up or direction == down:
            if input[position[0]][position[1] - 1] == "-":
                direction = left
                continue
            elif input[position[0]][position[1] + 1] == "-":
                direction = right
                continue
        if direction == left or direction == right:
            if input[position[0] + 1][position[1]] == "|":
                direction = down
                continue
            elif input[position[0] - 1][position[1]] == "|":
                direction = up
                continue
                
print "Part 1: ", answer
print "Part 2: ", count