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
from tabulate import tabulate

def get_points():
    """
    Prompt the user to enter points as coordinates and return a list of points.
    """
    coordinates = []
    x_coords = []
    print('''Please enter the points as coordinates in the format 'x y'. 
Press Enter without typing anything to finish.''')
    number = 1
    while True:
        try:
            point_input = input(f"Point {number}: ").strip()
            if not point_input:
                if not coordinates:
                    print('No points entered!')
                    continue
                break  # Break the loop if the input is empty
            x_coordinate, y_coordinate = map(float, point_input.split(' '))
            if x_coordinate in x_coords:
                print('Abscissae cannot be the same!')
                continue
            coordinates.append((x_coordinate, y_coordinate))
            x_coords.append(x_coordinate)
            number += 1
        except:
            print('Please enter a valid point as two numbers separated by a space.')
    headers = ['x', 'f(x)']
    coordinates = list(set(coordinates))
    print(tabulate(coordinates, headers=headers))
    return coordinates

def lagrange_interpolation(coordinates):
    """
    Perform Lagrange interpolation on the given points and return a list of Lagrange polynomials.
    """
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
    """
    Compute the Lagrange polynomial for the given points.
    """
    interpolated_polynomials = lagrange_interpolation(coordinates)
    poly = np.poly1d(0)
    for coordinate, lagrange_poly in zip(coordinates, interpolated_polynomials):
        poly += lagrange_poly * coordinate[1]
    return poly

def plot_polynomial(polynomial, points):
    """
    Plot the polynomial and the given points.
    """
    x_values = np.linspace(min(point[0] for point in points), max(point[0] for point in points), 100)
    y_values = polynomial(x_values)
    plt.plot(x_values, y_values, label='Lagrange Polynomial')
    plt.scatter(*zip(*points), color='red', label='Given Points')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Lagrange Interpolation')
    plt.legend()
    plt.grid(True)
    plt.show()

def explain_lagrange_polynomial():
    """
    Provides a user-friendly explanation of the Lagrange polynomial and its concept.
    """
    print("Lagrange Polynomial Explained:\n")
    print("**What is a Lagrange Polynomial?**")
    print("The Lagrange polynomial is a mathematical method used for interpolation, which means it helps us find a smooth curve that passes through a set of given points.\n")

    print("**How Does it Work?**")
    print("Imagine you have a set of points on a graph. The Lagrange polynomial calculates a polynomial equation that connects these points smoothly. It's like drawing a curve that touches each point exactly.\n")

    print("**Why is it Useful?**")
    print("Interpolation is handy when you want to estimate values between known data points. For example, if you know the temperature at 9 AM and 12 PM, you can use interpolation to estimate the temperature at 10 AM.\n")

    print("**Understanding the Algorithm:**")
    print("1. **For each point:** We create a small polynomial (called a basis polynomial) that equals 1 at that point and 0 at all other points.")
    print("2. **Combine Polynomials:** We multiply each basis polynomial by the corresponding y-value and add them all together. This gives us the Lagrange polynomial.\n")

    print("**Example:**")
    print("Let's say we have points (1, 2), (2, 3), and (3, 4). The Lagrange polynomial method constructs a curve that smoothly passes through these points. This curve can help us estimate values at any point between 1 and 3.\n")

    print("**Why it Matters:**")
    print("The Lagrange polynomial method is widely used in various fields like physics, engineering, and computer graphics. It's a powerful tool for approximating functions and understanding data trends.\n")


if __name__ == '__main__':
    print('Welcome to your personal Lagrange Polynomial Generator!')
    explain_lagrange_polynomial()
    while True:
        print('-' * 50)
        state = input('Enter 1 to try the program, 0 to exit: ')
        if state == '1':
            points = get_points()
            p = get_polynomial(points)
            print("Lagrange Polynomial:", p)
            plot_polynomial(p, points)
        else:
            print('Goodbye!')
            sys.exit()

