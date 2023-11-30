url = input ('Enter URL please: ')
namebeg = url.find('~')
nameend = url.find('/', namebeg)
name = url[namebeg + 1 : nameend]
print ('Username is' , name)