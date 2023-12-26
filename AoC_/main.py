class P1:
    def parse(file):
        res = ''

        return res

    def run(data):
        res = ''

        return(res)

# =============================================================================== #
#                                      Part 2                                     #
# =============================================================================== #
    
class P2:
    def parse(file):
        res = ''

        return res

    def run(data):
        res = ''
        
        return(res)


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