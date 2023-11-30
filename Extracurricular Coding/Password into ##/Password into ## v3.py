def maskify(cc):
    return "#"*(len(cc)-4) + cc[-4:]
run = maskify ('Your password is here')
print (run)