def parse(file):
    res = ''

    return res

def P1(f):
    res = ''

    return(res)

# =============================================================================== #
#                                      Part 2                                     #
# =============================================================================== #

def parse2(file):
    res = ''

    return res

def P2(f):
    res = ''
    
    return(res)


import time
t1 = time.time()

file = open("input.txt", "r")
hands = parse(file)
p1 = P1(hands)
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