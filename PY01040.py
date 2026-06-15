T = int(input())
def rot(s):
    tot = 0
    for c in s:
        tot = (tot + ord(c) - ord('A')) % 26
    ans = ""
    for c in s:
        x = ord(c) - ord('A')
        x = (x + tot) % 26
        ans += chr(ord('A') + x)
    return ans
def mer(x, y):
    xx = ord(x) - ord('A')
    yy = ord(y) - ord('A')
    xx = (xx + yy) % 26
    return chr(xx + ord('A'))
for _ in range(T):
    s = input()
    a = s[:len(s) // 2]
    b = s[len(s) // 2:]
    a = rot(a)
    b = rot(b)
    ans = ""
    for i in range(len(a)):
        ans += mer(a[i], b[i])
    print(ans)
