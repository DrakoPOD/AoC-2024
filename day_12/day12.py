class Plot:
    def __init__(self,x,y, name):
        self.x = x
        self.y = y
        self.name = name
        self.adjacent = []
        self.checked = False
        self.area = None
        self.right = True
        self.bottom = True
        self.left = True
        self.top = True

    @property
    def perimeter(self):
        return 4 - len(self.adjacent)
    
    def __repr__(self):
        return self.name
    
class Area:
    def __init__(self, name):
        self.plots = []
        self.name = name
        self.x = None
        self.y = None
        self.h = None
        self.w = None
        self.zones = None
        self.sides = []

    def add_plot(self, plot):
        if plot not in self.plots:
            plot.checked = True
            self.plots.append(plot)
            plot.area = self
            
        for adjacent in plot.adjacent:
            if adjacent not in self.plots:
                if not adjacent.checked:
                    adjacent.checked = True
                    self.plots.append(adjacent)
                    plot.area = self
                    self.add_plot(adjacent)

    @property
    def area(self):
        return len(self.plots)
    
    @property
    def perimeter(self):
        return sum([plot.perimeter for plot in self.plots])
    
    @property
    def price(self):
        return self.area * self.perimeter
    
    @property
    def price_discount(self):
        return self.total_sides * self.area
    
    @property
    def total_sides(self):
        if self.x is None:
            self.set_pos()
        # top
        top = 0
        for y in range(self.y, self.y + self.h):
            row = filter(lambda plot: plot.y == y, self.plots)
            row = sorted(row, key=lambda plot: plot.x)

            if len(row) == 1:
                if row[0].top:
                    top += 1
                    continue

            contiguos = False
            for i in range(len(row) - 1):
                plot_1 = row[i]
                plot_2 = row[i + 1]


                if not contiguos and plot_1.top:
                    top += 1
                    contiguos = True
                
                diff = plot_2.x - plot_1.x
                if diff > 1:
                    contiguos = False

                if not plot_1.top:
                    contiguos = False
                
                if not contiguos and plot_2.top:
                    top += 1
                    contiguos = True

        # bottom
        bottom = 0
        for y in range(self.y, self.y + self.h):
            row = filter(lambda plot: plot.y == y, self.plots)
            row = sorted(row, key=lambda plot: plot.x)

            contiguos = False
            if len(row) == 1:
                if row[0].bottom:
                    bottom += 1
                    continue
            for i in range(len(row) - 1):
                plot_1 = row[i]
                plot_2 = row[i + 1]

                if not contiguos and plot_1.bottom:
                    bottom += 1
                    contiguos = True

                diff = plot_2.x - plot_1.x
                if diff > 1:
                    contiguos = False

                if not plot_1.bottom:
                    contiguos = False
                
                if not contiguos and plot_2.bottom:
                    bottom += 1
                    contiguos = True


        # left
        left = 0
        for x in range(self.x, self.x + self.w):
            column = filter(lambda plot: plot.x == x, self.plots)
            column = sorted(column, key=lambda plot: plot.y)
            contiguos = False
            if len(column) == 1:
                if column[0].left:
                    left += 1
                    continue
            for i in range(len(column) - 1):
                plot_1 = column[i]
                plot_2 = column[i + 1]

                if not contiguos and plot_1.left:
                    left += 1
                    contiguos = True

                diff = plot_2.y - plot_1.y
                if diff > 1:
                    contiguos = False

                if not plot_1.left:
                    contiguos = False
                
                if not contiguos and plot_2.left:
                    left += 1
                    contiguos = True


        # right
        right = 0
        for x in range(self.x, self.x + self.w):
            column = filter(lambda plot: plot.x == x, self.plots)
            column = sorted(column, key=lambda plot: plot.y)

            contiguos = False
            if len(column) == 1:
                if column[0].right:
                    right += 1
                    continue
            for i in range(len(column) - 1):
                plot_1 = column[i]
                plot_2 = column[i + 1]


                if not contiguos and plot_1.right:
                    right += 1
                    contiguos = True
                
                diff = plot_2.y - plot_1.y
                if diff > 1:
                    contiguos = False

                if not plot_1.right:
                    contiguos = False
                
                if not contiguos and plot_2.right:
                    right += 1
                    contiguos = True


        self.sides = [top, bottom, left, right]
        return top + bottom + left + right

    def set_pos(self):
        self.x = min([x.x for x in self.plots])
        self.y = min([y.y for y in self.plots])
        self.h = max([y.y for y in self.plots]) - self.y + 1
        self.w = max([x.x for x in self.plots]) - self.x + 1
    
    def __str__(self):
        return f'{self.name} area: {self.area} perimeter: {self.perimeter} price: {self.price} total_sides: {self.total_sides}'

    def __repr__(self):
        return self.name
    
zone = []

with open('day_12/example_day12.txt') as f:
    for i, line in enumerate(f):
        zone.append([Plot(j, i, name) for j,name in enumerate(line.strip())])

for row in zone:
    for plot in row:
        for i, j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ny, nx = plot.y + i, plot.x + j
            if 0 <= ny < len(zone) and 0 <= nx < len(row):  # Verifica límites correctos
                if plot.name == zone[ny][nx].name:
                    plot.adjacent.append(zone[ny][nx])

                    if i == 1:
                        plot.bottom = False
                    elif i == -1:
                        plot.top = False
                    elif j == 1:
                        plot.right = False
                    elif j == -1:
                        plot.left = False

areas = []

for row in zone:
    for plot in row:
        if plot.checked == False:
            plot.checked = True
            area = Area(plot.name)
            area.zones = zone
            area.add_plot(plot)
            areas.append(area)

for area in areas:
    area.total_sides
    print(f"area: {area.name} price {area.area} * {area.total_sides} = {area.price_discount} -- {area.sides}")