try:
    hfile = open('cents.txt')
    
    
except:
    print ('Something went wrong')
    quit()
    
    
file = hfile.read()
cents = file.split()
n = []

for j in range(len(cents)):
    n.append(int(cents[j]))
    

def eurocents(ec):
    sumcent = 0
    for i in ec:
        if i in [1, 2, 5, 10, 20, 50]:
            sumcent += i
    return sumcent


def unkeurocents(ec):
    sumun = 0
    for i in ec:
        if i not in [1, 2, 5, 10, 20, 50]:
            sumun += i
    return sumun


def redeurocents(ec):
    sumred = 0
    for i in ec:
        if i in [1, 2, 5]:
            sumred += i
    return sumred

def red_coin (urk):
    red_coins = [1, 2, 5]
    smallest_euro_cent = 100
    for coin in urk:
        if (coin in red_coins) and (coin < smallest_euro_cent):
            smallest_euro_cent = coin
    if smallest_euro_cent == 100:
        return ('No red coins')
    return smallest_euro_cent


print (eurocents(n))
print (unkeurocents(n))
print (redeurocents(n))
print (red_coin(n))
hfile.close()

        
