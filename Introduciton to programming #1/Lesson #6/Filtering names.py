file = open('C:/Users/Nikita/Desktop/Tartu university/Programming/Programs/Lesson #6/names.txt' , 'r')
count = 0
surname = input ('Enter the name of the family ')
for j in file:
    if surname.lower() in j.lower():
        count += 1
        print (str(count) + '.', j.strip())
    else:
        continue