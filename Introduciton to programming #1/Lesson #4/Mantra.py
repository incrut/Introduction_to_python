mantra = input ('Enter your mantra: ')
try:
    repetition = int (input ('How many times to repeat: '))
    while repetition > 0:
        print (mantra)
        repetition = repetition - 1
except:
    print ('Not a number')