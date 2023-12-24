f = open("input.txt", "r")

#maxR,maxG,maxB=12,13,14
num = 0
for x in f:
    x = x.split(":")
    #id = int(x[0][5:])
    print(x)
    r=g=b=0
    success=True
    rounds = x[1].split(";")
    for throws in rounds:
        #r,g,b=0,0,0
        throws = throws.split(",")
        #print(throws)
        for part in throws:
            part = part.split(" ")
            #print(part)
            new = int(part[1].strip())
            match part[2].strip():
                case "red":
                    if new > r: r = new
                    #r+=int(part[1])
                case "green":
                    if new > g: g = new
                    #g+=int(part[1])
                case "blue":
                    if new > b: b = new
                    #b+=int(part[1])
        #if r > maxR or g > maxG or b > maxB:
        #    success=False
        print(r, g, b, success)
    num += r * g * b
    #if success:
    #    num += id

print(num)