def month_name (number):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    return months[number - 1]

hfile = input ('Enter the name of the file ')

try:
    file = open (hfile, 'r')
    
except:
    print ('There is no such file ')
    
else:
    bdays = {}
    
    for i in file:
        i = i.split('.')
        bdays[month_name(int(i[1]))] = bdays.get(month_name(int(i[1])), 0) + 1
        
    print (bdays)
    file.close()
    
    lst = [(v, k) for (k, v) in bdays.items()]
    lst.sort(reverse = True)
    for v,k in lst[:5]:
        print (k, v)