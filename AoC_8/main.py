def parse(file):
    steps = [*file.readline().strip()]
    file.readline()
    nodes = {}
    for f in file:
        n = f[:3]
        l = f[7:10]
        r = f[12:15]
        nodes[n]=(l,r)
    return (steps, nodes)

def getSteps(f,startNode):
    (steps, nodes) = f
    stepCounter = 0
    currentNode = startNode
    while(currentNode[2] != "Z"):
        (nextNodeL, nextNodeR) = nodes[currentNode]
        if (steps[stepCounter%len(steps)] == "L"):
            currentNode = nextNodeL
        if (steps[stepCounter%len(steps)] == "R"):
            currentNode = nextNodeR
        stepCounter += 1
    return(stepCounter)

# =============================================================================== #
#                                      Part 2                                     #
# =============================================================================== #

from functools import reduce

def parse2(file):
    steps = [*file.readline().strip()]
    file.readline()
    nodes = {}
    for f in file:
        n = f[:3]
        l = f[7:10]
        r = f[12:15]
        nodes[n]=(l,r)
    return (steps, nodes)

def P2(f):
    (steps, nodes) = f
    lengths = []
    for n in nodes:
        if (n[2] == "A"): 
            lengths.append(getSteps((steps, nodes), n))
    print(lengths)
    return lcm(lengths)

def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)

def lcm(A):
    lcm = 1
    for i in A:
        lcm = lcm * i // gcd(lcm, i)
    return lcm




import time
t1 = time.time()

file = open("input.txt", "r")
hands = parse(file)
p1 = getSteps(hands, "AAA")
print("\n================================{ Part 1 result: ", p1, "}================================\n")

t2 = time.time()

file = open("input.txt", "r")
hands = parse2(file)
p2 = P2(hands)

t3 = time.time()
print("\n================================{ Part 2 result: ", p2, "}================================\n")
print("P1 time: ", (t2 - t1), "\n")
print("P2 time: ", (t3 - t2), "\n")
print("Part 1 result: ", p1, "\n")
print("Part 2 result: ", p2, "\n")