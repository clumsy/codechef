def count_pairs_less_than_x(a, x):
    n = len(a)
    hi, res = n - 1, 0
    for lo in range(n):
        while lo < hi and a[lo] + a[hi] >= x:
            hi -= 1
        if lo == hi:
            break
        res += hi - lo
    return res

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    x = int(input())
    print(count_pairs_less_than_x(arr, x))
