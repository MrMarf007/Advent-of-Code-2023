# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

class P1:
    def parse(file):
        grid = []     #2D array representing the grid (y, x)
        start = (0,0)
        for f in file:
            if "S" in f: start = (len(grid), f.index("S"))
            grid.append([*f.strip()])
        print (grid, start)
        return (grid, start)

    def run(data):
        (grid, startPos) = data
        moves = P1.genMoves(grid, startPos, None)
        paths = []
        for m in moves:
            paths.append([startPos, m])
        while not P1.collide(paths):
            paths = P1.step(grid, paths)
        print(paths)
        return(len(paths[0])-1)
    
    def step(grid, paths):
        newPaths = []
        for path in paths:
            #print(path)
            previous = path[-2]
            source = path[-1]
            newMoves = P1.genMoves(grid, source, previous)
            newPaths.append(path + newMoves)
            #print(path + newMoves)
        return newPaths
        
    def collide(paths):
        lst = [p[-1] for p in paths]
        return (lst[:-1] == lst[1:])
        
    def genMoves(grid, pos, previous):
        (sy,sx) = pos
        paths = []
        temp = [0,0,0,0]
        ts = [-1,0,1,0]
        for i in range(4): # 0 up, 1 right, 2 down, 3 left
            paths.append((i,(sy,sx),(sy+ts[i],sx+ts[(i+1)%4])))
        #print("moves generated: ", paths)
        paths = P1.validateMoves(grid, paths, previous)
        return paths

    def validateMoves(grid, moves, previous):
        newMoves = []
        #print (moves)
        for m in moves:
            (direction,(sy,sx),(dy,dx)) = m
            #print("validating", direction, dy, dx, " -    ", end="")
            if dy < 0 or dy >= len(grid) or dx < 0 or dx >= len(grid[0]): 
                #print("Out of bounds")
                continue
            sourceShape = P1.getShape(grid[sy][sx])
            #print(sourceShape, end="")
            destShape = P1.getShape(grid[dy][dx])
            #print(destShape, end="")
            if sourceShape[direction] == 1 and destShape[(direction+2)%4] == 1 and (dy,dx) != previous:
                #print(" Accepted")
                newMoves.append((dy,dx))
            #else:
                #print(" Rejected")
        return newMoves   
            
    def getShape(shape):
        match shape: # 0 up, 1 right, 2 down, 3 left
            case "|": return [1,0,1,0]
            case "-": return [0,1,0,1]
            case "L": return [1,1,0,0]
            case "J": return [1,0,0,1]
            case "7": return [0,0,1,1]
            case "F": return [0,1,1,0]
            case ".": return [0,0,0,0]
            case "S": return [1,1,1,1]


# =============================================================================== #
#                                      Part 2                                     #
# =============================================================================== #
    
class P2:
    def parse(file):
        return P1.parse(file)

    def run(data):
        (grid, startPos) = data
        moves = P1.genMoves(grid, startPos, None)
        paths = []
        for m in moves:
            paths.append([startPos, m])
        while not P1.collide(paths):
            paths = P1.step(grid, paths)
        print(paths)
        return(len(paths[0])-1)
        


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