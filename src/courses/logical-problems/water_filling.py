t = int(input())
for _ in range(t):
    b = (int(i) for i in input().split())
    res = "Water filling time" if sum(b) < 2 else "Not now"
    print(res)
