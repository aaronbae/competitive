import random
import time
import math

def specialDown(power):
    total = 2
    for i in range(1,power):
        total += 10**i
    return total

def analyze(N):
    s = str(N)
    for index, d in enumerate(s):
        digit = int(d)
        power = len(s)-index-1
        if digit % 2 == 1:
            if power == 0:
                return 1
            remainder = int(s[index+1:])
            if digit == 9:
                return remainder + specialDown(power)
            down = remainder + specialDown(power)
            up = 10**power-int(s[index+1:])
            return min(up, down)
    return 0

def isEven(N):
    a = str(N)
    return len(a) == sum([int(s) % 2 == 0 for s in a])

max_pow = 3
length = 1000
random.seed(time.time())
values = [random.randint(math.pow(10, max_pow-1), math.pow(10, max_pow)) for i in range(length)]
results = [analyze(i) for i in values]
for i in range(length):
    if isEven(values[i]+ results[i]):
        donothing = 0
        print("{:2d} :\t{} + {:3d} = {:4d}".format(i, values[i], results[i], values[i]+results[i] ))
    elif isEven(values[i] - results[i]):
        donothing = 0
        print("{:2d} :\t{} - {:3d} = {:4d}".format(i, values[i], results[i],values[i]-results[i] ))
    else:
        print("{:2d} :\tERROR".format(i))

#t = int(input())  # read a line with a single integer
#for i in range(1, t + 1):
#    N = int(input())
#    print(analyze(N))
