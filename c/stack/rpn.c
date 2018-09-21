#include <stdio.h>
#include "stack.h"
#include "reverse_polish_notation.h"

int main(int argc, char const *argv[]) {
    char s[100];
    Stack stack = {
        0,
    };
    while (scanf("%s", s) != EOF) {
        run(&stack, s);
    }

    printf("%d\n", pop(&stack));
    return 0;
}
