#import

#function
def dictionary_from_file (filename):
    file = open (filename, encoding = 'UTF-8')
    
    country_codes = {} 
    
    for line in file:
        splitted_line = line.split(' ') #split()
        country_codes [splitted_line[0]] =splitted_line[1].strip()
        
    return country_codes

def codes_to_name(codes, countries):
    lst = []
    for code in codes:
        lst.append(countries.get(code, 'Unknown'))
    return lst

        
# Main program
user_file = input('Enter the file name: ')
user_codes = input ('Enter the country codes: ')

splitted_codes = user_codes.split()

country_names = dictionary_from_file(user_file)

list_names = codes_to_name(splitted_codes, country_names)

print (list_names)