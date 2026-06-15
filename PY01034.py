T = int(input())
def f(s):
    a = [int(c) for c in s]
    n = len(a)
    for i in range(n - 2, 0, -1):
        idx = -1
        for j in range(i + 1, n):
            if a[j] < a[i]:
                if idx == -1:
                    idx = j
                else:
                    if a[j] > a[idx]:
                        idx = j
        if idx != -1:
            a[i], a[idx] = a[idx], a[i]
            return "".join([str(x) for x in a])
    idx = -1
    for i in range(1, n):
        if a[i] == 0:
            continue
        if a[i] < a[0]:
            if idx == -1:
                idx = i
            else:
                if a[idx] < a[i]:
                    idx = i
        if idx != -1:
            a[0], a[idx] = a[idx], a[0]
            return "".join([str(x) for x in a])
    return -1
for _ in range(T):
    s = input()
    print(f(s))
