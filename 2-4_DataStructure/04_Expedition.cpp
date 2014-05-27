#include<stdio.h>
#include<queue>

using namespace std;

const int MAX_N = 100;

int N = 4, L = 25, P = 10;
int A[] = {10, 14, 20, 21, N};
int B[] = {10, 5, 2, 4, 0};

int solve();

int solve() {
    N++;

    priority_queue<int> que;

    int ans = 0, pos = 0, tank = P;

    for (int i = 0; i < N; i++) {
        int d = A[i] - pos;

        while (tank - d < 0) {
            if (que.empty()) { return -1; }
            tank += que.top();
            que.pop();
            ans++;
        }

        tank -= d;
        pos = A[i];
        que.push(B[i]);
    }

    return ans;
}

int main() {
    int ans = solve();
    printf("%d\n", ans);
    return 0;
}
