try:
    n = int(input('Enter odd numbers: '))
    
except:
    print ('Please enter only numbers')

else:
    if n % 2 == 1 and n >= 5:

        matrix = []

        for i in range (n):
            row = []
            for j in range (n):
                row.append('.')
            matrix.append(row)

# 5 x 5
# 0, 1, 2, 3, 4 - row
# 5 // 2 -> n // 2 -middle row
# 5 // 2 -> n // 2 -middle column
# 0 0, 1 1, 2 2, 3 3, 4 4 - first diagonal
# 0 4, 1 3, 2 2, 1 3, 4 0 - second diagonal
# 0 + 4 = 4, 1 + 3 = 4, 2 + 2 = 4, 1 + 3= 4, 4 + 0 = 4, n - 1

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if n // 2 == i or n // 2 == j or i == j or i + j == n - 1:
                    matrix[i][j] = '*'
    
            for i in range(len(matrix)):
                row_string = ''
                for j in range(len(matrix)):
                    row_string += matrix[i][j] + ' '
                print (row_string)
    else:
        print ('We need odd number')

        