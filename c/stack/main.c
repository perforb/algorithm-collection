#include <stdio.h>
#include "stack.h"

int main(int argc, char const *argv[]) {
    Stack stack = {
        0,
    };

    push(&stack, 3);
    push(&stack, 2);
    push(&stack, 1);

    printf("%d\n", pop(&stack)); // 1
    printf("%d\n", pop(&stack)); // 2
    printf("%d\n", pop(&stack)); // 3
    printf("%d\n", pop(&stack)); // 0

    push(&stack, 11);

    printf("%d\n", pop(&stack)); // 11
    printf("%d\n", pop(&stack)); // 0

    return 0;
}
