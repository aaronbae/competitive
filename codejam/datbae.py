import sys
import random
import time
import math
def defaultQuery(N):
    answer = ""
    flag = True
    while len(answer) < N:
        answer += str(int(flag))
        flag = not flag
    return answer

def generate(N, split_count):
    if split_count == 1:
        answer = ""
        zeros = round(N/2)
        for i in range(zeros):
            answer += "0"
        for i in range(N-zeros):
            answer += "1"
        return answer
    return generate(round(N/2), split_count - 1) + generate(N-round(N/2), split_count - 1)

def recurseSolve(indices, N, B, F):
    queries = []
    responses = []
    boundary = math.ceil(math.log(N)/math.log(2))
    for i in range(1, min(boundary, F+1)):
        query = generate(N, i)
        queries.append(list(map(int, list(query))))
        response = ask(indices, query)
        responses.append(list(map(int, list(response))))
        print("{:^30} => {:^30}".format(query,response))

    defQ = defaultQuery(N)
    queries.append(list(map(int, list(defQ))))
    response = ask(indices, defQ)
    responses.append(list(map(int, list(response))))
    print("{:^30} => {:^30}".format(defQ,response))

    faulty = []
    i, j = 0, 0
    left = [queries[k][0] for k in range(len(queries))]
    right = [responses[k][0] for k in range(len(responses))]
    while i < N and j < N-B:
        left = [queries[l][i] for l in range(len(queries))]
        right = [responses[l][j] for l in range(len(responses))]
        # compare
        same = True
        for k in range(len(responses)):
            if left[k] != right[k]:
                faulty.append(i)
                same = False
                break

        if same:
            j += 1
        i += 1
    print(faulty)
    return faulty


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

def main():
    '''
    # Standard Testing Scheme
    T = int(input())
    for _ in range(T):
        N, B, F = map(int, input().split())
        solve(N, B, F)
    '''

    # Creating the problem
    random.seed(time.time())
    T = 5
    for i in range(T):
        N = random.randint(40, 30)
        B = random.randint(1, min(15, N-1))
        indices = set()
        while len(indices) < B:
            indices.add(random.randint(0, N-1))
        print("N: {} B: {} Broken: {}".format(N, B, indices))

        # Solving
        recurseSolve(indices, N, B, 10)

main()
