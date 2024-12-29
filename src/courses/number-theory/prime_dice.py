primes = set()
for i in range(2, 13):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        primes.add(i)
t = int(input())
for _ in range(t):
    a, b = (int(i) for i in input().split())
    res = "Alice" if a + b in primes else "Bob"
    print(res)
