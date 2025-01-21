# matrix_mul.py
import pandas as pd
import numpy as np

# Load data
# data = pd.read_csv('path/to/data')

# Benitha Uwituze: Input arrays
Prices = [[300, 500],         
          [1000, 120.85]]

Array2 = [200, 100]          

# Benitha Uwituze and Roxannne Niteka: Multiply the input arrays

# Initialize empty list to store results
Ans = []

# Iterate through each row of Prices matrix and multiply each element with corresponding element in Array2
for i in range(len(Prices)):
    row_sum = 0
    for j in range(len(Prices[0])):
        row_sum += Prices[i][j] * Array2[j]
    Ans.append(row_sum) 
    
# Roxanne Niteka: Print the result with clear formatting
print("\nInput arrays:")
print("Prices:", Prices)
print("Array2:", Array2)
print("\nCalculations:")
print(f"Row 1: ({Prices[0][0]} × {Array2[0]}) + ({Prices[0][1]} × {Array2[1]}) = {Ans[0]}")
print(f"Row 2: ({Prices[1][0]} × {Array2[0]}) + ({Prices[1][1]} × {Array2[1]}) = {Ans[1]}")
print("\nFinal result:")
print(Ans)
