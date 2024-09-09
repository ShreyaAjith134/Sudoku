import tkinter as tk
from tkinter import messagebox
import random

difficulty = 0  # This will store the chosen difficulty level

def set_difficulty(level, chooser_window, root):
    global difficulty
    difficulty = level
    chooser_window.destroy()  # Close the chooser window after selecting difficulty
    app = SudokuGUI(root)  # Start the Sudoku game with the selected difficulty

class DifficultyChooser:
    def __init__(self, root):
        chooser_window = tk.Toplevel(root)  # Create a separate window for choosing difficulty
        chooser_window.title("Choose Difficulty")
        chooser_window.geometry("300x200")

        # Label for instruction
        label = tk.Label(chooser_window, text="Choose Difficulty Level", font=("Arial", 16))
        label.pack(pady=20)

        # Buttons for difficulty levels
        easy_button = tk.Button(chooser_window, text="Easy", width=10, command=lambda: set_difficulty(1, chooser_window, root))
        easy_button.pack(pady=5)

        medium_button = tk.Button(chooser_window, text="Medium", width=10, command=lambda: set_difficulty(2, chooser_window, root))
        medium_button.pack(pady=5)

        hard_button = tk.Button(chooser_window, text="Hard", width=10, command=lambda: set_difficulty(3, chooser_window, root))
        hard_button.pack(pady=5)

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku")
        self.root.geometry("550x600")
        self.grid = [[0] * 9 for _ in range(9)]
        self.entries = [[None] * 9 for _ in range(9)]
        
        self.create_grid()

        if difficulty == 1:
            self.generate_puzzle_easy()
        elif difficulty == 2:
            self.generate_puzzle_medium()
        elif difficulty == 3:
            self.generate_puzzle_difficult()

        # Create "Check Solution" Button
        check_button = tk.Button(self.root, text="Check Solution", command=self.check_solution)
        check_button.grid(row=10, column=0, columnspan=9, pady=10)

    def create_grid(self):
        for row in range(9):
            for col in range(9):
                entry = tk.Entry(self.root, width=3, font=('Arial', 18), justify='center')
                entry.grid(row=row, column=col, padx=5, pady=5, ipady=5)
                self.entries[row][col] = entry

    def generate_puzzle_easy(self):
        # Randomly generate numbers in some cells
        for i in range(9):
            for j in range(9):
                if random.random() > 0.5:
                    num = random.randint(1, 9)
                    self.grid[i][j] = num
                    self.entries[i][j].insert(0, str(num))
                    self.entries[i][j].config(state='disabled')  # Disable entry for pre-filled numbers

    def generate_puzzle_medium(self):
        # Randomly generate numbers in some cells
        for i in range(9):
            for j in range(9):
                if random.random() > 0.6:
                    num = random.randint(1, 9)
                    self.grid[i][j] = num
                    self.entries[i][j].insert(0, str(num))
                    self.entries[i][j].config(state='disabled') 

    def generate_puzzle_difficult(self):
        # Randomly generate numbers in some cells
        for i in range(9):
            for j in range(9):
                if random.random() > 0.7:
                    num = random.randint(1, 9)
                    self.grid[i][j] = num
                    self.entries[i][j].insert(0, str(num))
                    self.entries[i][j].config(state='disabled') 

    def check_solution(self):
        try:
            for row in range(9):
                for col in range(9):
                    value = self.entries[row][col].get()
                    if not value.isdigit() or not (1 <= int(value) <= 9):
                        raise ValueError(f"Invalid input at row {row + 1}, col {col + 1}")

                    # Updating grid with user's values
                    self.grid[row][col] = int(value)

            if self.is_valid_solution():
                messagebox.showinfo("Success", "Congratulations! You solved the puzzle.")
            else:
                messagebox.showerror("Error", "Incorrect solution. Try again.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def is_valid_solution(self):
        # Check rows, columns, and 3x3 grids for Sudoku validity
        for i in range(9):
            if not self.is_valid_block(self.grid[i]):  # Check rows
                return False
            if not self.is_valid_block([self.grid[x][i] for x in range(9)]):  # Check columns
                return False

        # Check 3x3 subgrids
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                subgrid = [self.grid[r][c] for r in range(i, i + 3) for c in range(j, j + 3)]
                if not self.is_valid_block(subgrid):
                    return False

        return True

    def is_valid_block(self, block):
        # A valid block must contain all digits from 1 to 9 exactly once
        return sorted(block) == list(range(1, 10))

if __name__ == "__main__":
    root = tk.Tk()  # Main root window
    DifficultyChooser(root)  # Open difficulty chooser first
    root.mainloop()  # Start the main event loop
