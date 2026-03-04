"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Example 1:

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]


Constraints:

    m == matrix.length
    n == matrix[0].length
    1 <= m, n <= 200
    -231 <= matrix[i][j] <= 231 - 1

Follow up:
    A straightforward solution using O(mn) space is probably a bad idea.
    A simple improvement uses O(m + n) space, but still not the best solution.
    Could you devise a constant space solution?
"""


def solution(matrix: list[list[int]]):
    """
    Key assumption would be - once in a given column/row 0 was found - it doesn't
    interest us anymore - it will all become 0s anyway.

    As we go through the matrix - it would be beneficial to have ability to look
    up current row/column to ensure that it wasn't yet flagged as zeroed.

    I think we can safely assume those to be first cells - for both row and column.
      c  0 1 2
    r
    0    1 1 1
    1    1 0 1
    2    1 1 1


    So in this case - we'd flag row 1 and column 1. And as we traverse - if we
    lookup i,j (row and column) and in case this row is flagged? we increment the row
    in case column is flagged we increment the column - nothing for us there.

    After we end the traversal - we can basically iterate over - just rows and columns
    and flip the values
    """
    columns = set()
    rows = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                columns.add(j)
                rows.add(i)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i in rows or j in columns:
                matrix[i][j] = 0

    return matrix


def solution_constant(matrix: list[list[int]]):
    zero_row = False
    zero_column = False
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                if i == 0:
                    zero_row = True
                if j == 0:
                    zero_column = True

                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[i])):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    if zero_row:
        for j in range(len(matrix[0])):
            matrix[0][j] = 0

    if zero_column:
        for i in range(len(matrix)):
            matrix[i][0] = 0

    return matrix


def print_solution(matrix: list[list[int]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="")
        print("\n", end="")


if __name__ == "__main__":
    matrixA = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    matrixB = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    matrixC = [[1, 2], [0, 1]]

    print_solution(solution_constant(matrixA))
    print_solution(solution_constant(matrixB))
    print_solution(solution_constant(matrixC))
