#include<stdio.h>

#define FOR(S,N) for (S = 0; S < N; S++)

const int MAX_N = 50;

int main() {
    int n, m, k[MAX_N];

    int i,a,b,c,d, f;

    scanf("%d %d", &n, &m);
    FOR(i,n) scanf("%d", &k[i]);

    FOR(a,n) FOR(b,n) FOR(c,n) FOR(d,n) {
        if (k[a] + k[b] + k[c] + k[d] == m) f = 1;
    }

    if (f) printf("Yes\n");
    else   printf("No\n");

    return 0;
}
