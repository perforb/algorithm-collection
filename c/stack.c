#include<stdio.h>

typedef struct {
    int top;
    int elements[1000];
} stack;

void push(stack *s, int number) {
    s->top++;
    s->elements[s->top] = number;
}

int pop(stack *s) {
    if (s->top <= 0) {
        return s->elements[0];
    }
    return s->elements[s->top--];
}

int main(int argc, char const *argv[]) {
    stack s = {
        0,
    };

    push(&s, 3);
    push(&s, 2);
    push(&s, 1);

    printf("%d\n", pop(&s)); // 1
    printf("%d\n", pop(&s)); // 2
    printf("%d\n", pop(&s)); // 3
    printf("%d\n", pop(&s)); // 0

    push(&s, 11);

    printf("%d\n", pop(&s)); // 11
    printf("%d\n", pop(&s)); // 0

    return 0;
}
