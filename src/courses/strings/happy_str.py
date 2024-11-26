vowels = "aeiou"
t = int(input())
for _ in range(t):
    s = input()
    res = "Sad"
    i1 = i2 = False
    for i in range(len(s)):
        i0 = s[i] in vowels
        if i0 and i1 and i2:
            res = "Happy"
            break
        i2, i1 = i1, i0
    print(res)
