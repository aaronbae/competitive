def troubleSort(array):
    odd = sorted(array[::2])
    even = sorted(array[1::2])
    total = []
    for i in range(len(odd)):
        total.append(odd[i])
        if i < len(even):
            total.append(even[i])
    return total

def solve(array):
    odd = sorted(array[::2])
    even = sorted(array[1::2])
    if odd[0] > even[0]:
        return 0
    for i in range(1, len(odd)):
        if i < len(even) and odd[i] > even[i]:
            return i*2
        elif odd[i] < even[i-1]:
            return i*2 - 1
    return "OK"

def main():

    # Standard input reading scheme
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        A = int(input())
        L = list(map(int, input().split()))
        val = solve(L)
        print("Case #{}: {}".format(i, val))
    '''
    # Custom Testing
    random.seed(time.time())
    for i in range(1, 10):
        a = [random.randint(0, 20) for j in range(3)]
        val = solve(a)
        print("Case #{}: {}".format(i, val))
    '''
main()
