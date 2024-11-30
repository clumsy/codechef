t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    res = "YES" if a != b and b != c and c != a else "NO"
    print(res)
