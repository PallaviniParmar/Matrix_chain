import tkinter as tk
from tkinter import ttk, messagebox

class MatrixChainMultiplication:
    def __init__(self, dimensions):
        self.dimensions = dimensions
        self.n = len(dimensions) - 1
        self.m = [[0 if i == j else float("inf") for j in range(self.n)] for i in range(self.n)]
        self.s = [[0] * self.n for _ in range(self.n)]
        self.compute_optimal_order()

    def compute_optimal_order(self):
        for l in range(2, self.n + 1):
            for i in range(self.n - l + 1):
                j = i + l - 1
                for k in range(i, j):
                    q = self.m[i][k] + self.m[k+1][j] + self.dimensions[i] * self.dimensions[k+1] * self.dimensions[j+1]
                    if q < self.m[i][j]:
                        self.m[i][j] = q
                        self.s[i][j] = k

    def get_optimal_order(self, i, j):
        if i == j:
            return f"A{i+1}"
        else:
            k = self.s[i][j]
            left = self.get_optimal_order(i, k)
            right = self.get_optimal_order(k+1, j)
            return f"({left} x {right})"

class MatrixChainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Matrix Chain Multiplication Visualizer")
        self.geometry("1000x700")
        self.configure(bg="#282c34")
        self.resizable(True, True)

        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self, text="Matrix Chain Multiplication Visualizer",
                               font=("Helvetica", 20, "bold"), fg="#61afef", bg="#282c34")
        title_label.grid(row=0, column=0, columnspan=3, pady=(20, 10))

        entry_frame = tk.Frame(self, bg="#282c34")
        entry_frame.grid(row=1, column=0, columnspan=3, pady=10, padx=10)

        entry_label = tk.Label(entry_frame, text="Enter Matrix Dimensions (comma-separated):",
                               font=("Helvetica", 12), fg="#abb2bf", bg="#282c34")
        entry_label.pack(side="left")

        self.entry = tk.Entry(entry_frame, font=("Helvetica", 12), width=30, bg="#3e4451", fg="white",
                              highlightbackground="#61afef", highlightcolor="#61afef", highlightthickness=1)
        self.entry.pack(side="left", padx=5)

        parenthesize_button = tk.Button(entry_frame, text="Show Parenthesization", command=self.show_parenthesization,
                                        font=("Helvetica", 12, "bold"), bg="#98c379", fg="white",
                                        activebackground="#61afef", activeforeground="white")
        parenthesize_button.pack(side="left", padx=5)

        self.create_parenthesization_section()
        self.create_cost_matrix_section()

        action_frame = tk.Frame(self, bg="#282c34")
        action_frame.grid(row=8, column=0, columnspan=3, pady=(20, 10))

        back_button = tk.Button(action_frame, text="Back", command=self.destroy,
                                font=("Helvetica", 12, "bold"), bg="#e06c75", fg="white",
                                activebackground="#61afef", activeforeground="white")
        back_button.pack(side="left", padx=10)

    def create_parenthesization_section(self):
        parenthesization_label = tk.Label(self, text="Best Way to Parenthesize:", font=("Helvetica", 14, "bold"),
                                          fg="#98c379", bg="#282c34")
        parenthesization_label.grid(row=2, column=0, columnspan=3, pady=(20, 5))

        self.parenthesization_text = tk.Text(self, width=100, height=3, wrap="word", font=("Helvetica", 12),
                                             bg="#3e4451", fg="white",
                                             highlightbackground="#61afef", highlightcolor="#61afef", highlightthickness=1)
        self.parenthesization_text.grid(row=3, column=0, columnspan=3, padx=10, pady=5)

    def create_cost_matrix_section(self):
        cost_matrix_label = tk.Label(self, text="Cost Matrix (Minimum Multiplications):", font=("Helvetica", 14, "bold"),
                                     fg="#e5c07b", bg="#282c34")
        cost_matrix_label.grid(row=4, column=0, columnspan=3, pady=(20, 5))

        # Cost Matrix Table using Treeview
        self.cost_matrix_table = ttk.Treeview(self, show="headings", selectmode="none")
        self.cost_matrix_table.grid(row=5, column=0, columnspan=3, padx=10, pady=5)
        
        self.cost_matrix_table.heading("#0", text="", anchor="center")

    def show_parenthesization(self):
        dimensions = self.entry.get().strip()
        if not dimensions:
            messagebox.showerror("Input Error", "Please enter the matrix dimensions.")
            return
        try:
            dimensions = list(map(int, dimensions.split(',')))
            if len(dimensions) < 2:
                messagebox.showerror("Input Error", "Please enter at least two dimensions.")
                return
            mcm = MatrixChainMultiplication(dimensions)
            optimal_order = mcm.get_optimal_order(0, mcm.n - 1)
            self.update_parenthesization(optimal_order)
            self.update_cost_matrix(mcm.m)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid integers separated by commas.")

    def update_parenthesization(self, optimal_order):
        self.parenthesization_text.delete("1.0", "end")
        self.parenthesization_text.insert("end", optimal_order)

    def update_cost_matrix(self, m):
        # Clear any existing columns in the table
        for col in self.cost_matrix_table["columns"]:
            self.cost_matrix_table.delete(*self.cost_matrix_table.get_children())
            self.cost_matrix_table["columns"] = ()

        # Configure the table columns dynamically based on the cost matrix size
        columns = [f"Col{i+1}" for i in range(len(m))]
        self.cost_matrix_table["columns"] = columns
        for i, col in enumerate(columns):
            self.cost_matrix_table.heading(col, text=f"{i+1}")
            self.cost_matrix_table.column(col, width=100, anchor="center")

        # Insert the cost matrix values row by row
        for i, row in enumerate(m):
            row_values = [f"{val}" if val != float("inf") else "∞" for val in row]
            self.cost_matrix_table.insert("", "end", values=row_values)

if __name__ == "__main__":
    app = MatrixChainApp()
    app.mainloop()


