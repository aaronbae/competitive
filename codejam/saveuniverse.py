def move_one(S):
    i = len(S) - 1
    while i >= 0:
        s = S[i]
        if s == 'C' and i < len(S) - 1 and S[i+1] == 'S':
            return S[:i]+"SC"+S[i+2:]
        i -= 1
    return "SOMETHING HAS GONE WRONG"

def score(S):
    factor = 1
    score = 0
    for c in S:
        if c == 'C':
            factor *= 2
        else:
            score += factor
    return score

def solve(D, S):
    min_score = sum([s == 'S' for s in S]);
    if min_score > D:
        return "IMPOSSIBLE"

    count = 0
    currScore = score(S)
    while currScore > D:
        S = move_one(S)
        currScore = score(S)
        count += 1
    return count

def main():

    # Standard input reading scheme
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        D, S = input().split()
        D = int(D)
        val = solve(D, S)
        print("Case #{}: {}".format(i, val))
    '''
    # Custom Testing
    val = solve(1, "CS")
    print("Case 1: {}".format(val))
    val = solve(2, "CS")
    print("Case 2: {}".format(val))
    val = solve(1, "SS")
    print("Case 3: {}".format(val))
    val = solve(6, "SCCSSC")
    print("Case 4: {}".format(val))
    val = solve(2, "CC")
    print("Case 5: {}".format(val))
    val = solve(3, "CSCSS")
    print("Case 6: {}".format(val))
    '''
main()
