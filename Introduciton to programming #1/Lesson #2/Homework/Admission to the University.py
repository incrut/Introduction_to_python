try:
    points = int (input ('Write the number of points you obtain '))
    if points < 0 :
        print ('You cannot obtain negative points')
    elif points < 66 :
        print ('The obtained points are not enough to be considered for admission')
    elif points <= 100 :
        print ('The obtained points are enough to be consedered for admissions')
    elif points > 100 :
        print ('The number of points cannot be more than 100 ponits')
except:
    print ('Not a number')