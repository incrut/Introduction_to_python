oddsumm = 0
evensumm = 0
summ = 0
file = open ('C:/Users/Nikita/Desktop/Tartu university/Programming/Programs/Lesson #6/numbers.txt', 'r')
for j in file:
    j = int(j.strip())
    summ += j
    if j % 2 == 0:
        evensumm += j
    elif j % 2 != 0:
        oddsumm += j
print ('The summ of even numbers is ', evensumm)
print ('The summ of odd numbers is ', oddsumm)
print ('The summ of all numbers is ', summ)