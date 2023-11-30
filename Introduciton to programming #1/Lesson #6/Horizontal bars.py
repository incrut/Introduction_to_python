file = open('C:/Users/Nikita/Desktop/Tartu university/Programming/Programs/Lesson #6/Horizontal bars.txt')
for j in file:
    j = int(j.strip())
    print ('*' * j)