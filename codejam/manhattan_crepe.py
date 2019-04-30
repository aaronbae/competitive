import random
import time

def find_opt_index(Q, greater, less):
    # edge cases
    if not greater and not less:
        return 0
    elif not greater:
        return max(0, less[0] - 1)
    elif not less:
        return min(Q, greater[0] + 1)

    # construct values to check
    values_to_check = []
    for i in greater:
        values_to_check.append(i+1)
    for i in less:
        values_to_check.append(i-1)
    values_to_check = sorted(values_to_check)

    # find the values
    best_score = len(less)
    best_index = 0
    for i in values_to_check:
        g_temp = greater[:]
        g_temp.append(i)
        g_temp = sorted(g_temp)
        g_score = g_temp.index(i)

        l_temp = less[:]
        l_temp.append(i)
        l_temp = sorted(l_temp, reverse=True)
        l_score = l_temp.index(i)
        total = g_score + l_score
        if total > best_score:
            best_score = total
            best_index = i
    return best_index


def solve(P, Q, people):
    result = {
        "N": [],
        "S": [],
        "E": [],
        "W": [],
    }
    for p in people:
        x, y, dir = p
        if dir == "N":
            result["N"].append(y)
        elif dir == "S":
            result["S"].append(y)
        elif dir == "E":
            result["E"].append(x)
        elif dir == "W":
            result["W"].append(x)
    result["N"] = sorted(result["N"], reverse=True)
    result["S"] = sorted(result["S"], reverse=False)
    result["E"] = sorted(result["E"], reverse=True)
    result["W"] = sorted(result["W"], reverse=False)

    opt_x = find_opt_index(Q, result["E"], result["W"])
    opt_y = find_opt_index(Q, result["N"], result["S"])
    return (opt_x, opt_y)

def main():
    
    # Standard Testing Scheme
    T = int(input())
    for i in range(1, T+1):
        P, Q = map(int, input().split())
        a = []
        for _x in range(P):
            t = input().split()
            t = (int(t[0]), int(t[1]), t[2])
            a.append(t)
        val = solve(P, Q, a)
        print("Case #{}: {} {}".format(i, val[0], val[1]))


    '''
    # Creating the problem
    a = [
        (5, 5, "N")
        ];
    solve(1, 10, a);
    b = [
        (2, 4, "N"),
        (2, 6, "S"),
        (1, 5, "E"),
        (3, 5, "W")
    ];
    solve(4, 10, b);
    c = [
        (0, 2, "S"),
        (0, 3, "N"),
        (0, 3, "N"),
        (0, 4, "N"),
        (0, 5, "S"),
        (0, 5, "S"),
        (0, 8, "S"),
        (1, 5, "W")
    ];
    solve(8, 10, c);

    P = 12
    Q = 100000
    random.seed(time.time())
    d = []
    for i in range(P):
        x = random.randint(0, Q)
        y = random.randint(0, Q)
        z = random.randint(0, 3)
        if z == 0:
            z = "N"
        elif z == 1:
            z = "S"
        elif z == 2:
            z = "E"
        elif z == 3:
            z = "W"
        d.append((x,y,z))
    solve(P, Q, d);
    '''
main()
