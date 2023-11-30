a = 1
try:
    P = int (input ('Enter a number of rows: '))
    while a <= P:
        print ('*' * a)
        a = a + 1
except:
    print ('Not a number')