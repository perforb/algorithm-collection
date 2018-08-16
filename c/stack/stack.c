#include "stack.h"

void push(Stack *stack, int number) {
    stack->top++;
    stack->elements[stack->top] = number;
}

int pop(Stack *stack) {
    if (stack->top <= 0) {
        return stack->elements[0];
    }
    return stack->elements[stack->top--];
}
