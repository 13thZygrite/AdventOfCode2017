#!/usr/bin/env python
from operator import itemgetter

with open("input_day20") as f:
    input = f.readlines()
    
particles = []
for line in input:
    data = line.strip().split(", ")
    position = map(int, data[0][3:-1].split(","))
    velocity = map(int, data[1][3:-1].split(","))
    acceleration = map(int, data[2][3:-1].split(","))
    particles.append([position, velocity, acceleration])
indices = []
for i in range(len(particles)):
    if sum(map(abs, particles[i][2])) == 1:
        indices.append(i)

# Solved the rest by hand, closest in the long run is whichever has the minimum velocity once all particles are actually accelerating
#p=<-1103,92,1785>, v=<49,-4,-97>, a=<1,0,0>  index: 279, vel 150 + step
#p=<2978,2082,4280>, v=<-135,-88,-178>, a=<1,0,0> index:308 vel min: step 135, 266
#p=<2030,-4343,-355>, v=<-69,145,25>, a=<0,0,-1> index:435 vel min: 204 at step 25
# So at step 135, all three's velocities will be increasing every step and 308 is the smallest
print "Part 1: ", 308

# Part 2

for _ in range(20000): # Assume it stabilizes after a certain number of repeats. 20k is probably overkill.
    particles.sort(key=itemgetter(0))
    # Remove duplicates:
    particles = [particles[i] for i in range(len(particles)) if i == 0 or (particles[i][0] != particles[i - 1][0] and particles[i][0] != particles[(i + 1) % len(particles)][0])]
    for particle in particles:
        particle[1][0] += particle[2][0]
        particle[1][1] += particle[2][1]
        particle[1][2] += particle[2][2]
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[0][2] += particle[1][2]
print "Part 2:", len(particles)