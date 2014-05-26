def fact(n):
    if n==0: return 1
    return n*fact(n-1)

def fact2(n,a=1):
    if n==0: return a
    return fact2(n-1, a*n)

print fact(5)
print fact2(5)
