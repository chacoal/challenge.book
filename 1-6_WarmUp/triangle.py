def solve(n,a):
    ln=len(a)
    mx=0
    for i in range(ln):
        for j in range(i+1, ln):
            for k in range(j+1, ln):
                l=a[i]+a[j]+a[k]
                ma = max([a[i],a[j],a[k]])
                rest=l-ma
                if ma<rest:
                    mx=max([mx,l])
    return mx

n=5
a=[2,3,4,5,10]
print solve(n,a)
n=4
a=[4,5,10,20]
print solve(n,a)
