directions = {
    "^": (0, -1),
    "v": (0, 1),
    "<": (-1, 0),
    ">": (1, 0)
}

class Box2:
    def __init__(self,x,y, zone):
        self.x1 = x
        self.x2 = x + 1
        self.y = y
        self.zone = zone

    @property
    def position(self):
        return (self.x1,self.y)
    
    @property
    def gps(self):
        return 100*self.y + self.x1
    
    def check_move(self, x, y):
        next_pos1 = self.zone[self.y + y][self.x1 + (x*2)]

        if y != 0:
            next_pos2 = self.zone[self.y + y][self.x2]
            if next_pos1 == "." and next_pos2 == ".":
                return True
            if next_pos1 == "#" or next_pos2 == "#":
                return False
            
            side1 = True
            side2 = True

            if isinstance(next_pos1, Box2):
                side1 = next_pos1.check_move(0, y)
            if isinstance(next_pos2, Box2):
                side2 = next_pos2.check_move(0, y)
            return side1 and side2
        else:
            if next_pos1 == ".":
                return True
            if next_pos1 == "#":
                return False
            if isinstance(next_pos1, Box2):
                return next_pos1.check_move(x, 0)
            return True
            

    def move(self, x, y):
        next_pos1 = self.zone[self.y + y][self.x1 + (x*2)]
        
        if y != 0:
            next_pos2 = self.zone[self.y + y][self.x2]
            if isinstance(next_pos1, Box2):
                next_pos1.move(0, y)
            if isinstance(next_pos2, Box2):
                next_pos2.move(0, y)
            self.zone[self.y][self.x1] = "."
            self.zone[self.y][self.x2] = "."
            self.y += y
            self.zone[self.y][self.x1] = self
            self.zone[self.y][self.x2] = self
            return True
        else:
            if isinstance(next_pos1, Box2):
                next_pos1.move(x, 0)
            self.zone[self.y][self.x1] = "."
            self.zone[self.y][self.x2] = "."
            self.x1 += x
            self.x2 += x
            self.zone[self.y][self.x1] = self
            self.zone[self.y][self.x2] = self
            return True
                
    def __repr__(self):
        return "O"
    
def open_file2(file):
    zone = []
    boxes = []
    initial_pos = None
    moves = []
    with open(file) as f:
        z, m = f.read().split('\n\n')
        
        for y, line in enumerate(z.split('\n')):
            zone.append([])
            for x, c in enumerate(list(line)):
                if c == "#":
                    zone[y].extend(["#", "#"])
                elif c == ".":
                    zone[y].extend([".", "."])
                elif c == "O":
                    box2 = Box2(x, y, zone)
                    zone[y].extend([box2, box2])
                    boxes.append(box2)
                elif c == "@":
                    initial_pos = (x*2, y)
                    zone[y].extend(["@", "."])

        m = map(list,m.split('\n'))
        moves = [element for sublist in m for element in sublist]
        moves = list(map(lambda x: directions[x], moves))
    
    return zone, boxes, initial_pos, moves

initial_pos = None
zone = []
moves = []
boxes = []

zone, boxes, initial_pos, moves = open_file2("./day_15/example_day15.txt")
for line in zone:
    print("".join(map(str,line)))

current = [initial_pos[0], initial_pos[1]]

for move in moves:
    x,y = move
    next_pos = zone[current[1] + y][current[0] + x]

    if next_pos == ".": 
        zone[current[1]][current[0]] = "."
        current[0] += x
        current[1] += y
        zone[current[1]][current[0]] = "@"
    elif next_pos == "#":
        continue
    elif isinstance(next_pos, Box2):
        if not next_pos.check_move(x , y):
            continue
        next_pos.move(x, y)
        zone[current[1]][current[0]] = "."
        current[0] += x
        current[1] += y
        zone[current[1]][current[0]] = "@"
    
        for line in zone:
            print("".join(map(str,line)))
        print("---------------------------")