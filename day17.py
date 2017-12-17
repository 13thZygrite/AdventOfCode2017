#!/usr/bin/env python

step_size = 394

# Part 1

buffer = [0]
current = 0
for i in range(1, 2018):
    current = (current + step_size) % len(buffer)
    buffer.insert((current + 1), i)
    current += 1
print "Part 1: ", buffer[(buffer.index(2017) + 1) % len(buffer)]

# Part 2
answer = 0
current = 0
for i in range(1, 50000000):
    current = (current + step_size) % i
    if current == 0:
        answer = i
    current += 1

print "Part 2: ", answer