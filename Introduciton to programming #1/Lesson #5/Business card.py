fname = input ('Please enter your first name ')
lname = input ('Please enter your last name ')
mail = input ('Please enter your e-mail adress ')
occupation = input ('Please enter your occupation ')
fname = fname.capitalize()
lname = lname.capitalize()
occupation = occupation.capitalize()
namail = fname + ' ' + lname + ' ' + '-' + ' ' + mail
size = max(len(namail), len(occupation)) + 12
print ('+'+'-'*size +'+')
print ('|'+' '*size +'|')
print ('|', namail.center(size - 2), '|')
print ('|'+' '*size +'|')
print ('|',  occupation.center(size -2), '|')
print ('|'+' '*size +'|')
print ('+'+'-'*size+'+')