month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def date (j):
    f = j.strip().split('.')
    m = month[int(f[1])-1]
    d = f[0]
    y = f[2]
    return m + ' ' + d + ',' + " "  + y

data = input('Enter the date (dd.mm.yy.) ')
print (date(data))