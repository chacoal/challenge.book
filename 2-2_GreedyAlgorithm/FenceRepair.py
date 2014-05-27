import sys
from datetime import (
    datetime,
)

def permutations(t,n):
    used=[False]*n
    perms=[0]*n
    def __perms(pos, n, perm, p=[]):
        if n==pos:
            tmp=tuple(perms)
            if tmp not in p:
                p.append(tmp)
            return
        for i in range(n):
            if not used[i]:
                perms[pos]=perm[i]
                used[i]=True
                __perms(pos+1,n,perm)
                used[i]=False
        return p
    return __perms(0, n, t)

def solve(N,L):
    p=permutations(L, N)
    ans=[]
    for pi in p:
        tmp=0
        while len(pi)>1:
            ln=sum(pi)
            tmp+=ln
            pi=pi[1:]

        ans.append(tmp)

    print ans
    return min(ans)


N=3
L=[8,5,8]
print solve(N,L)
