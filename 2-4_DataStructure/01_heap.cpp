#include<stdio.h>

const int MAX_N = 5000;

int heap[MAX_N], sz;

void push(int);
int pop();

void push(int x) {
    int i = sz++;

    while (i > 0) {
        int p = (i - 1) / 2;
        if (heap[p] <= x) break;
        heap[i] = heap[p];
        i = p;
    }

    heap[i] = x;
}

int pop() {
    int ret = heap[0];

    int x = heap[--sz];

    int i = 0;
    while (i * 2 + 1 < sz) {
        int a = i * 2 + 1, b = i * 2 + 2;
        if (b < sz && heap[b] < heap[a]) a = b;

        if (heap[a] >= x) break;

        heap[i] = heap[a];
        i = a;
    }

    heap[i] = x;

    return ret;
}

int main() {

    int i;
    for (i = 0; i < 10; i++) push(i);
    for (i = 0; i < 10; i++) printf("pop:%d\n", pop());

    return 0;
}
