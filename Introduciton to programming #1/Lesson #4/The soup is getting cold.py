tsoup = 90
troom = 20
while tsoup > troom:
    tsoup = round tsoup - (tsoup*0.19)
    if tsoup > troom:
        print ('1 min. Soup temperature:' , tsoup)