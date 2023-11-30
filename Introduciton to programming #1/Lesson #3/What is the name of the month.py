def month_as_name (DATE):
    current_month = DATE
    return current_month
try :
    date = int (input ('Write the number of the month '))
    month = month_as_name (date)
    if month == 1 :
        print ('The 1st month of the year is January')
    elif month == 2 :
        print ('The 2nd month of the year is February')
    elif month == 3 :
        print ('The 3rd month of the year is March')
    elif month == 4 :
        print ('The 4th month of the year is April')
    elif month == 5 :
        print ('The 5th month of the year is May')
    elif month == 6 :
        print ('The 6th month of the year is June')
    elif month == 7 :
        print ('The 7th month of the year is July')
    elif month == 8 :
        print ('The 8th month of the year is August')
    elif month == 9 :
        print ('The 9th month of the year is September')
    elif month == 10 :
        print ('The 10th month of the year is October')
    elif month == 11 :
        print ('The 11th month of the year is November')
    elif month == 12 :
        print ('The 12th month of the year is December')
    else :
        print ('The number must be in range [1-12]')
except :
    print ('please write a number')