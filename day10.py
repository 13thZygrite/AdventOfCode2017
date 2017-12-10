#!/usr/bin/env python

input = "76,1,88,148,166,217,130,0,128,254,16,2,130,71,255,229"

lengths = map(int, input.split(","))

state = range(256)

# Part 1

skip_size = 0
pos = 0

for length in lengths:
    for i in range(length // 2):
        state[(pos + i) % 256], state[(pos + length - i - 1) % 256] = state[(pos + length - i - 1) % 256], state[(pos + i) % 256]
    pos = (pos + length + skip_size) % 256
    skip_size += 1

print "Part 1: ", state[0] * state[1]

#input = ""

chars = map(ord, list(input.strip()))
chars.extend([17, 31, 73, 47, 23])
state = range(256)
# Part 2

skip_size = 0
pos = 0

for k in range(64):
    for length in chars:
        for i in range(length // 2):
            state[(pos + i) % 256], state[(pos + length - i - 1) % 256] = state[(pos + length - i - 1) % 256], state[(pos + i) % 256]
        pos = (pos + length + skip_size) % 256
        skip_size += 1
        
dense_hash = []
for i in range (16):
    value = state[i*16]
    for j in range(15):
        value = value ^ state[i*16+j+1]
    dense_hash.append(value)

output = "Part 2: "
for char in dense_hash:
        hexd = hex(char)
        hexd = hexd[2:]
        if len(hexd) == 1:
            hexd = "0" + hexd
        output += hexd
print output