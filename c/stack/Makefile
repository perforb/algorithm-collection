CC      = gcc
CFLAGS  = -g -Wall -Wextra
OBJS    = main.o stack.o
PROGRAM = stack

all: $(PROGRAM)

$(PROGRAM): main.c stack.c
	$(CC) main.c stack.c -o $(PROGRAM)

clean:
	rm -f *.o *.exe $(PROGRAM)

.PHONY: \
	all \
	stack \
	clean
