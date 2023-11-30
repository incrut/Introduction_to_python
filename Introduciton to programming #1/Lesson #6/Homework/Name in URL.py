number = 0
count = 0
def find_name (a):
    namebeg = a.find('~')
    while number < len(a):
        letter = a[number]
        if letter == '/':
            count += 1
        if count == 4:
            break
        number += 1
    name = a [namebeg+1 : number]
    return (name)
file = open('urls.txt')
try:
    for url in file:
        print (find_name (url))
except:
    print (':(')