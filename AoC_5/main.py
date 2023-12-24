class map:
    def __init__(self, n, r):
        self.name = n
        self.ranges = r

    def getMapping(self, x):
        for (target, match, range_) in self.ranges:
            if (x >= match and x < match+range_):
                return (target + (x - match))
        return x
    
    def mapArray(self, arr):
        res = []
        for val in arr:
            num = self.getMapping(val)
            #print (self.name, "mapped: ", val, " -> ", num)
            res.append(num)
        return res
    
    def getLowestMappingFromRange(self, x):
        #print(x)
        (lo, size) = x
        for (target, match, range_) in self.ranges:
            if (lo >= match and lo < match+range_):
                res = [((lo + target - match), size)]
                if not((lo+size-1) >= match and (lo+size-1) < match+range_):
                    #print("panicc")
                    restSize = ((lo+size-1)-(match+range_))
                    rest = ((match+range_), restSize)
                    res = [((lo + target - match), (size - restSize))]
                    #print(val)
                    temp = self.getLowestMappingFromRange(rest)
                    res = res + temp
                return res
        return [x]
    
    def mapArrayOfRanges(self, arr):
        res = []
        for val in arr:
            num = self.getLowestMappingFromRange(val)
            #print (self.name, "mapped: ", val, " -> ", num)
            for n in num:
                res.append(n)
        return res

def P1(f):
    res = ''
    seeds = [eval(i) for i in file.readline().split(":")[1].strip().split(" ")]
    maps = [] 
    for m in f.read().strip().split("\n\n"):
        ranges = []
        splittedParts = m.split(":")
        name = splittedParts[0].strip().split(" ")[0]
        splittedIntoRanges = splittedParts[1].strip().split("\n")
        for a in splittedIntoRanges:
            nums = [eval(i) for i in a.split(" ")]
            ranges.append((nums[0],nums[1],nums[2]))
        maps.append( map(name, ranges) )
    mapSteps = seeds
    for map_ in maps:
        mapSteps = map_.mapArray(mapSteps)

    return(min(mapSteps))


def P2(f):
    res = ''
    seedLine = [eval(i) for i in file.readline().split(":")[1].strip().split(" ")]
    seeds = []
    for s in range(0, len(seedLine), 2):
        val1 = seedLine[s]
        val2 = seedLine[s+1]
        seeds.append((val1,val2))

    maps = []
    for m in f.read().strip().split("\n\n"):
        ranges = []
        splittedParts = m.split(":")
        name = splittedParts[0].strip().split(" ")[0]
        splittedIntoRanges = splittedParts[1].strip().split("\n")
        for a in splittedIntoRanges:
            nums = [eval(i) for i in a.split(" ")]
            ranges.append((nums[0],nums[1],nums[2]))
        maps.append( map(name, ranges) )
    mapSteps = seeds
    for map_ in maps:
        mapSteps = map_.mapArrayOfRanges(mapSteps)
    (lowest, _) = min(mapSteps)
    return(lowest)

import time
t1 = time.time()

file = open("input.txt", "r")
p1 = P1(file)
print("\n================-----------{ Part 1 result: ", p1, "}-----------================\n")

t2 = time.time()

file = open("input.txt", "r")
p2 = P2(file)

t3 = time.time()
print("P1 time: ", (t2 - t1), "\n")
print("P2 time: ", (t3 - t2), "\n")
print("Part 1 result: ", p1, "\n")
print("Part 2 result: ", p2, "\n")