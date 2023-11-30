filename = input ('Please enter a name of the file ')
try:
    file = open(filename, encoding = 'UTF-8')
except:
    print ('This file does not exist please check the spelling')
else:
    lst = []
    for line in file:
        splitted_line = line.split()
        lst.append(splitted_line)
    student_name = input('Please enter the student\'s name ').capitalize()
    column = None
    for rows in lst:
        try:
            column = rows.index(student_name)
            row = lst.index(rows)
            print (student_name, 'sits in row №',  row + 1, 'and column №', column + 1)
        except:
            pass