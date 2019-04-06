class Interval:
    def __init__(self, l, r):
        self.left = l
        self.right = r

    def length(self):
        return r-l

class Organizer:
    def __init__(self, num, book):
        self.data = {}
        self.N = num
        self.Q = book
    
    def add(self, interval):
        if interval.length() not in self.data:
            self.data[interval.length()] = []
        self.data[interval.length()].append(interval)
    
    def calculate(self):
        curr_min = self.N
        seats = set()
        keys = list(self.data.keys())
        keys.sort()
        for length in keys:
            intervals = self.data[length]
            for i in intervals:
                
            

def solve(N, Q, LR):
    # Step 1: group by subset
    # Step 2: merge the subsets two at a time
    return 0

def main():
    '''
    # Standard input reading scheme
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        N, Q = map(int, input().split())
        LR = []
        for _ in range(1, Q+1):
            N, Q = map(int, input().split())
            LR.append([N,Q])
        val = solve(N, Q, LR)
        print("Case #{}: {}".format(i, val))
    '''
    # Custom Testing
    a = [[1, 2],
        [3, 4],
        [2, 5]]
    val = solve(5, 3, a)
    print("Case 1: {}".format(val))

    b = [[10, 11],
        [10, 10],
        [11, 11]]
    val = solve(30, 3, b)
    print("Case 2: {}".format(val))

    c = [[1, 8],
        [4, 5],
        [3, 6],
        [2, 7]]
    val = solve(10, 4, c)
    print("Case 3: {}".format(val))

main()
