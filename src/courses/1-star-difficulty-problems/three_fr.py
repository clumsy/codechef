t = int(input())
for _ in range(t):
    x, y, z = (int(i) for i in input().split())
    # a = b + x -> a - b = x
    # b = c + y -> b - c = y -> 0 = x + y + z
    # c = a + z -> c - a = z
    res = "YES" if x in [-y + -z, y + z, -y + z, y + -z] else "NO"
    print(res)
