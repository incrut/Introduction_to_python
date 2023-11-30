calories = 0

try:
    gfile = input ('Enter the name of the file ')
    file = open(gfile)
    
except:
    print ('File does not exist')
    
else:
    hfile = file.read()
    hfile = hfile.split('\n')
    lst = []
    
    for i in hfile:
        inlst = []
        i = i.split()
        
        for j in i:
            inlst.append(j)
        lst.append(i)
    
    print (lst)
    for g in range(len(lst)):
        for f in range(len(lst[g])):
            if f == 0 or f == 1:
                calories += int((lst[g][f]))*4
            elif f == 2:
                calories += int((lst[g][f]))*9
    
    print ('All meals together give %i calories'%(calories))
    
    
        