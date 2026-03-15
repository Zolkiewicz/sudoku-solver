# Sudoku Solver

A Python application for **solving and validating Sudoku puzzles**.

The project combines:

- **Python** for the graphical interface and image processing
- A **C library** for fast Sudoku validation and solving
- **OpenCV + Tesseract OCR** to read Sudoku boards from images

**Project repository:**  
https://github.com/Zolkiewicz/sudoku-solver.git

---

# How It's Made

## C Library

The core Sudoku logic is implemented in **C** for performance. The library exposes several functions that are used by the Python application.

### `bool is_sudoku_valid(const int grid[9][9]);`

Checks whether the current board configuration is valid.

It verifies that:

- No row contains duplicate numbers
- No column contains duplicate numbers
- No 3×3 subgrid contains duplicate numbers

Only the provided numbers are checked; empty cells (`0`) are ignored.

---

### `bool sudoku_solve(int grid[9][9]);`

Solves the Sudoku puzzle using a **backtracking algorithm**.

The solver:

1. Searches for an empty cell
2. Tries numbers **1–9**
3. Validates each number using internal helper functions
4. Recursively continues until the puzzle is solved or determined unsolvable



---

### `bool sudoku_is_solved(const int grid[9][9]);`

Checks whether the puzzle is completely solved.

It verifies that:

- All cells are filled
- The board satisfies all Sudoku constraints

---

# Python GUI

The graphical interface is built with **Tkinter**.

Features:

- Interactive **9×9 Sudoku board**
- Ability to **manually enter numbers**
- **Solve** puzzles using the C solver
- **Validate** puzzles
- **Clear** the board
- **Scan Sudoku from an image**

The GUI communicates with the C library through a Python wrapper (`sudoku_c`).

---

# OCR (Sudoku Image Recognition)

The OCR module uses:

- **OpenCV** for image preprocessing
- **Tesseract** for digit recognition

The pipeline works as follows:

### 1. Image preprocessing

The input image is:

- Converted to grayscale
- Blurred to reduce noise
- Thresholded using adaptive thresholding

This helps isolate the Sudoku grid.

---

### 2. Grid detection

Contours are detected and the **largest quadrilateral** is assumed to be the Sudoku board.

A **perspective transform** is then applied to obtain a perfectly square grid.

---

### 3. Cell extraction

The board is divided into **81 individual cells**.

Each cell is processed separately.

---

### 4. Cell cleaning

Each cell undergoes:

- grayscale conversion
- adaptive thresholding
- margin cropping
- morphological operations to remove noise

---

### 5. Digit recognition

Digits are recognized using **Tesseract OCR**.

Additional heuristics are used to improve accuracy:

- Empty cells are detected using pixel density
- Contour analysis counts **holes in digits**
- This helps differentiate confusing digits like **3 and 8**

---

# How to Run

## 1. Clone the repository

```bash
git clone https://github.com/Zolkiewicz/sudoku-solver.git
cd sudoku-solver
```

---

## 2. Create Python virtual environment

```bash
make venv
```

---

## 3. Build the C library

```bash
make clib
```

---

## 4. Install dependencies

```bash
make install
```

---

## 5. Run the GUI

Navigate to the Python GUI directory:

```bash
cd src/python_gui
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

Run the application.

```bash
python GUI.py
```
---

## 6. Deactivate environment

```bash
deactivate
```

---

## 7. Clean build files

From the project root directory:

```bash
make clean
```

---

# Technologies Used

- **Python**
- **C**
- **Tkinter**
- **OpenCV**
- **Tesseract OCR**
- **NumPy**
