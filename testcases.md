1. **Basic Test Case**:
   - Input: (1, 2), (2, 3), (3, 4)
   - Expected Output: The Lagrange polynomial and the corresponding graph should be displayed.

2. **Vertical Line**:
   - Input: (1, 2), (1, 3), (1, 4)
   - Expected Output: The Lagrange polynomial and the corresponding graph should be displayed.
   - This case tests how the program handles multiple points with the same x-coordinate.

3. **Horizontal Line**:
   - Input: (1, 2), (2, 2), (3, 2)
   - Expected Output: 2
   - This case tests how the program handles multiple points with the same y-coordinate.

4. **Single Point**:
   - Input: (1, 2)
   - Expected Output: The Lagrange polynomial should be equivalent to the given point, and a graph displaying this point should be shown.

5. **Two Points**:
   - Input: (1, 2), (3, 4)
   - Expected Output: x + 1
   
6. **Zero Points**:
   - Input: No input (just press Enter)
   - Expected Output: The program should show an error message2.

7. **Non-Numeric Input**:
   - Input: (a, b), (c, d), (e, f)
   - Expected Output: The program should prompt the user to enter valid points and handle non-numeric inputs gracefully.

8. **Negative Numbers**:
   - Input: (-1, 2), (-2, -3), (3, 4)
   - Expected Output: -0.9x^2 + 2.3x + 5.2

9. **Large Numbers**:
   - Input: (1000, 2000), (2000, 3000), (3000, 4000)
   - Expected Output: x + 1000

10. **Repeated Points**:
    - Input: (1, 2), (1, 2), (3, 4)
    - Expected Output: x + 1
    - Treating repeated points as distinct points.
