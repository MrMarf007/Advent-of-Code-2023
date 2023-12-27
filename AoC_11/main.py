import numpy as np

class P1:
    def parse(file):
        res = []
        galaxies = []
        for f in file:
            res.append([*f.strip()])
        res = np.array(res)
        # print(res, len(res), len(res[0]))
        res = P1.expand(res)
        for i in range(len(res)):
            for j in range(len(res[0])):
                if res[i][j] == '#':
                    galaxies.append([i, j])
        return (galaxies, res)
    
    def expand(data):
        add = []
        add2 = []
        i = 0
        while i < len(data):
            line = data[i]
            if P1.empty(line):
                #print("empty row", i)
                add.append(i)
            i += 1
        i = 0
        data = np.transpose(data)
        while i < len(data):
            line = data[i]
            if P1.empty(line):
                #print("empty col", i)
                add2.append(i)
            i += 1
        data = np.transpose(data)
        add.reverse()
        for j in add:
            data = np.insert(data, j, ['.'] * len(data[0]), axis=0)
        data = np.transpose(data)
        add2.reverse()
        for j in add2:
            data = np.insert(data, j, ['.'] * len(data[0]), axis=0)
        data = np.transpose(data)
        #print(data, len(data), len(data[0]))
        return data

    def empty(line):
        return all([c == '.' for c in line])
    
    def run(data):
        (galaxies, map) = data
        paths = {}
        for (x,y) in galaxies:
            for (x2,y2) in galaxies:
                if (x,y) != (x2,y2):
                    (a,b) = (x + y * len(map[0]),x2 + y2 * len(map[0]))
                    if a > b: (a,b) = (b,a)
                    paths[(a,b)] = P1.path(map, (x,y), (x2,y2))
        # print(paths, len(paths))
        return(sum(paths.values()))
    
    def path(map, g1, g2):
        #print (g1, g2)
        (x1, y1) = g1
        (x2, y2) = g2
        (dx, dy) = ((x1 - x2), (y1 - y2))
        # print(abs(dx) + abs(dy))
        return (abs(dx) + abs(dy))

# =============================================================================== #
#                                      Part 2                                     #
# =============================================================================== #
    
class P2:
    def parse(file):
        res = []
        data = {}
        galaxies = []
        for f in file:
            res.append([*f.strip()])
        res = np.array(res)
        # print(res, len(res), len(res[0]))
        res = P2.expand(res)
        for i in range(len(res)):
            for j in range(len(res[0])):
                data[(i,j)] = res[i][j]
                if data[(i,j)] == '#':
                    galaxies.append([i, j])
        return (galaxies, data, (len(res), len(res[0])))
    
    def expand(data):
        add = []
        add2 = []
        i = 0
        while i < len(data):
            line = data[i]
            if P1.empty(line):
                #print("empty row", i)
                add.append(i)
            i += 1
        i = 0
        data = np.transpose(data)
        while i < len(data):
            line = data[i]
            if P1.empty(line):
                #print("empty col", i)
                add2.append(i)
            i += 1
        data = np.transpose(data)
        add.reverse()
        for j in add:
            data[j] = ['X'] * len(data[0])
        data = np.transpose(data)
        add2.reverse()
        for j in add2:
            data[j] = ['X'] * len(data[0])
        data = np.transpose(data)
        # print(data, len(data), len(data[0]))
        return data
    
    def run(data):
        (galaxies, map, (sy, sx)) = data
        paths = {}
        for (x,y) in galaxies:
            for (x2,y2) in galaxies:
                if (x,y) != (x2,y2):
                    (a,b) = (x + y * sx,x2 + y2 * sx)
                    if a > b: (a,b) = (b,a)
                    c = P2.path(map, (x,y), (x2,y2))
                    # print((a,b), (x,y), (x2,y2), c)
                    paths[(a,b)] = c
        # print(paths, len(paths))
        return(sum(paths.values()))
    
    def path(map, g1, g2):
        cost = 0
        (x1, y1) = g1
        (x2, y2) = g2
        (mx, my) = (x1,y2)
        if (y1 > y2): (y1,y2) = (y2,y1)
        if (x1 > x2): (x1,x2) = (x2,x1)
        for i in range(y1, y2):
            # print(map[(mx, i)], (mx, i), end=" ")
            if map[(mx, i)] == 'X':
                cost += 1000000
            if map[(mx, i)] == '.' or map[(mx, i)] == '#':
                cost += 1
            # print (cost)
        for i in range(x1, x2):
            
            # print(map[(i, my)], (i, my), end=" ")
            if map[(i,my)] == 'X':
                cost += 1000000
            if map[(i,my)] == '.' or map[(i,my)] == '#':
                cost += 1
            # print (cost)
        return (cost)
    
    # X costs 1000000


import time
t1 = time.time()

file = open("input.txt", "r")
data = P1.parse(file)
p1 = P1.run(data)
print("\n================================{ Part 1 result: ", p1, "}================================\n")

t2 = time.time()

file = open("input.txt", "r")
data = P2.parse(file)
p2 = P2.run(data)

t3 = time.time()
print("\n================================{ Part 2 result: ", p2, "}================================\n")
print("P1 time: ", (t2 - t1), "\n")
print("P2 time: ", (t3 - t2), "\n")
print("Part 1 result: ", p1, "\n")
print("Part 2 result: ", p2, "\n")