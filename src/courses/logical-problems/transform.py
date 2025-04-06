t = int(input())
for _ in range(t):
    x = int(input()) 
    x = x % 3
    res = ["NORMAL", "HUGE", "SMALL"][x]
    print(res)
