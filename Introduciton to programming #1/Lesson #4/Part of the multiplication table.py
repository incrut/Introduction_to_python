try:
    number = int (input ('Enter the number '))
    for times in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        product = number * times
        print (product)
except:
    print ('You must write the number')