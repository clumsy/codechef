prime = [True] * 100001
prime[0] = prime[1] = False
for i in range(3, 100001, 2):
    if prime[i]:
        for j in range(2 * i, 100001, i):
            prime[j] = False

t = int(input())
for _ in range(t):
    n = int(input())
    res = "yes" if prime[n] else "no"
    print(res)
