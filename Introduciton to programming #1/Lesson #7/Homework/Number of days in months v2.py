def days (number):
    mname = ['31', '28', '31', '30', '31', '30', '31', '31', '30', '31', '30', '31']
    return mname [number]
hfile = input('Enter the name of the file ')
try:
    file = open (hfile)
except:
    print ('Something went wrong, check the spelling of the entered file')
    quit()
for j in file:
    sentence = j.strip()
    word = sentence.split('.')
    nber = (int (word[1])) - 1
    print ('Month', nber+1, 'has', days(nber) , 'days in it')