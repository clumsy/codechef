def sortArrayByParity(nums):
    o, n, e = 0, len(nums), sum(e & 1 for e in nums)
    res = [-1] * n
    for v in nums:
        if v & 1 == 1:
            res[o] = v
            o += 1
        else:
            res[e] = v
            e += 1
    for i in range(n):
        nums[i] = res[i]
    

if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().split()))

    sortArrayByParity(nums)

    print(" ".join(map(str, nums)))
