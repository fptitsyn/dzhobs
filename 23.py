def f(s, p):
    if p[0] == p[-1] and len(p) > 1:
        return 1
    if s > 49 or s < 40 or p[-1] in p[1:-1]:
        return 0
    return f(s + 1, p + [s + 1]) + f(s + 3, p + [s + 3]) + f(s - 1, p + [s - 1]) + f(s - 3, p + [s - 3])

print(f(42, [42]))
