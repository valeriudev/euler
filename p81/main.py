# https://projecteuler.net/problem=81
import os

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the absolute path to the matrix file
matrix_file_path = os.path.join(script_dir, '0081_matrix.txt')

matrix = []

with open(matrix_file_path, 'r') as file:
    for line in file:
        matrix.append(list(map(int, line.strip().split(','))))

cols = len(matrix[0])
rows = len(matrix)

dp = [[0] * cols for _ in range(rows)]
dp[0][0] = matrix[0][0]

# Fill first row (can only move right)
for j in range(1, cols):
    dp[0][j] = dp[0][j-1] + matrix[0][j]

# Fill first column (can only move down)
for i in range(1, rows):
    dp[i][0] = dp[i-1][0] + matrix[i][0]

for i in range (1, rows):
    for j in range (1, cols):
        dp[i][j] = matrix[i][j] + min(dp[i-1][j], dp[i][j-1])


print(dp[79][79])