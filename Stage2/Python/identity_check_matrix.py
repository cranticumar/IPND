# Problem Statement 3: Check if a matrix is a identity matrix
def matrix_check(matrix):
    if not isinstance(matrix, list):
        raise Exception("matrix is not a list")
    else:
        for row in matrix:
            if not isinstance(row, list):
                raise Exception("one of the row is not a list")

def square_check(matrix):
    matrix_check(matrix)
    for row in matrix:
        if len(row) != len(matrix):
            return False
    return len(matrix)

def identity_check(matrix):
    order = square_check(matrix)
    if order:
        for row in range(order):
            for column in range(order):
                if row == column:
                    if matrix[row][column] != 1:
                        return False
                else:
                    if matrix[row][column] != 0:
                        return False
    else:
        return False
    return True

# print identity_check(
#   [[1,0,0],
#   [0,1,0],
#   [0,0,1],
#   [0,0,0]])
# print identity_check([[1,0],0,1])