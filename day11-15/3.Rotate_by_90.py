def rotate(matrix): 
    n = len(matrix)
    for i in range(n // 2 + n % 2):
        for j in range(n // 2):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][n - i - 1]
            matrix[j][n - i - 1] = matrix[n - 1 - i][n - j - 1]
            matrix[n - 1 - i][n - j - 1] = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = temp