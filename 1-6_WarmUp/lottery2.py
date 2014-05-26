def binary_search(x,k):
    l=0
    r=len(k)
    while r-l>=1:
        i=(l+r)/2
        if k[i]==x: return True
        elif k[i]<x: l=i+1
        else: r = i

    return False

def solve(n,m,k):
    k.sort()
    kk=[c+d for c in k for d in k]
    kk.sort()
    for a in k:
        for b in k:
            if binary_search(m-a-b,kk): return 'YES'
    return 'NO'

print solve(3, 10, [1,3,5])
print solve(3,  9, [1,3,5])
