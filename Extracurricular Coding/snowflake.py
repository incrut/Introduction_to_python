n = int (input ('Please enter an odd number '))
if n % 2 == 0:
    print ('This is an even number')
else:
    lst = [['.'] * n for i in range (n)]

    for i in range(n):
        lst[n//2][i] = '*'
        lst [i][n//2] = '*'
        lst[i][i] = '*'
        lst[i][n - 1 - i] = '*'
        
    for i in lst:
        for j in i:
            print (j, end = ' ')
        print ('\n')