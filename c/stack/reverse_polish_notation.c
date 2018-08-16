#include<stdlib.h>
#include "stack.h"

void reversePolishNotation(Stack *stack, char s[]) {
    if (s[0] == '+') {
        int a = pop(stack);
        int b = pop(stack);
        push(stack, a + b);
    } else if (s[0] == '-') {
        int b = pop(stack);
        int a = pop(stack);
        push(stack, a - b);
    } else if (s[0] == '*') {
        int a = pop(stack);
        int b = pop(stack);
        push(stack, a * b);
    } else {
        push(stack, atoi(s));
    }
}
