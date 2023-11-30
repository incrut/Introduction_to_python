def budget(PP) :
    Money=PP*10+55
    return Money

inv = 0
att = 0
fname = input ('Please enter the name of the file: ')
try:
    file = open(fname)
except:
    print ('The file seems to be missing :(')
    quit()
for j in file:
    inv += 1 
    if '+' in j:
        att += 1
print ('The number of invited people: ', inv)
print ('The number of people attending: ', att)
print("Maximum budget is ",budget(inv),"EUROS")
print("Minimum budget is ",budget(att),"EUROS")