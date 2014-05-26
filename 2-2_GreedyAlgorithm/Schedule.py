def solve(n, s, t):
    et=min(t)
    ans=1
    for i in range(n):
        if s[i]>et:
            ans+=1
            et=t[i]

    return ans

n=5
s=[1,2,4,6,8]
t=[3,5,7,9,10]
print solve(n, s, t)
