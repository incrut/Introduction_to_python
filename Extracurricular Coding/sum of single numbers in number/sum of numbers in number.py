def summa (x):
    sul = 0
    if len(str(x)) != 1:
        for i in str(x):
            sul += int(i)
        x = sul
        return summa (x)
        
    else:
        return (x)


print (summa (input()))