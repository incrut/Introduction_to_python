money = input ('Please enter the amount of cents you obtain ')
try:
    money = int(money)
except:
    print ('Not a number')
euro = money // 100
cent = money % 100
