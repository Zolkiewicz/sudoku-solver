import tkinter as tk 

GRID_SIZE = 9
CELL_SIZE = 50
GRID_WIDTH = GRID_SIZE * CELL_SIZE
GRID_HEIGHT = GRID_SIZE * CELL_SIZE

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku")

        self.canvas = tk.Canvas(root, width = GRID_WIDTH, height = GRID_HEIGHT)
        self.canvas.pack()

        frame = tk.Frame(root)
        frame.pack()

        btn1 = tk.Button(frame, text = "Scan", command=self.scan_board)
        btn1.pack(side = "left")
        btn2 = tk.Button(frame, text = "Check", command=self.check_board)
        btn2.pack(side = "left")
        btn3 = tk.Button(frame, text = "Solve", command=self.solve_board)
        btn3.pack(side = "left")

        self.board = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

        self.selected_row = None
        self.selected_col = None

        self.draw_grid()

        self.canvas.bind("<Button-1>", self.select_cell)
        self.root.bind("<Key>", self.key_pressed)

    def draw_grid(self):
        self.canvas.delete("all")

        for i in range(GRID_SIZE + 1):
            width = 3 if i % 3 == 0 else 1
            pos = i * CELL_SIZE

            self.canvas.create_line(pos, 0, pos, GRID_SIZE * CELL_SIZE, width = width)
            self.canvas.create_line(0, pos, GRID_SIZE * CELL_SIZE, pos, width = width)
        
        for r in range(GRID_SIZE):
                    for c in range(GRID_SIZE):
                        num = self.board[r][c]
                        if num != 0:
                            x = c * CELL_SIZE + CELL_SIZE // 2
                            y = r * CELL_SIZE + CELL_SIZE // 2
                            self.canvas.create_text(x, y, text=str(num), font=("Arial", 15))

        if self.selected_row is not None:
            x1 = self.selected_col * CELL_SIZE
            y1 = self.selected_row * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE
            self.canvas.create_rectangle(x1, y1, x2, y2, outline="red", width = 3)

    def select_cell(self, event):
        col = event.x // CELL_SIZE
        row = event.y // CELL_SIZE

        if row < GRID_SIZE and col < GRID_SIZE:
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
        print("Scan clicked")

    def check_board(self):
        print("Check clicked")

    def solve_board(self):
        print("Solve clicked")

root = tk.Tk()
app = SudokuGUI(root)
root.mainloop()