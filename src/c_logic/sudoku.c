#include "sudoku.h"

static bool can_place(const int grid[9][9], int num, int row, int col) {
    for (int i = 0; i < 9; i++) {
        if (col != i && grid[row][i] == num) return false;
        if (row != i && grid[i][col] == num) return false;
        
        int boxRow = 3 * (row / 3) + (i / 3);
        int boxCol = 3 * (col / 3) + (i % 3);
        if (boxRow == row && boxCol == col) continue;
        if (grid[boxRow][boxCol] == num) return false;
    }
    return true;
}

static bool find_empty(const int grid[9][9], int* row, int* col) {
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++){
            if (grid[i][j] == 0) {
                *row = i;
                *col = j;
                return true;
            }
        }
    }
    return false;
}

bool is_sudoku_valid(const int grid[9][9]) {
    for (int i = 0; i < 9; i++) { 
        for (int j = 0; j < 9; j++) {
            if (grid[i][j] == 0) continue;
            if (grid[i][j] < 0 || grid[i][j] > 9) return false;
            if (!can_place(grid, grid[i][j], i, j)) return false;
        }
    }

    return true;   
}

bool sudoku_solve(int grid[9][9]) {
    int row, col;
    if (!find_empty(grid, &row, &col)) return true;

    for (int num = 1; num <= 9; num++) {
        if (can_place(grid, num, row, col)) {
            grid[row][col] = num;
            if(sudoku_solve(grid)) return true;
            grid[row][col] = 0;
        }
    }
    return false;
}

bool sudoku_is_solved(const int grid[9][9]) {
    for (int i = 0; i < 9; i++) { 
        for (int j = 0; j < 9; j++) {
            if (grid[i][j] == 0) return false;
            if (!can_place(grid, grid[i][j], i, j)) return false;
        }
    }

    return true;   
}
