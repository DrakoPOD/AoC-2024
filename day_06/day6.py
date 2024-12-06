import os, platform
import time
import numpy as np

def clear():
   if platform.system() == 'Windows':
      os.system('cls')
   else:
      os.system('clear')

zone = []

with open('./example_day06.txt') as f:
    for line in f:
        zone.append([0] + list(line.strip()) + [0])
    zeros = [0] * len(zone[0])
    zone.insert(0, zeros)
    zone.append(zeros)

pos = []

for i in range(1, len(zone) - 1):
    for j in range(1, len(zone[i]) - 1):
        point = zone[i][j]
        if point != '.' and point != '#' and point != 0:
            pos = [i, j]
            break

    if pos:
        break

directions = ['^','>','v','<']
current_direction = zone[pos[0]][pos[1]]

def move(pos):
    global current_direction
    next_pos = pos.copy()
    if current_direction == '^':
        next_pos[0] -= 1
        if zone[next_pos[0]][next_pos[1]] == '#':
            current_direction = '>'
        elif zone[next_pos[0]][next_pos[1]] == 0:
            return True
        else:
            pos[0] -= 1
    elif current_direction == '>':
        next_pos[1] += 1
        if zone[next_pos[0]][next_pos[1]] == '#':
            current_direction = 'v'
        elif zone[next_pos[0]][next_pos[1]] == 0:
            return True
        else:
            pos[1] += 1
    elif current_direction == 'v':
        next_pos[0] += 1
        if zone[next_pos[0]][next_pos[1]] == '#':
            current_direction = '<'
        elif zone[next_pos[0]][next_pos[1]] == 0:
            return True
        else:
            pos[0] += 1
    elif current_direction == '<':
        next_pos[1] -= 1
        if zone[next_pos[0]][next_pos[1]] == '#':
            current_direction = '^'
        elif zone[next_pos[0]][next_pos[1]] == 0:
            return True
        else:
            pos[1] -= 1

    return False

steps = np.zeros((len(zone), len(zone[0])), dtype=int)

steps[5][5] = 1
print(np.matrix(steps))
# while True:
#     steps[pos[0]][pos[1]] = 1
#     clear()
#     print(np.matrix(steps))
#     time.sleep(0.5)
#     if move(pos):
#         break