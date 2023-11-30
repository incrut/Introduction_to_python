hfile = input ('Enter the name of a file ')
try:
    file = open (hfile)
except:
    print ('Something went wrong, check the spelling of the entered file')
    quit()
listic = list()
for j in file:
    j = j.strip()
    f = j.split('.')
    listic.append(f)
print (listic)
i = 0
while i < len(listic):
    if listic [i][1] == '01' or listic[i][1] == '03' or listic[i][1] == '05' or listic[i][1] == '07' or listic[i][1] == '08' or listic[i][1] == '10' or listic[i][1] == '12':
        print ('Month', listic[i][1], 'has 31 days in it')
    elif listic [i][1] == '04' or listic[i][1] == '06' or listic[i][1] == '09' or listic[i][1] == '11':
        print ('Month', listic[i][1], 'has 30 days in it')
    elif listic [i][1] == '02':
        print ('Month', listic [i][1], 'has 28 days in it')
    i+= 1