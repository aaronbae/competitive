import random
import time

def solve(S):
    newS = ""
    for i in S:
        s = "S"
        if i == "S":
            s = "E"
        newS += s
    return newS

def main():

    # Standard input reading scheme
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        N = int(input())
        S = input()
        val = solve(S)
        print("Case #{}: {}".format(i, val))

main()
