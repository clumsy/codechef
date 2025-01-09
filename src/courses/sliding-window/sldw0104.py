t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    cnt = [0] * 26
    res = b = 0
    for i, c in enumerate(s):
        k = ord(c) - ord("a")
        cnt[k] += 1
        while cnt[k] > k + 1:
            cnt[ord(s[b]) - ord("a")] -= 1
            b += 1
        res = max(res, i - b + 1)
    print(res)
