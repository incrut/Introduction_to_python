try:
    month = int (input ('Write the number of the month '))
    if month == 1 :
        print ('That month has 31 days in it')
    elif month == 2 :
        print ('That month has 28 days in it')
    elif month == 3 :
        print ('That month has 31 days in it')
    elif month == 4 :
        print ('That month has 30 days in it')
    elif month == 5 :
        print ('That month has 31 days in it')
    elif month == 6 :
        print ('That month has 30 days in it')
    elif month == 7 :
        print ('That month has 31 days in it')
    elif month == 8 :
        print ('That month has 31 days in it')
    elif month == 9 :
        print ('That month has 30 days in it')
    elif month == 10 :
        print ('That month has 31 days in it')
    elif month == 11 :
        print ('That month has 30 days in it')
    elif month == 12 :
        print ('That month has 31 days in it')
    else:
        print ('The number of a month must be in range of [1-12]')
except:
    print ('Please enter a number')