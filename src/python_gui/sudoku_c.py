import ctypes
import config

lib = ctypes.CDLL("../c_logic/libsudoku.so")

Row = ctypes.c_int * config.GRID_SIZE
Grid = Row * config.GRID_SIZE

lib.is_sudoku_valid.argtypes = [ctypes.POINTER(Grid)]
lib.is_sudoku_valid.restype = ctypes.c_bool

lib.sudoku_solve.argtypes = [ctypes.POINTER(Grid)]
lib.sudoku_solve.restype = ctypes.c_bool

lib.sudoku_is_solved.argtypes = [ctypes.POINTER(Grid)]
lib.sudoku_is_solved.restype = ctypes.c_bool

def python_to_c(board):
    return Grid(*[Row(*row) for row in board])

def c_to_python(grid):
    return [[grid[r][c] for c in range(config.GRID_SIZE)] for r in range(config.GRID_SIZE)]

def solve(board):
    grid = python_to_c(board)
    success = lib.is_sudoku_valid(ctypes.byref(grid))
    if success is True:
        success = lib.sudoku_solve(ctypes.byref(grid))
    return success, c_to_python(grid)

def check(board):
    grid = python_to_c(board)
    return lib.is_sudoku_valid(ctypes.byref(grid))
