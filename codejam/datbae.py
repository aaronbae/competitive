import sys
import random
import time

def ask(indices, query):
    result = ""
    for i in range(len(query)):
        if i not in indices:
            result += query[i]
    return result

def solve(N, B, F):
    m = ""
    for i in range(N):
        m += "1"
        
    for i in range(F):
        print(m)
        sys.stdout.flush()
        s = input()
    return 0

    '''
    possibility = [True] * N
    m = (a + b) // 2
    print(m)
    sys.stdout.flush()
    s = input()
    if s == "CORRECT":
        return
    '''

def main():

    # Standard Testing Scheme
    T = int(input())
    for _ in range(T):
        N, B, F = map(int, input().split())
        solve(N, B, F)

    '''
    # Custom Testing scheme
    random.seed(time.time())
    N = 20
    #N = 1024
    B = random.randint(1, N-1)
    indices = set()
    # break
    while len(indices) < B:
        indices.add(random.randint(0, N-1))

    print("N: {} B: {} Broken: {}".format(N, B, indices))
    # interact
    count = 1
    while(True):
        result = ask(indices, input("{} : ".format(count)))
        print("{} : {}".format(count, result))
        count += 1
    #solve(N, B, F)
    '''
main()
