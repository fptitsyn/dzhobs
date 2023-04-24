def d(n):
    a = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(i)
            a.add(n // i)
    return a


f = open("17.txt")
a = [int(x) for x in f]

mxd = 0
mx = 0
for i in a:
    b = d(i)
    if mxd < len(b):
        mxd = len(b)
        mx = i

ans = []
for i in range(len(a) - 1):
    a1 = d(a[i])
    a2 = d(a[i + 1])
    ma = d(mx)
    if len(a1.intersection(ma)) >= 3 and len(a2.intersection(ma)) >= 3:
        ans.append(len(a1.intersection(a2)))

print(len(ans), max(ans))
