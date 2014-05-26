def permutations(t,n):
    used=[False]*n
    perms=[0]*n
    def __perms(pos, n, perm, p=[]):
        if n==pos:
            p.append(tuple(perms))
            return
        for i in range(n):
            if not used[i]:
                perms[pos]=perm[i]
                used[i]=True
                __perms(pos+1,n,perm)
                used[i]=False
        return p
    return __perms(0, n, t)

n=9
perm=[(1<<i)-1 for i in range(n)]
for x in permutations(perm,n):
    print x
