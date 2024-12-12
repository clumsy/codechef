from heapq import heapify, heappop


n = int(input())
h = [int(i) for i in input().split()]
heapify(h)
res = [heappop(h) for _ in range(n)]
print(*res)
