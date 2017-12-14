#!/usr/bin/env python

input = "wenycdww-"

def knot_hash(input):
    chars = map(ord, list(input.strip()))
    chars.extend([17, 31, 73, 47, 23])
    state = range(256)

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

    output = ""
    for char in dense_hash:
            hexd = hex(char)
            hexd = hexd[2:]
            if len(hexd) == 1:
                hexd = "0" + hexd
            output += hexd
    return output

# Tests

assert(knot_hash("") == "a2582a3a0e66e6e86e3812dcb672a272")
assert(knot_hash("AoC 2017") == "33efeb34ea91902bb2f59c9920caa6cd")

# Part 1

hashes =[ format(int(knot_hash(input + str(i)), 16), '0128b') for i in range(128) ]
popcount = 0
for hash in hashes:
    popcount += hash.count("1")
print popcount

# Part 2

to_do = set()
for i in range(128):
    for j in range(128):
        to_do.add((i, j))

regions = 0;
while (len(to_do) > 0):
    checking = [to_do.pop()]
    if (hashes[checking[0][0]][checking[0][1]] == "1"):
        regions +=1
        while (len(checking) > 0):
            val = checking.pop()
            to_do.discard(val)
            square = hashes[val[0]][val[1]]
            if (square == "1"):
                print ((val[0] - 1, val[1]) in to_do)
                if ((val[0] - 1) > -1) and ((val[0] - 1, val[1]) in to_do):
                    checking.append((val[0] - 1, val[1]))
                if ((val[0] + 1) < 128) and ((val[0] + 1, val[1]) in to_do):
                    checking.append((val[0] + 1, val[1]))
                if ((val[1] - 1) > -1) and ((val[0], val[1] -1 ) in to_do):
                    checking.append((val[0], val[1] - 1))
                if ((val[1] + 1) < 128) and ((val[0], val[1] + 1) in to_do):
                    checking.append((val[0], val[1] + 1))
    else:
        to_do.discard(checking[0])
        
    #print regions
print regions