class P1:
    def parse(file):
        parsed = []
        for line in file:
            parsed.append([int(i) for i in line.strip().split(" ")])
        return parsed


    def run(data):
        result = 0
        for line in data:
            lines = []
            lines.append(line)
            while ( not P1.allIsZero(lines[-1])):
                lines.append( P1.stepDown(lines[-1]) )
            
            extrapolation = 0
            lines.reverse()
            for line in lines:
                extrapolation += line[-1]
                #print(line, extrapolation)
            result += extrapolation

        return(result)
    
    def stepDown(array):
        newArr = []
        for i in range(len(array)-1):
            newArr.append(array[i+1] - array[i])
        return newArr
    
    def allIsZero(array):
        return all(x == 0 for x in array)
    


# =============================================================================== #
#                                      Part 2                                     #
# =============================================================================== #
    
class P2:
    def parse(file):
        return P1.parse(file)

    def run(data):
        result = 0
        for line in data:
            lines = []
            lines.append(line)
            while ( not P1.allIsZero(lines[-1])):
                lines.append( P1.stepDown(lines[-1]) )
            
            extrapolation = 0
            lines.reverse()
            for line in lines:
                extrapolation = line[0] - extrapolation
                # print(line, extrapolation)
            result += extrapolation

        return(result)


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