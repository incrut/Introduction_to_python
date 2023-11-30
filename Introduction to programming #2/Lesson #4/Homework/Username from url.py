import re

fname = input ('Please enter a file name: ')

try:
    file = open(fname)
    
except:
    print ('File does not exist please enter a valid name')
    
else:
    print ('The user names are:')
    datepat = re.compile(r'/~\w+')
    for line in file:
        line = line.strip()
        if (datepat.findall(line)):
            for i in (datepat.findall(line)):
                print (i[2:])
            