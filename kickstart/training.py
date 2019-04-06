def solve(N, P, skills):
    #print("P: {}".format(P))
    # Step 1: turn it into frequency table
    freq = {}
    for i in skills:
        if i not in freq:
            freq[i] = 0
        freq[i] += 1
        if freq[i] > P:
            return 0

    keys = list(freq.keys())
    keys.sort()
    hours_needed = []
    # Step 2: calculate the hours needed for each skill
    for i in keys:
        still = P-freq[i]
        total_hours = 0

        # Step 3: Check if it is even feasible with the current skill i
        test = sum([freq[k] for k in keys[:keys.index(i)]])
        if test < still: 
            continue
        
        # Step 4: If it is feasible, calculate the hours needed
        for j in range(1, i):
            if i-j in freq:
                if still - freq[i - j] < 0:
                    total_hours += j * still
                    break
                else:
                    still -= freq[i-j]
                    total_hours += j * freq[i-j]
        hours_needed.append(total_hours)
        # print("Skill: {}\t hours: {}".format(i,total_hours))
    return min(list(hours_needed))

def main():
    
    # Standard input reading scheme
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        N, P = map(int, input().split())
        skills = map(int, input().split())
        val = solve(N, P, skills)
        print("Case #{}: {}".format(i, val))
    '''
    # Custom Tests
    ps = [3, 2, 5]
    skills = [[3, 1, 9, 100],
                [5, 5, 1, 2, 3, 4],
                [7, 7, 1, 7, 7]]
    for i in range(3):
        p = ps[i]
        s = skills[i]
        n = len(s)
        val = solve(n, p, s)
        print("Case #{}: {}".format(i, val))   
    '''
main()
