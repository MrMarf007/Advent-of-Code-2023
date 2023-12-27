# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

import math

class P1:
    def parse(file):
        grid = []     #2D array representing the grid (y, x)
        start = (0,0)
        for f in file:
            if "S" in f: start = (len(grid), f.index("S"))
            grid.append([*f.strip()])
        # print (grid, start)
        return (grid, start)

    def run(data):
        (grid, startPos) = data
        moves = P1.genMoves(grid, startPos, None)
        paths = []
        for m in moves:
            paths.append([startPos, m])
        while not P1.collide(paths):
            paths = P1.step(grid, paths)
        # print(paths)
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
        (sy,sx) = startPos
        moves = P1.genMoves(grid, startPos, None)
        
        # MAKE THIS WORK SO RESULT IS 351
        isPassable = False
        (my1, mx1) = moves[0]
        (my2, mx2) = moves[1]
        diff = (my1-sy, mx1-sx)
        (dy1,dx1) = (my1-sy, mx1-sx)
        (dy2,dx2) = (my2-sy, mx2-sx)
        diff = (dy1+dy2, dx1+dx2)
        print(diff)
        match diff:
            case (1,1): 
                isPassable = False
            case (-1,-1): 
                isPassable = False
            case (0,0): 
                isPassable = False
            case (-1,1): 
                isPassable = True
            case (1,-1): 
                isPassable = True
        
        path = [startPos, moves[0]]
        while path[-1] != moves[1]:
            path = P2.step(grid, path)
        loop = {}
        i = 0
        for p in path:
            loop[p] = grid[p[0]][p[1]]
        hitsL = []
        count = 0
        print("raycasting started!")
        for y in range(len(grid)):
            #print (y)
            for x in range(len(grid[0])):
                if (y,x) in loop: continue
                
                hits = 0
                dy = y
                dx = x
                
                while dy < len(grid) and dx < len(grid[0]):
                    if (dy,dx) in loop:
                        val = loop[(dy,dx)] 
                        if val != "L" and val != "7":
                            if not (isPassable and val == "S"):
                                #print("hit at: ", dy, dx, loop[(dy,dx)])
                                hits += 1
                    dy += 1
                    dx += 1
                if hits % 2 == 1: 
                    print("hit at", y, x)
                    hitsL.append((y,x))
                    count += 1
                    
        for hit in hitsL:
            loop[hit] = "X"
                    
        # for y in range(len(grid)):
        #     print ()
        #     for x in range(len(grid[0])):
        #         if (y,x) in loop: print(loop[(y,x)], end="") 
        #         else: print("O", end="")
                
        return(count)
    
    
    def step(grid, path):
        newMove = P1.genMoves(grid, path[-1], path[-2])
        return path + newMove
        


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