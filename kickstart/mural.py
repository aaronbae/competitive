import math

def solve(mural):
    painted_window = math.ceil(len(mural) / 2)
    max_beauty = sum(mural[:painted_window])
    curr_beauty = max_beauty
    for i in range(0, len(mural)-painted_window):
        curr_beauty -= mural[i]
        curr_beauty += mural[i+painted_window]
        if curr_beauty > max_beauty:
            max_beauty = curr_beauty
    return max_beauty


# Standard input reading scheme
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    N = int(input())
    mural = list(map(int, list(input())))
    val = solve(mural)
    print("Case #{}: {}".format(i, val))