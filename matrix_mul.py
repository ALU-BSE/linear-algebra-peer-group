# matrix_mul.py
import pandas as pd
import numpy as np

# Load data
data = pd.read_csv('path/to/data')

# Benitha Uwituze: Imput arrays
Prices = [[300, 500],         
          [1000, 120.85]]

Array2 = [200, 100]          

# Benitha Uwituze and Roxannne: Calculate the result
Ans = []

for i in range(len(Prices)):
    row_sum = 0
    for j in range(len(Prices[0])):
        row_sum += Prices[i][j] * Array2[j]
    Ans.append(row_sum)