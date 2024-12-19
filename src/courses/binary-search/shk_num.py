t = int(input())
for _ in range(t):
    n = int(input())
    if n <= 2:
        res = 3 - n
    elif n == -n & n:  # power of 2 => 1000...01
        res = 1
    else:
        s = bin(n)[2:]
        res = (int("1" + "0" * len(s), 2) + 1) - n
        if s[1] == "0":
            x = s[2:].lstrip("0")
            res = min(res, int("1" + "0" * len(x), 2) - (int(x, 2)))
        rem = 2
        for i, c in enumerate(s):
            if c == "1":
                rem -= 1
                if rem == 0:
                    res = min(res, n - int(s[:i + 1] + "0" * (len(s) - 1 - i), 2))
                    break
    print(res)
