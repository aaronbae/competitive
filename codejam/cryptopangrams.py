import random
import time

def readPrimes():
    result = []
    with open('primes.txt') as f:
        for l in f:
            result.append(int(l))
    f.close()
    return result

def solve(N, L, values):
    # find the offset for the initial-repeat problem
    offset = 0
    prev = values[0]
    for i in range(1,L):
        if values[i] != values[i-1]:
            offset = i - 1
            break

    # find a factor of the first
    first = -1
    for i in range(2, N+1):
        if values[offset] % i == 0:
            if values[offset+1] % i == 0:
                first = int(values[offset] / i)
            else:
                first = i
            break
    if offset % 2 == 1:
        first = int(values[offset]/first)

    # Decode the others
    decode_values = [first]
    prev = decode_values[0]
    for v in values:
        newDV = int(v/prev)
        decode_values.append(newDV)
        prev = newDV
    converter = sorted(list(set(decode_values)))

    # Convert it to alpha numeric characters
    answer = ""
    for v in decode_values:
        answer += chr(converter.index(v) + 65)
    return answer

def main():
    
    # Standard input reading scheme
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        N, L = map(int, input().split())
        values = list(map(int, input().split()))
        val = solve(N, L, values)
        print("Case #{}: {}".format(i, val))

    '''
    # Default Test Cases
    a = [217, 1891, 4819, 2291, 2987, 3811, 1739, 2491, 4717, 445, 65, 1079, 8383, 5353, 901, 187, 649, 1003, 697, 3239, 7663, 291, 123, 779, 1007, 3551, 1943, 2117, 1679, 989, 3053]
    val = solve(103, 31, a)
    print("Case #1: {}".format(val))
    b = [3292937, 175597, 18779, 50429, 375469, 1651121, 2102, 3722, 2376497, 611683, 489059, 2328901, 3150061, 829981, 421301, 76409, 38477, 291931, 730241, 959821, 1664197, 3057407, 4267589, 4729181, 5335543]
    val = solve(10000, 25, b)
    print("Case #2: {}".format(val))
    '''
    '''
    # Custom Test Cases
    N = 100000
    primes = readPrimes()
    random.seed(time.time())
    all_alphabet = set([chr(i+65) for i in range(26)])
    for i in range(1,1000):
        # Create a new string
        s = ""
        for j in range(75):
            s += chr(random.randint(0,25)+65)
        diff = list(all_alphabet - set(s))
        for d in diff:
            s += d

        # Select primes
        primes_used = set()
        while len(primes_used) < 26:
            primes_used.add(primes[random.randint(0,25)])
        primes_used = list(primes_used)

        # Create input array
        input = []
        prev = primes_used[ord(s[0])-65]
        for j in range(1,len(s)):
            newPrime = primes_used[ord(s[j])-65]
            input.append(prev*newPrime)
            prev =newPrime

        # solve
        print("Case #{}: {}".format(i, s))
        val = solve(100000, len(input), input)
        print("       : {}".format(val))
        '''

main()
