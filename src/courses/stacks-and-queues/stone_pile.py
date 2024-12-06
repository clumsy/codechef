from collections import deque

t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    dq, pl = deque(a), 0
    while len(dq) > 1:
        dq.append(dq.popleft())
        if pl == 1:
            dq.append(dq.popleft())
        dq.popleft()
        pl = 1 - pl
    res = (pl, dq.pop())
    print(*res)
