t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    m = {"A": "T", "T": "A", "C": "G", "G": "C"}
    res = "".join(m[c] for c in s)
    print(res)
