V = [1, 5, 10, 50, 100, 500]


def solve(C, A):
    ans = {v: 0 for v in V}
    for i in range(len(V))[::-1]:
        t = min(A / V[i], C[i])
        A -= t * V[i]
        ans[V[i]] = t
    return ans

coins = [1, 100, 12, 10, 4000, 1300]
mx = 500 * 300 * 20
a = solve(coins, mx).items()
print sorted(a, reverse=True)
print len(a)
