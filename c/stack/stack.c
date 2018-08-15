#include "stack.h"

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
