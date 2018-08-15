#ifndef STACK_H
#define STACK_H

typedef struct {
    int top;
    int elements[1000];
} stack;

void push(stack *s, int number);

int pop(stack *s);

#endif
