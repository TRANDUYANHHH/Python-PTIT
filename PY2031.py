T = int(input())
for _ in range(T):
    n = int(input())
    ans = 0
    i = 2
    while i * (i + 1) // 2 <= n:
        if (n * 2) % i == 0:
            tt = (n * 2) // i
            if (i + tt - 1) % 2 == 0:
                b = (i + tt - 1) // 2
                a = tt - b
                if a > 0 and b > 0:
                    ans += 1
        i += 1
    print(ans)

