def solve(n, W, wv, memo):
    def rec(i, j):
        if memo[i][j] >= 0:
            return memo[i][j]

        res = 0
        if i == n:
            res = 0
        elif j < wv[i][0]:
            res = rec(i + 1, j)
        else:
            res = max([rec(i + 1, j), rec(i + 1, j - wv[i][0]) + wv[i][1]])
        memo[i][j] = res
        print memo
        return res
    return rec(0, W)

n = 4
w = 5
wv = [(2, 3), (1, 2), (3, 4), (2, 2)]
memo = [[-1] * (w + 1)] * (n + 1)
print solve(n, w, wv, memo)
