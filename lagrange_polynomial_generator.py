"""
This script performs Lagrange interpolation for a set of points entered by the user.
It prompts the user to input points as coordinates in the format 'x y' and displays them.
Then, it computes the Lagrange polynomial that interpolates the given points, computes the polynomial and plots a graph.

Author: Muddassir Khalidi
Date: 14 February 2024

Example:
    $ python lagrange_polynomial_generator.py
    Please enter the points as coordinates in the format 'x y'. 
    Press Enter without typing anything to finish.
    Point 1: 1 2
    Point 2: 2 3
    Point 3: 3 4
    x    f(x)
    ---  ------
    1     2
    2     3
    3     4
    1.0 * x^2 + -3.0 * x + 2.0
"""

import numpy as np
import matplotlib.pyplot as plt
import sys
from tkinter import *
from tkinter import messagebox
from tabulate import tabulate
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def get_points():
    coordinates = []
    x_coords = []
    points = point_entries.get("1.0", END).strip().split("\n")
    for number, point in enumerate(points, start=1):
        try:
            x_coordinate, y_coordinate = map(float, point.split())
            if x_coordinate in x_coords:
                messagebox.showerror("Error", "Abscissae cannot be the same!")
                return None
            coordinates.append((x_coordinate, y_coordinate))
            x_coords.append(x_coordinate)
        except ValueError:
            messagebox.showerror("Error", f"Invalid point format at point {number}!")
            return None

    headers = ['x', 'f(x)']
    coordinates = list(set(coordinates))
    points_display.config(state=NORMAL)
    points_display.delete("1.0", END)
    points_display.insert(END, tabulate(coordinates, headers=headers))
    points_display.config(state=DISABLED)
    return coordinates

def lagrange_interpolation(coordinates):
    lagrange_polynomials = []
    for point_x in coordinates:
        poly = np.poly1d([1.0])
        denominator = 1
        for other_point in coordinates:
            if point_x == other_point:
                continue
            poly = np.polymul(poly, np.poly1d([1, -other_point[0]]))
            denominator *= point_x[0] - other_point[0]
        lagrange_polynomials.append(poly / denominator)
    return lagrange_polynomials

def get_polynomial(coordinates):
    interpolated_polynomials = lagrange_interpolation(coordinates)
    poly = np.poly1d(0)
    for coordinate, lagrange_poly in zip(coordinates, interpolated_polynomials):
        poly += lagrange_poly * coordinate[1]
    return poly

def plot_polynomial(polynomial, points):
    x_values = np.linspace(min(point[0] for point in points), max(point[0] for point in points), 100)
    y_values = polynomial(x_values)
    ax.clear()
    ax.plot(x_values, y_values, label='Lagrange Polynomial')
    ax.scatter(*zip(*points), color='red', label='Given Points')
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.set_title('Lagrange Interpolation')
    ax.legend()
    ax.grid(True)
    canvas.draw()

def on_generate_click():
    points = get_points()
    if points:
        p = get_polynomial(points)
        polynomial_display.config(state=NORMAL)
        polynomial_display.delete("1.0", END)
        polynomial_display.insert(END, "Lagrange Polynomial:\n")
        polynomial_display.insert(END, str(p))
        polynomial_display.config(state=DISABLED)
        plot_polynomial(p, points)

def explain_lagrange_polynomial():
    explanation = """
Lagrange Polynomial Explained:

**What is a Lagrange Polynomial?**
The Lagrange polynomial is a mathematical method used for interpolation, which means it helps us find a smooth curve that passes through a set of given points.

**How Does it Work?**
Imagine you have a set of points on a graph. The Lagrange polynomial calculates a polynomial equation that connects these points smoothly. It's like drawing a curve that touches each point exactly.

**Why is it Useful?**
Interpolation is handy when you want to estimate values between known data points. For example, if you know the temperature at 9 AM and 12 PM, you can use interpolation to estimate the temperature at 10 AM.

**Understanding the Algorithm:**
1. **For each point:** We create a small polynomial (called a basis polynomial) that equals 1 at that point and 0 at all other points.
2. **Combine Polynomials:** We multiply each basis polynomial by the corresponding y-value and add them all together. This gives us the Lagrange polynomial.

**Example:**
Let's say we have points (1, 2), (2, 3), and (3, 4). The Lagrange polynomial method constructs a curve that smoothly passes through these points. This curve can help us estimate values at any point between 1 and 3.

**Why it Matters:**
The Lagrange polynomial method is widely used in various fields like physics, engineering, and computer graphics. It's a powerful tool for approximating functions and understanding data trends.
"""
    messagebox.showinfo("Lagrange Polynomial Explanation", explanation)


# GUI Setup
root = Tk()
root.title("Lagrange Polynomial Generator")

frame = Frame(root)
frame.pack(padx=10, pady=10)

label = Label(frame, text="Enter points as 'x y' (one per line):")
label.grid(row=0, column=0, sticky=W)

point_entries = Text(frame, width=40, height=6)
point_entries.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

generate_button = Button(frame, text="Generate Polynomial", command=on_generate_click)
generate_button.grid(row=2, column=0, pady=5)

explanation_button = Button(frame, text="Explanation", command=explain_lagrange_polynomial)
explanation_button.grid(row=2, column=1, pady=5)

points_display = Text(frame, width=40, height=6, state=DISABLED)
points_display.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

polynomial_display = Text(frame, width=40, height=6, state=DISABLED)
polynomial_display.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# Create a figure and canvas for plotting
fig, ax = plt.subplots(figsize=(6, 4))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

root.mainloop()
