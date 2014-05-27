#include<stdio.h>
#include<queue>

using namespace std;

int main() {

    int i;

    priority_queue<int> pque;

    for (i = 0; i < 10; i++) pque.push(i);

    while (!pque.empty()) {
        printf("pop: %d\n", pque.top()); pque.pop();
    }
}
