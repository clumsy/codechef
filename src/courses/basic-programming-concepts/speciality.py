t = int(input())
for _ in range(t):
    x, y, z = (int(i) for i in input().split())
    res = "Setter" if x > max(y, z) else "Tester" if y > max(x, z) else "Editorialist"
    print(res)
