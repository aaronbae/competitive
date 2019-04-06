import random
import time

def solve(N):
    s = str(N)
    length = len(s)
    left = ""
    right = ""
    for d in s:
        if d == "4":
            left += "0"
            right += "4"
        else:
            left += d
            right += "0"
    left = int(left) + int(int(right)/2)
    right = int(int(right) /2)
    if right == 0:
        right = left % 10
        left -= left % 10
    return (left, right)

def main():

    # Standard input reading scheme
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        N = int(input())
        val = solve(N)
        print("Case #{}: {}".format(i, val[0], val[1]))
    '''
    # Custom Testing
    random.seed(time.time())
    for i in range(1, 20):
        a = random.randint(0, 1000000000000)
        val = solve(a)
        print("Case #{}: {} {}".format(i, val[0], val[1]))
    '''
main()
