count = 0
number = 0
url = input ('Enter URL please: ')
namebeg = url.find('~')
while number < len(url):
    letter = url[number]
    if letter == '/':
        count += 1
    if count == 4:
        break
    number += 1
name = url[namebeg + 1 : number]
print ('Username is' , name)