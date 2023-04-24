f = [0] * 12400
for n in range(12_345, 0, -1):
    if n > 10000:
        f[n] = n - 10000
    else:
        f[n] = f[n + 1] + f[n + 2]

print(f[12345] * (f[10] - f[12]) / f[11] + f[10101])
