#!/usr/bin/env python

gen_a_state = 699
gen_b_state = 124

judge_total = 0

for i in range(40000000):
    gen_a_state = (gen_a_state * 16807) % 2147483647
    gen_b_state = (gen_b_state * 48271) % 2147483647
    if (gen_a_state & 0xffff == gen_b_state & 0xffff):
        judge_total += 1
print judge_total

# Part 2
gen_a_state = 699
gen_b_state = 124


judge_a = -1
judge_b = -1
judge_total = 0
judge_compared = 0

while judge_compared < 5000000:
    if (judge_a == -1):
        gen_a_state = (gen_a_state * 16807) % 2147483647
        if (gen_a_state % 4 == 0):
            judge_a = gen_a_state
    if (judge_b == -1):
        gen_b_state = (gen_b_state * 48271) % 2147483647
        if (gen_b_state % 8 == 0):
            judge_b = gen_b_state
    if (judge_a != -1 and judge_b != -1):
        if (gen_a_state & 0xffff == gen_b_state & 0xffff):
            judge_total += 1
        judge_a = -1
        judge_b = -1
        judge_compared += 1
print judge_total