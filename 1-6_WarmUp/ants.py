def solve(L, n, x):
    half = L / 2
    mx, mn = 0, 0
    for xi in x:
        if xi > half:
            mx = max([mx, xi])
            mn = max([mn, L - xi])
        else:
            mx = max([mx, L - xi])
            mn = max([mn, xi])

    return (mn, mx)

(mn, mx) = solve(10, 3, [2, 6, 7])
print 'min =', mn
print 'max =', mx
