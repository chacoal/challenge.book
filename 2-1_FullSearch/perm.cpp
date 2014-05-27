#include<cstdio>
#include<algorithm>

using namespace std;

const int MAX_N = 50;

int perm2[MAX_N];

void permutation2(int);

void permutation2(int n) {
    for (int i = 0; i < n; i++) {
        perm2[i] = i;
    }
    do {
        for (int i = 0; i < n; i++) {
            printf("%d ", perm2[i]);
        }
        printf("\n");

    } while (next_permutation(perm2, perm2 + n));
    return;
}

int main() {
    permutation2(5);
    return 0;
}
