# Matrix Chain Multiplication Visualizer

A Python application with a graphical user interface (GUI) to visualize the Matrix Chain Multiplication problem using dynamic programming. This tool allows users to find the optimal order of parenthesizing matrices to minimize the number of scalar multiplications.

## Features

- **Input Dimensions:** Enter matrix dimensions as a comma-separated list (e.g., `10,20,30,40,50`).
- **Optimal Parenthesization:** Displays the best way to parenthesize matrices for minimum multiplications.
- **Cost Matrix Display:** Shows the cost matrix representing the minimum number of multiplications for each subproblem.
- **User-Friendly GUI:** Built using `tkinter` for an interactive and intuitive user experience.

## Screenshots

![image](https://github.com/user-attachments/assets/5026d2e7-1d74-4ae8-8ecc-487fbc34d9b3)
![image](https://github.com/user-attachments/assets/efaa8841-9a8f-4607-8860-584df3d94014)



1. Install Python (if not already installed). This project requires Python 3.6+.
2. Run the application:
python app.py
3. Enter the matrix dimensions in the input box and click "Show Parenthesization" to view the results.
### Requirements:
Python 3.6+
tkinter (included in most Python installations)
ttk module for enhanced GUI widgets
### File Structure:
app.py: Main application script containing the logic and GUI implementation.
