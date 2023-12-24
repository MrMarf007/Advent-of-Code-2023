def P1(f):
    res = 0
    for line in f:
        count = 0
        numbers = " ".join(line[7:].split()).split('|')
        winningNums = numbers[0].strip().split(" ")
        scratchNums = numbers[1].strip().split(" ")
        for n in scratchNums:
            if n in winningNums:
                if count > 0: count *= 2
                else: count += 1
        res += count
    return(res)

def P2(f):
    results = []
    amounts = []
    res = 0
    for line in f:
        count = 0
        splitted = " ".join(line.split()).split(':')
        # id = int(splitted[0].split(" ")[1])
        numbers = splitted[1].split('|')
        winningNums = numbers[0].strip().split(" ")
        scratchNums = numbers[1].strip().split(" ")
        count = 0
        for n in scratchNums:
            if n in winningNums:
                count += 1
        results.append(count)
        amounts.append(1)
    
    for i in range(len(results)):
        res += amounts[i]
        for j in range(results[i]):
            amounts[i+j+1] += amounts[i]

    return(res)

file = open("input.txt", "r")
p1 = P1(file)
print("Part 1 result: ", p1)

file = open("input.txt", "r")
p2 = P2(file)
print("Part 2 result: ", p2)