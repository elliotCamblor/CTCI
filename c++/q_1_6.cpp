#include <iostream>

using namespace std;

void rotateClockwise(int **matrix, int offset, int size) {
    if (size - 2*offset <= 1)
        return;

    for (int i = offset; i < size-1-offset; i++) {
        int temp = matrix[offset][i+offset];
        matrix[offset][i+offset] = matrix[size-1-offset-i][offset];
        matrix[size-1-offset-i][offset] = matrix[size-1-offset][size-1-offset-i];
        matrix[size-1-offset][size-1-offset-i] = matrix[i+offset][size-1-offset];
        matrix[i+offset][size-1-offset]=temp;
    }

    rotateClockwise(matrix, offset + 1, size);
}

void printMatrix(int **matrix, int size) {
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            cout<<matrix[i][j] <<"\t";
        }
        cout<<"\n";
    }
}

int main() {
    int **testMatrix = new int*[5];
    for(int i = 0; i < 10; i++)
        testMatrix[i] = new int[5];
    
    int num = 0;
    for(int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            testMatrix[i][j] = num++;
        }
    }

    printMatrix(testMatrix, 5);
    cout<<"\n\n\n";
    rotateClockwise(testMatrix, 0, 5);
    printMatrix(testMatrix, 5);
}
