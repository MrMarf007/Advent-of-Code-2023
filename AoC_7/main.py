def parse(p, file):
    hands = []
    for f in file:
        line = f.split(" ")
        hands.append(Hand(p, line[0], line[1]))
    return hands

# 1 4 3 2 5
def P1(hands):
    # print(hands[0].cards, hands[1].cards)
    # print(Hand.getCardWorth(hands[0].cards[0]), Hand.getCardWorth(hands[1].cards[0]))
    # print(hands[0].type, hands[1].type)
    # print(Hand.lowerThanOrEquals(hands[0],hands[1]))
    res = 0
    sortedHands = quickSortHands(hands)
    for i in range(len(sortedHands)):
       #print(sortedHands[i].type, sortedHands[i].cards)
       res += sortedHands[i].bid * (i+1)
    return res

# 
def P2(hands):
    Hand.cardOrder = ["J","2","3","4","5","6","7","8","9","T","Q","K","A"]
    return P1(hands)


class Hand:

    cardOrder = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
    cardOrder2 = ["J","2","3","4","5","6","7","8","9","T","Q","K","A"]

    def __init__(self, i, cs, b):
        self.part = i
        self.cards = [*cs]
        self.bid = int(b)
        self.type = self.getType()
    
    def getType(self):
        amounts = [0 for i in range(len(Hand.cardOrder))]
        if self.part == 1:
            for card in self.cards:
                amounts[Hand.getCardWorth(card)]+=1
            Js = 0
            group = [i for i in amounts if i != 0]
        if self.part == 2:
            for card in self.cards:
                amounts[Hand.getCardWorth2(card)]+=1
            Js = amounts[0]
            group = [i for i in amounts[1:] if i != 0]
        group.sort()
        if(group == [] and Js == 5): group = [5]
        else:
            group[len(group)-1] += Js
        #print(group)
        match group:
            case [5]:       #five of a kind
                return 6
            case [1,4]:       #five of a kind
                return 5
            case [2,3]:     #full house
                return 4
            case [1,1,3]:
                return 3
            case [1,2,2]:
                return 2
            case [1,1,1,2]:
                return 1
            case [1,1,1,1,1]:
                return 0
    
    def getCardWorth(card):
        return Hand.cardOrder.index(card)
    
    def getCardWorth2(card):
        return Hand.cardOrder2.index(card)
    
    def lowerThanOrEquals(x, y):
        if (x.type == y.type):
            for i in range(len(x.cards)):
                xW = int(Hand.getCardWorth(x.cards[i]))
                yW = int(Hand.getCardWorth(y.cards[i]))
                if(xW == yW): continue
                #print( "yee: ", x.cards[i], y.cards[i])
                return xW < yW
        return x.type <= y.type


def quickSortHands(hands):
    if (hands != [] and len(hands) > 1):
        pivot = hands[len(hands)-1]
        r = []
        l = []
        for j in range(len(hands)-1):
            if hands[j].lowerThanOrEquals(pivot):
                l.append(hands[j])
            else:
                r.append(hands[j])
        return quickSortHands(l) + [pivot] + quickSortHands(r)
    return hands


import time
t1 = time.time()

file = open("input.txt", "r")
hands = parse(1, file)
p1 = P1(hands)
print("\n================================{ Part 1 result: ", p1, "}================================\n")

t2 = time.time()

file = open("input.txt", "r")
hands = parse(2, file)
p2 = P2(hands)

t3 = time.time()
print("\n================================{ Part 2 result: ", p2, "}================================\n")
print("P1 time: ", (t2 - t1), "\n")
print("P2 time: ", (t3 - t2), "\n")
print("Part 1 result: ", p1, "\n")
print("Part 2 result: ", p2, "\n")