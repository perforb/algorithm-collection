CC      = gcc
CFLAGS  = -g -Wall -Wextra
OBJS    = main.o stack.o

all: stack

stack: main.c stack.c
	$(CC) main.c stack.c -o stack

rpn: rpn.c stack.c reverse_polish_notation.c
	$(CC) rpn.c stack.c reverse_polish_notation.c -o rpn

clean:
	rm -f *.o *.exe *.stackdump stack rpn

.PHONY: \
	all \
	stack \
	clean
