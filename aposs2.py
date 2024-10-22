import math
import numpy as np

def is_perfect_square(n):
    return math.isqrt(n) ** 2 == n

def nearest_square(n):
    root = math.isqrt(n)
    if root ** 2 == n:
        return n
    else:
        return (root + 1) ** 2

def create_square_matrix(n):

    n = nearest_square(n)

    matrix_size = int(math.isqrt(n))
   
    matrix = np.arange(1, n + 1).reshape(matrix_size, matrix_size)
    
    return matrix

N = int(input("Введіть число N: "))
matrix = create_square_matrix(N)

print("Квадратна матриця:")
print(matrix)
