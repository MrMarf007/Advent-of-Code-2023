f = open("input.txt", "r")
num = 0
for x in f:
    print(x)
    for r in (("one", "o1e"), ("two", "t2o"), ("three", "t3e"), ("four", "f4r"), ("five", "f5e"), ("six", "s6x"), ("seven", "s7n"), ("eight", "e8t"), ("nine", "n9e")):
        x = x.replace(*r)
    print(x)
    digits = ''.join(filter(str.isdigit, x))
    num += int(digits[0] + digits[-1])
print(num)