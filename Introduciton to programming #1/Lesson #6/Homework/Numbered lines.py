count = 0
fname = input ('Please enter the name of the file: ')
try:
    file = open(fname)
except:
    print ('The file seems to be missing :(')
    quit()
for name in file:
    count += 1
    scount = str(count)
    print (scount + '.', name.strip())