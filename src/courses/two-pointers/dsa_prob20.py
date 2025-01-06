def largestCommonElement(a1, a2):
    a1.sort()
    a2.sort()
    i1, i2 = len(a1) - 1, len(a2) - 1
    while i1 >= 0 and i2 >= 0:
        if a1[i1] == a2[i2]:
            return a1[i1]
        if a1[i1] > a2[i2]:
            i1 -= 1
        else:
            i2 -= 1
    return -1

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    print(largestCommonElement(arr1, arr2))
