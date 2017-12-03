#!/usr/bin/env python

input = 368078

# Part 1

n=1

while (((2*n - 1)* (2*n - 1)) < input):
    n += 1
print n, (2*n-1)*(2*n-1) # prints 304, 368449

# 368449 is at (304, 304) -> 368145 is at (304, 0)
# so distance is 145-78 + 304 = 371


# Part 2

def add_surroundings(grid, x, y):
    grid[x][y] += grid[x-1][y-1]
    grid[x][y] += grid[x-1][y]
    grid[x][y] += grid[x-1][y+1]
    grid[x][y] += grid[x][y-1]
    grid[x][y] += grid[x][y+1]
    grid[x][y] += grid[x+1][y-1]
    grid[x][y] += grid[x+1][y]
    grid[x][y] += grid[x+1][y+1]
    if grid[x][y] > 368449:
        raise Exception(grid[x][y])

grid = [[0 for x in range(101)] for y in range (101)]
# start point is (50, 50)
grid[50][50] = 1
spiral_count = 1
current_pos = [0,0]
try:
    while (1):
        current_pos[0] += 1
        add_surroundings(grid, current_pos[0]+ 50, current_pos[1]+ 50)
        for i in range(spiral_count*2 - 1): # move up
            current_pos[1] += 1
            add_surroundings(grid, current_pos[0]+ 50, current_pos[1]+ 50)
        for i in range((spiral_count * 2)): # move left
            current_pos[0] -= 1
            add_surroundings(grid, current_pos[0]+ 50, current_pos[1]+ 50)
        for i in range((spiral_count * 2)): # move down
            current_pos[1] -= 1
            add_surroundings(grid, current_pos[0]+ 50, current_pos[1]+ 50)
        for i in range((spiral_count * 2)): # move right
            current_pos[0] += 1
            add_surroundings(grid, current_pos[0]+ 50, current_pos[1]+ 50)
        spiral_count += 1
except Exception as err:
    answer, = err.args
    print answer