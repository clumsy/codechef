from heapq import heappush


n = int(input())
res = []
for _ in range(n):
    x = int(input())
    heappush(res, x)
    print(*res)
