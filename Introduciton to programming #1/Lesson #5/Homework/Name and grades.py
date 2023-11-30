countg = 0
counta = 0
countb = 0
name = input ('Enter your first name please: ')
grades = input ('Enter your grades please: ')
rightname = ((name.lower()).capitalize())
rightgrades = grades.upper()
for z in grades:
    countg += 1
for x in rightgrades:
    if x == 'A':
        counta += 1
for c in rightgrades:
    if c == 'B':
        countb += 1
countab = counta + countb
print ('Hello,', rightname, 'your grades are', rightgrades)
print ('You have', countg, 'grades')
print ('Your grade for second course is ', rightgrades [1])
print ("The number of A's and B's is ", countab)