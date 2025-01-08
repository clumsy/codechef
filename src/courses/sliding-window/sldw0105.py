def findMinSumSubarray(n, k, arr):
    res = cur = sum(arr[:k])
    for i in range(k, len(arr)):
        cur = cur - arr[i - k] + arr[i]
        res = min(res, cur)
    return res

if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(findMinSumSubarray(n, k, arr))
