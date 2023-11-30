name = input ("Enter your last name ")
sex = input ("Are you male or female (m/f)? ") #s/m
status = input ("Are you single or married (s/m)? ") #s/m
if (sex == 'm') :
    print ('Nice to have you here, Mr', name)
if (sex == 'f') :
    if (status == 's') :
      print ('Nice to have you here, Miss', name)
      else:
          print ('Nice to have you here, Mrs', name)