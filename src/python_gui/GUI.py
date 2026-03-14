import tkinter as tk 
from tkinter import messagebox
from tkinter import filedialog
import config
import sudoku_c
from OCR import read_sudoku

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku")

        self.canvas = tk.Canvas(root, width = config.GRID_WIDTH, height = config.GRID_HEIGHT)
        self.canvas.pack()

        frame = tk.Frame(root)
        frame.pack()

        btn1 = tk.Button(frame, text = "Scan", command=self.scan_board)
        btn1.pack(side = "left")
        btn2 = tk.Button(frame, text = "Check", command=self.check_board)
        btn2.pack(side = "left")
        btn3 = tk.Button(frame, text = "Solve", command=self.solve_board)
        btn3.pack(side = "left")
        btn4 = tk.Button(frame, text = "Clear", command=self.clear_board)
        btn4.pack(side = "left")

        self.board = [[0 for _ in range(config.GRID_SIZE)] for _ in range(config.GRID_SIZE)]

        self.selected_row = None
        self.selected_col = None

        self.draw_grid()

        self.canvas.bind("<Button-1>", self.select_cell)
        self.root.bind("<Key>", self.key_pressed)

    def draw_grid(self):
        self.canvas.delete("all")

        for i in range(config.GRID_SIZE + 1):
            width = 3 if i % 3 == 0 else 1
            pos = i * config.CELL_SIZE

            self.canvas.create_line(pos, 0, pos, config.GRID_SIZE * config.CELL_SIZE, width = width)
            self.canvas.create_line(0, pos, config.GRID_SIZE * config.CELL_SIZE, pos, width = width)
        
        for r in range(config.GRID_SIZE):
                    for c in range(config.GRID_SIZE):
                        num = self.board[r][c]
                        if num != 0:
                            x = c * config.CELL_SIZE + config.CELL_SIZE // 2
                            y = r * config.CELL_SIZE + config.CELL_SIZE // 2
                            self.canvas.create_text(x, y, text=str(num), font=("Arial", 15))

        if self.selected_row is not None:
            x1 = self.selected_col * config.CELL_SIZE
            y1 = self.selected_row * config.CELL_SIZE
            x2 = x1 + config.CELL_SIZE
            y2 = y1 + config.CELL_SIZE
            self.canvas.create_rectangle(x1, y1, x2, y2, outline="red", width = 3)

    def select_cell(self, event):
        col = event.x // config.CELL_SIZE
        row = event.y // config.CELL_SIZE

        if row < config.GRID_SIZE and col < config.GRID_SIZE:
            self.selected_row = row
            self.selected_col = col
            self.draw_grid()

    def key_pressed(self, event):
        if self.selected_row is None:
            return

        if event.char in "123456789":
            self.board[self.selected_row][self.selected_col] = int(event.char)

        if event.keysym == "BackSpace":
            self.board[self.selected_row][self.selected_col] = 0

        self.draw_grid()

    def scan_board(self):
        file_path = filedialog.askopenfilename(
            title="Select Sudoku image",
            filetypes=[("Image files", "*.png *.jpg ")]
        )
        if not file_path:
            return

        self.board = read_sudoku(file_path)
        self.draw_grid()

    def check_board(self):
        if not sudoku_c.check(self.board):
            tk.messagebox.showinfo(title=None, message='wrong')
        else:
            tk.messagebox.showinfo(title=None, message='fine')
            
    def solve_board(self):
        success, self.board = sudoku_c.solve(self.board)
        if not success:
            tk.messagebox.showinfo(title=None, message='wrong')
        self.draw_grid()

    def clear_board(self):
        for r in range(config.GRID_SIZE):
                    for c in range(config.GRID_SIZE):
                        self.board[r][c] = 0
        self.draw_grid()


root = tk.Tk()
app = SudokuGUI(root)
root.mainloop()