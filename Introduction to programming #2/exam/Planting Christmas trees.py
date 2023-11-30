def into_dictionary(file_name):
    try:
        file = open (file_name, encoding = 'UTF-8')
    except:
        print ('This file does not exist please check the spelling')
    else:
        countries = dict()
        for line in file:
            line = line.strip()
            splitted_line = line.split(';')
            countries[splitted_line[0]]  = float(splitted_line[1])
        return countries


file_n = input ('Please enter a file name ')
limit = float(input('Enter the threshold of the reforestation: '))

for k,v in into_dictionary(file_n).items():
    if v >= limit:
        print (k, 'reforestation of spruce: ', v)