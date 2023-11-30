try:
    hfile = open ('Hall.txt')
    
except:
    print ('File does not exist')

else:
    lst = []

    for i in hfile:
        parts = i.split()
        inlst = []
        
        for j in parts:
            inlst.append(int(j))
        lst.append (inlst)
        
  #  print (list(range(len(lst))))
    
    for i in range(len(lst)):
        for j in range (len(lst[i])):
            if lst[i][j] % 2 == 0:
                print (lst[i][j] ,'An even appartment')
            else:
                print (lst[i][j] ,'An odd appartment')
        