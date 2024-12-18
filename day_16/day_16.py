import heapq

class Node:
    def __init__(self, x,y, end):
        self.x = x
        self.y = y
        self.end = end
        self.start = False
        self.path = False
        self.cost = float('inf')
        self.prev = []
        self.direction = None
        self.real_cost = float('inf')

    def __repr__(self):
        if self.end:
            return 'E'
        if self.start:
            return 'S'
        if self.path:
            return self.direction
        return '.'
    
    def __lt__(self, other):
        return self.cost < other.cost
    
class Wall:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "#"

def open_file(file):
    zone = []
    start = None
    end = None
    with open(file) as f:
        for y,line in enumerate(f.readlines()):
            zone.append([])
            for x,block in enumerate(line):
                if block == ".":
                    zone[y].append(Node(x,y, zone, False))
                elif block == "#":
                    zone[y].append(Wall(x,y))
                elif block == "S":
                    node = Node(x,y, False)
                    zone[y].append(node)
                    start = node
                    start.cost = 0
                    start.direction = ">"
                    start.start = True
                elif block == "E":
                    node = Node(x,y, zone, True)
                    zone[y].append(node)
                    end = node
    return zone, start, end

def dijkstra_2(zone, start, end):
    open_list = [start]
    paths = []

    while open_list:
        current = heapq.heappop(open_list)

        for x,y,d in [(0,1,"v"), (0,-1,"^"), (1,0,">"), (-1,0,"<")]:
            node = zone[current.y + y][current.x + x]
            
            if isinstance(node, Wall):
                continue

            additional_cost = 0 if d == current.direction else 1000

            new_cost = current.cost + 1 + additional_cost

            if new_cost <= node.cost:
                if new_cost < node.cost:
                    node.cost = new_cost
                    node.prev = []
                node.prev.append(current)
                node.real_cost = 1 + additional_cost
                node.direction = d
                heapq.heappush(open_list,node)

    def find_paths(node, path, paths):
        if node == start:
            paths.append(path[::-1])
            return

        for parent in node.prev:
            parent.path = True
            find_paths(parent, path + [node], paths)

    paths = []
    find_paths(end, [], paths)
    return paths    

zone, start, end = open_file("day_16/example_day16.txt")
path = dijkstra_2(zone,start,end)

for row in zone:
    for block in row:
        print(block, end="")
    print()

    ###############
    #.......#....E#
    #.#.###.#.###^#
    #.....#.#...#^#
    #.###.#####.#^#
    #.#.#.......#^#
    #.#.#####.###^#
    #....^>>>>>>#^#
    ###.#^#####v#^#
    #...#^....#v#^#
    #.#.#^###.#v#^#
    #^>>>>#...#v#^#
    #^###.#.#.#v#^#
    #S..#.....#v>>#
    ###############