def date_as_string (MONTH, DAY, YEAR):
    if MONTH == 1 :
        month = 'January'
    elif MONTH == 2 :
        month = 'February'
    elif M == 3 :
        month = 'March'
    elif MONTH == 4 :
        month = 'April'
    elif MONTH == 5 :
        month = 'May'
    elif MONTH == 6 :
        month = 'June'
    elif MONTH == 7 :
        month = 'July'
    elif MONTH == 8 :
        month = 'August'
    elif MONTH == 9 :
        month = 'September'
    elif MONTH == 10 :
        month = 'October'
    elif MONTH == 11 :
        month = 'November'
    elif MONTH == 12 :
        month = 'December'
    else:
        print ('The number of a month must be in range [1-12]')
    try:
       print (month, DAY,',', YEAR)
    except:
        print ('Please write the numbers')
M = int (input ('Write the number of the month '))
D = int (input ('Write the number of the day '))
Y = int (input ('Write the number of the year '))
date_as_string (M, D, Y)

        
        
    