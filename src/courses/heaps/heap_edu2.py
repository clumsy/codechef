from heapq import heappop, heapify


n = int(input())
res = [int(i) for i in input().split()]
heapify(res)
while len(res) > 0:
    heappop(res)
    print(*res)
