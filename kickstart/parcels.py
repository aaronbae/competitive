FLAG = True
def man(r1, r2, c1, c2):
    return abs(r1 - r2) + abs(c1 - c2)

def manhattan_map(R, C, mapping):
    # Step 1: count the number of offices 
    offices = []
    for i in range(R):
        for j in range(C):
            if mapping[i][j] == 1:
                offices.append((i,j))
    
    # Step 2: find the minimum manhattan
    new_map = [[R+C for _ in range(C)] for _a in range(R)]
    for oi, oj in offices:
        for i in range(R):
            for j in range(C):
                new_manhattan_val = man(oi, i, oj, j)
                new_map[i][j] = min(new_map[i][j], new_manhattan_val)
    return new_map

def solve(R, C, mapping):
    # Step 1: count the current manhattan distance of each square
    curr_man = manhattan_map(R,C, mapping)

    # Step 2: choose the biggest number and make that the new office
    new_office = (0, 0)
    max_man_val = 0
    for i in range(R):
        for j in range(C):
            new_man_val = curr_man[i][j]
            if new_man_val > max_man_val:
                max_man_val = new_man_val
                new_office = (i,j)
    mapping[new_office[0]][new_office[1]] = 1

    # Step 3: count the new manhattan distance of each square
    new_man = manhattan_map(R,C, mapping)
    if FLAG:
        print("NEW MAP")
        for i in range(R):
            print(new_man[i])
        print("")
    return max([max(new_man[i]) for i in range(R)])

def main():
    '''
    # Standard input reading scheme
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        R, C = map(int, input().split())
        mapping = []
        for _ in range(R):
            row = list(map(int, list(input())))
            mapping.append(row)
        val = solve(R, C, mapping)
        print("Case #{}: {}".format(i, val))
    '''
    # Custom Tests
    a = [[1, 0, 1],
        [0, 0, 0],
        [1, 0, 1]]
    val = solve(3, 3, a)
    print("Case #1: {}".format(val))  

    b = [[1, 1]]
    val = solve(1, 2, b)
    print("Case #2: {}".format(val)) 

    c = [[1, 0, 0, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 0, 0, 0, 1]]
    val = solve(5, 5, c)
    print("Case #3: {}".format(val))   
main()
