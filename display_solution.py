import tkinter as tk
from tkinter import ttk
import time



def display_solution(solution):
    if solution is None:
        print("No solution found!")
        return

    solution_states = []
    current_node = solution
    while current_node:
        solution_states.append(current_node.state)
        current_node = current_node.parent

    solution_states.reverse()

    root = tk.Tk()
    root.title("8-Queen Problem Solution")

    canvas = tk.Canvas(root)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scroll = ttk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.configure(yscrollcommand=scroll.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor=tk.NW)

    for index, state in enumerate(solution_states):
        for row in range(8):
            for col in range(8):
                label = tk.Label(frame, width=4, height=2, relief="solid")
                label.grid(row=row, column=col)
                if state[col] == row:
                    label.config(text='Q', font=("Arial", 12, "bold"))
                elif (row + col) % 2 == 0:
                    label.config(bg="white")
                else:
                    label.config(bg="gray")

        if index < len(solution_states) - 1:
            time.sleep(1)

        root.update()

    root.mainloop()