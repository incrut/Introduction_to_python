def file_into_dict(filename):
    f = open (filename, encoding = 'UTF-8')
    cities = {}
    for line in f:
        splitted_line = line.split(' ')
        
        for i in range (1, len (splitted_line)):
            cities[splitted_line[i]] = splitted_line [0]
        
        for city in splitted_line[1:]:
            cities[city] = splitted_line[0]
            
    return cities

f_name = input('Enter a file name: ')

data = file_into_dict(f_name)

while True:

    city_name = input ('Enter the city: ')
    
    if city_name.lower() == 'done':
        break
    elif city_name in data.keys():
        print(city_name, 'is in', data[city_name])
    else:
        print('No information about the city')