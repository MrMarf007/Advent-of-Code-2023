def parse(part, file):
    times=distances=[]
    lines = [line.rstrip() for line in file]
    joinStr = ''
    if part == 1: joinStr = ' '
    times = [eval(i) for i in joinStr.join(lines[0].split(":")[1].split()).split(" ")]
    distances = [eval(i) for i in joinStr.join(lines[1].split(":")[1].split()).split(" ")]
    return times, distances

def P1(times, distances):
    res = 1
    for i in range(len(distances)):
       res *=  getAmountOfWinningDistances(i, times[i], distances[i])
    return(res)

def getAmountOfWinningDistances(i, roundTime, roundRecord):
    print("Round: ", i, " | Total time: ", roundTime, " | Time to beat: ", roundRecord)
    winningDistances = 0
    for holdTime in range(roundTime+1):
        speed = holdTime
        timeLeft = roundTime - holdTime
        travelDistance = timeLeft * speed
        if travelDistance > roundRecord: winningDistances += 1
    print("Amount winning distances: ", winningDistances)
    return winningDistances

 
import time
t1 = time.time()

file = open("input.txt", "r")
t,d = parse(1, file)
p1 = P1(t,d)
print("\n================================{ Part 1 result: ", p1, "}================================\n")

t2 = time.time()

file = open("input.txt", "r")
t,d = parse(2, file)
p2 = P1(t,d)

t3 = time.time()
print("\n================================{ Part 2 result: ", p2, "}================================\n")
print("P1 time: ", (t2 - t1), "\n")
print("P2 time: ", (t3 - t2), "\n")
print("Part 1 result: ", p1, "\n")
print("Part 2 result: ", p2, "\n")