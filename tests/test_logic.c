#include "../src/c_logic/sudoku.h"
#include <assert.h>
#include <stdio.h>

int main(void) {
    int sudoku1[9][9];
    int sudoku2[9][9];
    int sudoku3[9][9];
    FILE *file = fopen("../../data/examples.txt", "r"); // nazwa pliku

    if (file == NULL) {
        printf("error\n");
        return 1;
    }

    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            if (fscanf(file, "%d", &sudoku1[i][j]) != 1) {
                printf("Błąd wczytywania pierwszego Sudoku!\n");
                fclose(file);
                return 1;
            }
        }
    }

    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            if (fscanf(file, "%d", &sudoku2[i][j]) != 1) {
                printf("Błąd wczytywania drugiego Sudoku!\n");
                fclose(file);
                return 1;
            }
        }
    }


    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            if (fscanf(file, "%d", &sudoku3[i][j]) != 1) {
                printf("Błąd wczytywania trzeciego Sudoku!\n");
                fclose(file);
                return 1;
            }
        }
    }

    fclose(file);

     for (int p = 0; p < 3; p++) {
        printf("\nSudoku %d:\n", p + 1);
        int (*sudoku)[9];
        if (p == 0) sudoku = sudoku1;
        else if (p == 1) sudoku = sudoku2;
        else sudoku = sudoku3;

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                printf("%d ", sudoku[i][j]);
            }
            printf("\n");
        }
    }

    assert(is_sudoku_valid(sudoku1));
    assert(sudoku_solve(sudoku1));
    assert(sudoku_is_solved(sudoku1));
    assert(is_sudoku_valid(sudoku2));
    assert(sudoku_is_solved(sudoku2));
    assert(sudoku_solve(sudoku2));
    assert(sudoku_is_solved(sudoku2));
    assert(!is_sudoku_valid(sudoku3));
    assert(!sudoku_is_solved(sudoku3));

    return 0;
}
