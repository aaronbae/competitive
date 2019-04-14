def find(w, x):
    accent = -1
    while(w[accent:] == x[accent:]):
        accent -= 1
    return accent + 1

def solve(N, words):
    # Create priority dictionary
    priority = {}
    pairable_words = {}
    for i in range(len(words)):
        a = words[i]
        minV = 0
        other_words = []
        for j in range(len(words)):
            if i != j:
                b = words[j]
                v = find(a,b)
                if v < minV:
                    minV = v
                    other_words = [b]
                elif v == minV:
                    other_words.append(b)
        if minV not in priority:
            priority[minV] = []
        priority[minV].append(a)
        pairable_words[a] = other_words

    # count
    count = 0
    keys_used = set()
    for k in priority.keys():
        if k != 0:
            words_used = set()
            # traverse through all the words in the group
            for w in priority[k]:
                if w not in words_used:
                    words_used.add(w)
                    other = pairable_words[w][0]
                    # find pariable word 'other'
                    for x in pairable_words[w]:
                        other = x
                        if x not in words_used and other[k:] not in keys_used:
                            break
                    if other[k:] not in keys_used:
                        count += 2
                        words_used.add(other)
                        keys_used.add(other[k:])
    return count

def main():
    
    # Standard input reading scheme
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        N = int(input())
        words = []
        for i in range(N):
            words.append(input())
        val = solve(N, words)
        print("Case #{}: {}".format(i, val))
    '''
    # Custom Testing
    a = ["TARPOL", 'PROL']
    val = solve(2, a)
    print("Case 1: {}".format(val))
    b = ["TARPOR", "PROL", "TARPRO"]
    val = solve(3, b)
    print("Case 2: {}".format(val))
    c = ["CODEJAM", "JAM", "HAM", "NALAM", "HUM", "NOLOM"]
    val = solve(6, c)
    print("Case 3: {}".format(val))
    d = ["PI", "HI", "WI", "FI"]
    val = solve(4, d)
    print("Case 4: {}".format(val))
    '''
main()
