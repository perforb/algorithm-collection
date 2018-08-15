#ifndef STACK_H
#define STACK_H

typedef struct {
    int top;
    int elements[1000];
} Stack;

void push(Stack *s, int number);

int pop(Stack *s);

#endif
