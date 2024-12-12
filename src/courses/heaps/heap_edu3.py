from heapq import heappush, heappop


n = int(input())
h = []
for _ in range(n):
    o = input().split()
    if len(o) == 1:
        heappop(h)
    else:
        heappush(h, -int(o[1]))
    res = -h[0]
    print(res)
