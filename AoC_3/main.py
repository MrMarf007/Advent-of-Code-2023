import re

def P1(f):
    res = 0
    arr = []
    lines, w, h = parseP1(f)
    symbols, nums = numsList(lines, w, h)
    #print(w,h)
    #print(lines)
    #print(symbols)
    #print(nums)
    ns = []
    for (row,col) in symbols:
         ns += validNums(row,col,w,h,lines)
         #print(ns)
    #print(ns)
    for n in ns: 
        (id, val) = nums[n]
        if (id, val) not in arr: arr.append((id, val))
    for (_,n) in arr: res += int(n)
    return(res)

def numsList(lines, w, h):
    symbols = []
    nums = {}
    id = 0
    for row in range(h):
        curNum = ''
        numPosses = []
        for col in range(w):
            n = lines[row][col]
            #print(n,row,col)
            if str.isdigit(n):
                curNum += n
                numPosses.append((row,col))
                if col == w-1 and len(numPosses) > 0:
                    for p in numPosses:
                        nums[p] = (id, curNum)
                        id+=1
            else:
                if n != ".": symbols.append((row,col))
                if len(numPosses) > 0:
                    for p in numPosses:
                        nums[p] = (id, curNum)
                    id += 1
                    curNum = ''
                    numPosses = []
                

    return symbols, nums

def parseP1(f):
    lines = [line.rstrip() for line in f]
    w = int(len(lines[0]))
    h = int(len(lines))
    return lines, w, h

def validNums(row,col,w,h,lines):
    valids = []
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            nRow = row + i
            nCol = col + j
            if (nRow < h and nRow >= 0 and nCol < w and nCol >= 0):
                if (str.isdigit(lines[nRow][nCol])):
                    #print(nRow,nCol)
                    valids.append((nRow,nCol))
    return valids
            
            



def P2(f):
    res = 0
    arr = []
    lines, w, h = parseP1(f)
    symbols, nums = numsList2(lines, w, h)
    #print(w,h)
    #print(lines)
    #print(symbols)
    #print(nums)
    for (row,col) in symbols:
        a = []
        ns = validNums(row,col,w,h,lines)
        for n in ns: 
            (id, val) = nums[n]
            if (id, val) not in a: a.append((id, val))
        if len(a) == 2: 
            b = []
            for (_,n) in a: b.append(int(n))
            arr.append(b[0]*b[1])

    res = sum(arr)
    return(res)

def numsList2(lines, w, h):
    symbols = []
    nums = {}
    id = 0
    for row in range(h):
        curNum = ''
        numPosses = []
        for col in range(w):
            n = lines[row][col]
            #print(n,row,col)
            if str.isdigit(n):
                curNum += n
                numPosses.append((row,col))
                if col == w-1 and len(numPosses) > 0:
                    for p in numPosses:
                        nums[p] = (id, curNum)
                        id+=1
            else:
                if n == "*": symbols.append((row,col))
                if len(numPosses) > 0:
                    for p in numPosses:
                        nums[p] = (id, curNum)
                    id += 1
                    curNum = ''
                    numPosses = []
    return symbols, nums



file = open("input.txt", "r")
p1 = P1(file)
print("\nPart 1 result: ")
print(p1)


file = open("input.txt", "r")
p2 = P2(file)
print("\nPart 2 result: ")
print(p2)