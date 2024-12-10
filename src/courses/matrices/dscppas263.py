def main():
    n, m = (int(i) for i in input().split())
    if (n * m) & 1 == 1:
        print(-1)
    else:
        res = [1] * m
        for _ in range(n):
            print(*res)

if __name__ == "__main__":
    main()
