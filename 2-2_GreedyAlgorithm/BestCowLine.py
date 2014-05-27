def solve(N, S):
    T = ""
    while 1:
        print S, T
        if len(S) == 0:
            break
        f = 0
        l = len(S) - 1
        _S = S[::-1]
        for j in range(len(S)):
            print j
            if S[j] > _S[j]:
                T += S[l]
                S = S[:l]
                break
            elif S[j] < _S[j]:
                T += S[f]
                S = S[f + 1:]
                break
        else:
            T += S[f]
            S = S[f + 1:]
    return T


N = 6
S = "ACDBCB"
print solve(N, S)
