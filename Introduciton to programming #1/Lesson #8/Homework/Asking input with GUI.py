from easygui import *


def days (number):
    mname = ['31', '28', '31', '30', '31', '30', '31', '31', '30', '31', '30', '31']
    return mname [number]

def mm(j):
    acg = ['January', 'February', 'March', 'April', 'May', 'July', 'June', 'August', 'September', 'October', 'November', 'December']
    return acg [j]

name = enterbox ('Enter your name')
month = integerbox ('Enter the month of your birth')

msgbox ('You are' + ' ' + str(name) + ' ' +'You were born in' + ' ' + str(mm(month - 1)) + ' ' +'which has' + ' ' + str(days(month - 1)) + ' ' + 'in it')