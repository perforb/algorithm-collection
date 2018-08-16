#ifndef STACK_H
#define STACK_H

typedef struct {
    int top;
    int elements[1000];
} Stack;

void push(Stack *stack, int number);

int pop(Stack *stack);

#endif
