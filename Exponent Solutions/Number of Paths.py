"""
https://www.tryexponent.com/practice/prepare/number-of-paths

Algorithm:
1. Create an n x n matrix filled with 0s
2. Set the square below the destination to a 1
3. Traverse right to left, top to bottom from the 1, adding the values of the cells above and to the right
    a. If there is no right cell, use a 0
    b. If the cell is on the diagonal or to the left, skip it
4. Return the value at matrix[0][0]

TC: O(n^2)
SC: O(n^2)
"""

def num_of_paths_to_dest(n: int) -> int:
    n += 1
    matrix = [[0] * n for _ in range(n)]
    matrix[0][-1] = 1
    n -= 1

    for r in range(1, n+1):
        for c in range(n, -1, -1):
            if c == n - r:  # We crossed the diagonal
                continue
            if c == n:  # We are on the rightmost column
                right = 0
            else:
                right = matrix[r][c+1]
            
            matrix[r][c] = matrix[r-1][c] + right  # up + right

    # print(str(matrix).replace('], ','],\n '))
    return matrix[-1][1]

# Test case
num_of_paths_to_dest(3)

'''
n = 3

[[0, 0, 0, 0],
 [0, 0, 0, 1],
 [0, 0, 1, 1],
 [0, 2, 2, 1]]

Answer is 2.
'''
