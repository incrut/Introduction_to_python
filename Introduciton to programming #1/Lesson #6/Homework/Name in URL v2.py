def find_name (a):
    namebeg = a.find('~')
    nameend = a.find('/', namebeg)
    name = a [namebeg + 1 : nameend]
    print (name)
    return (name)
file = open('urls.txt')
for url in file:
    print (find_name(url))