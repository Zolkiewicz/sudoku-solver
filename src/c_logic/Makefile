CC = gcc
CFLAGS = -Wall -O2 -fPIC
LIBNAME = libsudoku.so

SRC = sudoku.c
OBJ = $(SRC:.c=.o)

all: $(LIBNAME)

$(LIBNAME): $(OBJ)
	$(CC) -shared -o $@ $^

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

test: $(LIBNAME)
	$(CC) ../../tests/test_logic.c -L. -lsudoku -Wl,-rpath,. -o test

clean:
	rm -f $(OBJ) $(LIBNAME) test