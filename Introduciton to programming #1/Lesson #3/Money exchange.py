def money_change (GBP):
    eu = round ((1.09 * GBP), 2)
    return eu
grb = float (input ('Enter the amount of English pounds '))
money = money_change (grb)
print ('This is', money, 'Euros')
print (grb, 'GRB is', money, 'Euros')