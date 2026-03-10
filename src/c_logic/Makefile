CC = gcc
CFLAGS = -Wall -O2 -fPIC
LIBNAME = libsudoku.so

SRC = sudoku.c internal.c
OBJ = $(SRC:.c=.o)

all: $(LIBNAME)

$(LIBNAME): $(OBJ)
	$(CC) -shared -o $@ $^

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

test:
	$(CC) $(SRC) ../../tests/test_logic.c -o test

clean:
	rm -f $(OBJ) $(LIBNAME) test
