file = open('C:/Users/Nikita/Desktop/Tartu university/Programming/Programs/Lesson #6/numbers.txt', 'r')
for j in file:
    if int(j.strip()) % 2 == 0:
        print (j.strip(), 'Number is even ')
    elif int(j.strip()) % 2 != 0:
        print (j.strip(), 'Number is odd')