t = int(input())
for _ in range(t):
    res, ops = [], []
    s = input()
    for i, c in enumerate(s):
        if c == ")":
            while ops and ops[-1] != "(":
                res.append(ops.pop())
            if ops:
                ops.pop()  # (
        elif "a" <= c <= "z":
            res.append(c)
        else:
            ops.append(c)
    while ops:
        res.append(ops.pop())
    res = "".join(res)
    print(res)

# t = int(input())
# for _ in range(t):
#     vals, ops = [], []
#     s = input()
#     s = s + ")" if s[-1] != ")" else s
#     for i, c in enumerate(s):
#         if c == ")":
#             rgt = vals.pop()
#             lft = vals.pop()
#             op = ops.pop()
#             vals.append(f"{lft}{rgt}{op}")
#         elif c in "+-*^/%":
#             ops.append(c)
#         elif c != "(":
#             vals.append(c)
#     res = "".join(vals.pop())
#     print(res)
