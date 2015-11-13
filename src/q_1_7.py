def modify(matrix):
    bannedRows = set()
    bannedCols = set()

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                bannedRows.add(i)
                bannedCols.add(j)

    for i in bannedRows:
        for j in range(len(matrix[0])):
            matrix[i][j] = 0

    for j in bannedCols:
        for i in range(len(matrix)):
            matrix[i][j] = 0

def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            
            endC = '\t'
            if j == len(matrix[0])-1:
                endC = '\n'

            print(matrix[i][j], end=endC)
     
if __name__ == "__main__":
    testMatrix = [
        [1, 2, 0, 8],
        [5, 3, 6, 2],
        [3, 4, 5, 3],
        [4, 7, 3, 8]
        ]

    printMatrix(testMatrix)
    print()
    modify(testMatrix)
    printMatrix(testMatrix)
