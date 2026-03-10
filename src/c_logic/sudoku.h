#ifndef SUDOKU_H
#define SUDOKU_H

#include <stdbool.h>

bool is_sudoku_valid(const int grid[9][9]);
bool sudoku_solve(int grid[9][9]);
bool sudoku_is_solved(const int grid[9][9]);

#endif //SUDOKU_H