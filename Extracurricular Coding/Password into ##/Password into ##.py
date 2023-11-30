def maskify (cc):
    numbers = len(cc)
    j = cc[0 : numbers - 4]
    if numbers > 4:
        newpass = cc.replace (j , '#'* (numbers - 4))
    elif numbers <= 4 and numbers >= 2:
        j = cc[0 : numbers - 1]
        newpass = cc.replace (j , '#' * (numbers - 1))
    elif numbers == 1 or numbers == 0:
        newpass = cc
    print (newpass)
cm = input ('Write ')
maskify (cm)