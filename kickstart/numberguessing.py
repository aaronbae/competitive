import sys

def solve(a, b, n):
    m = (a + b) // 2
    print(m)
    sys.stdout.flush()
    s = input()
    if s == "CORRECT":
        return
    elif s == "TOO_SMALL":
        a = m + 1
        n -= 1
    else:
        b = m - 1
        n -= 1
    if n > 0:
        solve(a, b, n)

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    n = int(input())
    solve(a + 1, b, n)