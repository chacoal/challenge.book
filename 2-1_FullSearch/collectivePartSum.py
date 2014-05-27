
def solve(n, a, k):
    def dfs(i, sum):
        if n == i:
            return sum == k
        if dfs(i + 1, sum):
            return True
        if dfs(i + 1, sum + a[i]):
            return True
        sum += a[i]
        return False
    return 'YES' if dfs(0, 0) else 'NO'


print solve(4, [1, 2, 4, 7], 13)
print solve(4, [1, 2, 4, 7], 15)
