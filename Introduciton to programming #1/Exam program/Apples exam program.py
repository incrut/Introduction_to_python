summa = 0   # sum of all juice made

def juice (apw):    #apples weight in kg
    return (float(apw) * 0.5)


try:
    file = input ('Enter the name of the file ')
    gfile = open (file)
except:
    print ('File does not exist')

else:
    mfile = gfile.read()
    apples = mfile.split()
    applelist = []
    
    for i in apples:
        applelist.append(i)
    print ('The following data was read from the file:', applelist)
    
    for j in applelist:
        if juice(j) // 50 == 0:
            print ('We got', juice(j) ,'litres of apple juice and could not donate any juice.')
        elif juice(j) // 50 != 0:
            remain = round((juice(j) - 50), 2)
            print ('We got', juice(j), 'litres of apple juice and kept', remain, 'litres of juice.')
        
        summa += round(juice(j), 2)
    print ('The Family made a total of', summa)