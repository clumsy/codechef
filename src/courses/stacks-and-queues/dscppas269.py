n = int(input())
h = [int(i) for i in input().split()]
res = [0] * n
st = []
for i in reversed(range(len(h))):
    while st and st[-1] <= h[i]:
        st.pop()
    res[i] = st[-1] if st else -1
    st.append(h[i])
print(*res)
