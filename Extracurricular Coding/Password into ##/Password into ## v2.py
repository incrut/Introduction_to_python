# return masked string
def maskify(cc):
    numbers = len(cc)
    j = cc[0 : numbers - 4]
    if numbers > 4:
        newpass = cc.replace (j , '#'* (numbers - 4))
    elif numbers <= 4 and numbers >= 0:
        newpass = cc
    print (newpass)
    return (newpass)
maskify ('your password is here')