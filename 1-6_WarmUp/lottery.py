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
    for a in k:
        for b in k:
            for c in k:
                if binary_search(m-a-b-c,k): return 'YES'
                # if m-a-b-c in k: return 'YES'
    return 'NO'

print solve(3, 10, [1,3,5])
print solve(3,  9, [1,3,5])
