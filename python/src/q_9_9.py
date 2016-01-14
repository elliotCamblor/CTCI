def placeQueens(size):
    results = []
    __placeQueens(size, 0, [-1]*size, results)
    return results

def __placeQueens(size, row, columns, results):
    if row == size:
        results.append(columns.copy())

    for col in range(size):
        if isValid(columns, row, col):
            columns[row] = col
            __placeQueens(size, row + 1, columns, results)

def isValid(columns, row, col):
    for i in range(row):
        if columns[i] == col:
            return False
        elif row - i == abs(col - columns[i]):
            return False

    return True
