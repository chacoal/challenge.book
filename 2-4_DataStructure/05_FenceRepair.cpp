#include<stdio.h>
#include<queue>
#include<vector>

using namespace std;

typedef long long ll;

const int MAX_N = 1000000;

int N, L[MAX_N];

ll solve() {
    ll ans = 0;

    priority_queue<int, vector<int>, greater<int> > que;

    for (int i = 0; i < N; i++) {
        que.push(L[i]);
    }

    while (que.size() > 1) {
        int l1, l2;
        l1 = que.top();
        que.pop();
        l2 = que.top();
        que.pop();
        ans += l1 + l2;
        que.push(l1 + l2);
    }

    return ans;

}

int main() {
    N = 3;
    L[0] = 8;
    L[1] = 5;
    L[2] = 8;
    ll ans = solve();
    printf("%lld\n", ans);
    return 0;
}
