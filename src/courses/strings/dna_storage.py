dna = {
    "00": "A",
    "01": "T",
    "10": "C",
    "11": "G",
}
t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    res = "".join(dna[s[2*i:2*i + 2]] for i in range(n // 2))
    print(res)
