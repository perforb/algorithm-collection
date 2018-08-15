#include <stdio.h>
#include "stack.h"

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
