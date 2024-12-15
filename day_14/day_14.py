import re
import os
import time

class Robot:
    def __init__(self,x,y,vx, vy, max_x, max_y):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.max_x = max_x
        self.max_y = max_y

    def move(self):
        self.x += self.vx
        self.y += self.vy

        if self.x < 0:
            self.x = self.max_x + self.x

        if self.y < 0:
            self.y = self.max_y + self.y

        if self.x >= self.max_x:
            self.x = self.x - self.max_x

        if self.y >= self.max_y:
            self.y = self.y - self.max_y

    @property
    def quadrant(self):
        x = self.max_x // 2 
        y = self.max_y // 2 

        if self.x < x and self.y < y:
            return 1
        elif self.x < x and self.y > y:
            return 2
        elif self.x > x and self.y < y:
            return 3
        elif self.x > x and self.y > y:
            return 4
        else:
            return 0

    def __repr__(self):
        return f"({self.x},{self.y})"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
robots = []

with open('data_day14.txt') as f:
    for line in f:
        x,y,vx,vy = map(int,re.findall(r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)',line)[0])
        robots.append(Robot(x,y,vx,vy,101,103))

for i in range(10000):
    zone = []
    for j in range(103):
        zone.append(['.' for _ in range(101)])

    for robot in robots:
        zone[robot.y][robot.x] = '#'

        robot.move()

    if i > 8000:
        for row in zone:
            print()
            for col in row:
                print(col,end='')
            print()

        print(f"Step: {i}")
        input("Presiona Enter para continuar...")
    clear()