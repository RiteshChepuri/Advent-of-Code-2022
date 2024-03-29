#!/usr/bin/python3

import sys
from collections import defaultdict
with open("day10.in") as file:
    data = file.read().strip()
    lines = data.split('\n')


G = [['?' for _ in range(40)] for _ in range(6)]
p1 = 0
x = 1
t = 0

def handle_tick(t, x):
    global p1
    global G
    t1 = t-1
    G[t1//40][t1%40] = ('#' if abs(x-(t1%40))<=1 else ' ')
    if t in [20, 60, 100, 140, 180, 220]:
        p1 += x*t

for line in lines:
    words = line.split()
    if words[0] == 'noop':
        t += 1
        handle_tick(t,x)
    elif words[0] == 'addx':
        t += 1
        handle_tick(t,x)
        t += 1
        handle_tick(t,x)
        x += int(words[1])
print(p1)
for r in range(6):
    print(''.join(G[r]))
