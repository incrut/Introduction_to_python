def number_of_days (a):
    month = a
    if (year % 4 == 0) and (year % 100 != 0 ) or (year % 400 == 0):
        Y = 1
    else:
        Y = 0
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        print ('This month has 31 days in it')
    elif month == 4 or month == 6 or month == 9 or month == 11:
       print ('This month has 30 days in it')
    elif month == 2 and Y == 0:
        print ('This month has 28 days in it')
    elif month == 2 and Y == 1:
        print ('This month has 29 days in it')
    else:
        print ('The number of a month must be in range [1-12]')
while True:
    month = input ('Write the number of a month or Enter word "done" ')
    if month == 'done':
        break
    try:
        month = int (month)
        year = int (input ('Enter the current year '))
        number_of_days (month)
    except:
        print ('Please enter the number')