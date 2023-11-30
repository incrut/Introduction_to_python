import random
from tkinter import *
from rich import print



HP = 0
money = 0
DMG = 0
HPlst = []
HPbattle = None
dragonslayer = {'dragons' : 0}



def printstate():
    print ('You have [green]{0} hp[/], [yellow]{1} coins[/] and your [red]damage equals {2}[/]'
           .format(HP, money, DMG))
 
 


def init_game(initHP, initMONEY, initDMG):
    global HP
    global money
    global DMG
    
    HP = initHP
    money = initMONEY
    DMG = initDMG
    
    hfile = open('Lore.txt')
    file = hfile.read()
    print (file)
    printstate()
    
    
    
    
def purchase(cost):
    global HP
    global money
    global DMG
        
        
    if money >= cost:
        money -= cost
        return True
    print ('You do not have enough [yellow]coins[/] for that. Come back later when you get more money!')
    return False
   
   
   
   
def tavern():
    global HP
    global money
    global DMG
    global HPlst
    
    shopquality = ('old', 'new', 'mythic')
    shops = (('iron sword', 'wooden hummer', 'shovel', 'dirk', 'cooking knife', 'giant axe'),('leather pants','cloth coat','plate armor','chainmail helmet','leather gloves','steel boots'))
    shoplvl = random.randint (1,3)
    shopqualities = shopquality [shoplvl - 1]
    shopefficiency = round(((random.randint (1,5) * shoplvl) + 1 ) / 1.5)
    shopcost = (random.randint (1,8) * shoplvl)
    if random.randint(1,4) == 1:
        shop = random.choice(shops[1])
        checking = True
    else:
        shop = random.choice(shops[0])
        checking = False
    
    armour = 5
    
    print ('You hear the sound of people laughing and singing songs. You went to watch what is the reason for those noises and saw a [blue]tavern[/].')
    printstate()
    
    while input ('Do you want to enter the tavern or do you want to ignore it? (enter/ignore) ').lower().strip() == 'enter':
        if HP <=10: print ('1) Improve your armour (increases your [green]HP by 1[/]) - [yellow]{} coins[/]'.format(armour))
        elif HP <= 13: print ('1) Improve your armour (increases your [green]HP by 2[/]) - [yellow]{} coins[/]'.format(armour))
        elif HP <= 15: print ('1) Improve your armour (increases your [green]HP by 3[/]) - [yellow]{} coins[/]'.format(armour))
        elif HP <= 20: print ('1) Improve your armour (increases your [green]HP by 4[/]) - [yellow]{} coins[/]'.format(armour))
        elif HP >= 20: print ('1) Improve your armour (increases your [green]HP by 5[/]) - [yellow]{} coins[/]'.format(armour))
        if checking: print ('2)', shopqualities, shop,'with [green]armour of {0}[/] for [yellow]{1} coins[/]'.format(shopefficiency, shopcost))
        else: print ('2)', shopqualities, shop,'with [red]damage of {0}[/] for [yellow]{1} coins[/]'.format(shopefficiency, shopcost))
        print ('3) Read the monster manuscript.')
        print ('4) Nevermind')
        
        try:
            choice = int (input ('Do you want to buy something (1/2), read the monster manuscript (3) or leave (4)? '))
            if choice == 1:
                if HP <=10:
                    if purchase(armour):
                        HP += 1
                        print ('You have [green]{} hp[/] now'.format(HP))
                elif HP <=13:
                    if purchase(armour):
                        HP += 2
                        print ('You have [green]{} hp[/] now'.format(HP))
                elif HP <=15:
                    if purchase(armour):
                        HP += 3
                        print ('You have [green]{} hp[/] now'.format(HP))
                elif HP <=20:
                    if purchase(armour):
                        HP += 4
                        print ('You have [green]{} hp[/] now'.format(HP))
                elif HP >=20:
                    if purchase(armour):
                        HP += 5
                        print ('You have [green]{} hp[/] now'.format(HP))
            elif choice == 2 and not checking:
                if purchase(shopcost):
                    
                    DMG = shopefficiency
                    print ('Your [red]damage is {}[/] now'.format(DMG))
            elif choice == 2 and checking:
                if purchase(shopcost):
                    if HPlst:
                        HP -= HPlst[0]
                    HP += shopefficiency
                    if HPlst:
                        HPlst[0] = shopefficiency
                    else: HPlst.append(shopefficiency)
                    print ('You have [green]{} hp[/] now'.format(HP))
                    
            elif choice == 3:
                afile = open('Monster script.txt')
                dfile = afile.read()
                print (dfile)
                afile.close()
            elif choice == 4:
                break
            else:
                print ("I don't sell such thing")
        except:
            print ('please enter only one number')
            continue
    print ('You continued your adventure')




def monster():
    global HP
    global money
    global DMG
    global dragonslayer
    global HPbattle
    
    monsterlvl = random.randint(1,3)
    monsters = ("Pig Bull", "Lizard archer", "Hedgefrog", "Purple Dragon")
    if HP < 25 or DMG < 10:
        monsterchance = random.randint (1,46)
    elif HP >= 25 and DMG >= 10:
        monsterchance = random.randint (1,50)
    if monsterchance >= 1 and monsterchance <= 20:
        monster = monsters [0]
    elif monsterchance >= 21 and monsterchance <= 35:
        monster = monsters [1]
    elif monsterchance >= 36 and monsterchance <= 45:
        monster = monsters [2]
    else:
        monster = monsters [3]
    if monster == "Pig Bull":
        monsterHP = monsterlvl
        monsterDMG = monsterlvl + 1
        print ('You have met a [red]Pig Bull[/]. It has [green]{0} hp[/] and it\'s [red]damage is {1}[/]'.format(monsterHP, monsterDMG))
        printstate()
        HPbattle = HP
        
        while monsterHP > 0:
            choice = input ('Do you want to fight it or to try run away (failure to escape leads to death, you\'d better think twice.)(fight/run) ').lower().strip()
        
            if choice == 'fight':
                monsterHP -= DMG
                print ('You hit a monster for [red]{0}[/] and it has [green]{1} hp[/] left'.format(DMG, monsterHP))
            elif choice == 'run':
                chance = random.randint (0, 100)
                if chance < 30:
                    print ('You managed to run away. Congratulations my fast legs friend :)')
                    break
                else:
                    print ('This Pig Bull was much faster than you. It thrown you high into the sky after you fell down and died.')
                    HP = 0
                    break
            else:
                print ('Please check the spelling of your answer ')
                continue
        
            if monsterHP > 0:
                HP -= monsterDMG
                print ('Monster [red]hit you for {0}[/] and you have [green]{1} hp[/] left'.format(monsterDMG, HP))
            
            if HP <= 0:
                break
        else:
            loot = random.randint (0,1) + monsterlvl
            money += loot
            HP = HPbattle
            print ('You have defeated this monster. After looting it you found [yellow]{} coins[/]'.format(loot))
            printstate()
        
        
    elif monster == "Lizard archer":
        monsterHP = monsterlvl
        monsterDMG = monsterlvl * 2 
        print ('You have met a [red]Lizard archer[/]. It has [green]{0} hp[/] and it\'s [red]damage is {1}[/]'.format(monsterHP, monsterDMG))
        printstate()
        HPbattle = HP
        
        while monsterHP > 0:
            choice = input ('Do you want to fight it or to try run away (failure to escape leads to death, you\'d better think twice.)(fight/run) ').lower().strip()
        
            if choice == 'fight':
                if monsterHP > 0:
                    HP -= monsterDMG
                    print ('Monster [red]hit you for {0}[/] and you have [green]{1} hp[/] left'.format(monsterDMG, HP))
                monsterHP -= DMG
                print ('You hit a monster for [red]{0}[/] and it has [green]{1} hp[/] left'.format(DMG, monsterHP))
            elif choice == 'run':
                chance = random.randint (0, 100)
                if chance < 70:
                    print ('You managed to run away. Congratulations, my fast legs friend :)')
                    break
                else:
                    print ('This Lizard archer sniped you while you were trying to run away.')
                    HP = 0
                    break
            else:
                print ('Please check the spelling of your answer ')
                continue
        


            
            if HP <= 0:
                break
        else:
            loot = random.randint (3,5) + monsterlvl
            money += loot
            HP = HPbattle 
            print ('You have defeated this monster. After looting it you found [yellow]{} coins[/]'.format(loot))
            printstate()
        
        
    elif monster == "Hedgefrog":
        monsterHP = (monsterlvl + 1) * 3
        monsterDMG = monsterlvl 
        print ('You have met a [red]Hedgefrog[/]. It has [green]{0} hp[/] and it\'s [red]damage is {1}[/]'.format(monsterHP, monsterDMG))
        printstate()
        HPbattle = HP
        
        while monsterHP > 0:
            choice = input ('Do you want to fight it or to try run away (failure to escape leads to death, you\'d better think twice.)(fight/run) ').lower().strip()
        
            if choice == 'fight':
                monsterHP -= DMG
                print ('You hit a monster for [red]{0}[/] and it has [green]{1} hp[/] left'.format(DMG, monsterHP))
            elif choice == 'run':
                chance = random.randint (0, 100)
                if chance < 97:
                    print ('You managed to run away. Congratulations, my fast legs friend :)')
                    break
                else:
                    print ('Unfortunately, you were unlucky enough to stumble over a stone. This Hedgefrog caught up with you and pierced you with its needles.')
                    HP = 0
                    break
            else:
                print ('Please check the spelling of your answer ')
                continue
        
            if monsterHP > 0:
                HP -= monsterDMG
                print ('Monster [red]hit you for {0}[/] and you have [green]{1} hp[/] left'.format(monsterDMG, HP))
            
            if HP <= 0:
                break
        else:
            loot = random.randint (5,10) + monsterlvl
            money += loot
            HP = HPbattle
            print ('You have defeated this monster. After looting it you found [yellow]{} coins[/]'.format(loot))
            printstate()
        
        
    elif monster == "Purple Dragon":
        monsterHP = monsterlvl * 10
        monsterDMG = monsterlvl * 10 
        print ('You have met a [red]Purple Dragon[/]. It is hard to call this meeting pleasant. The best option for you is to beg for mercy... \nIt has [green]{0} hp[/] and it\'s [red]damage is {1}[/]'.format(monsterHP, monsterDMG))
        printstate()
        HPbattle = HP
        
        while monsterHP > 0:
            choice = input ('Do you want to fight it or to try run away (failure to escape leads to death, you\'d better think twice.)(fight/run) ').lower().strip()
        
            if choice == 'fight':
                monsterHP -= DMG
                print ('You hit a monster for [red]{0}[/] and it has [green]{1} hp[/] left'.format(DMG, monsterHP))
            elif choice == 'run':
                chance = random.randint (0, 100)
                if chance < 3:
                    print ('It looks like god himself protects you from death. Somehow you managed to run away from this terrifying creature.')
                    break
                else:
                    print ('What happened was to be expected. The dragon caught up with you. He crushed you into a flat cake and then fried you into a crisp with his flame.')
                    HP = 0
                    break
            else:
                print ('Please check the spelling of your answer ')
                continue
        
            if monsterHP > 0:
                HP -= monsterDMG
                print ('Monster [red]hit you for {0}[/] and you have [green]{1} hp[/] left'.format(monsterDMG, HP))
            
            if HP <= 0:
                break
        else:
            HP = HPbattle
            chance = random.randint(1,4)
            if chance == 1:
                print ('''You have defeated this legendary monster and after looting it you found something very unusual. W...Wait is it a boot?...
Yes! It is [yellow]a legendary boot of jet kicks[/] with [red]damage of 25[/].''')
                DMG = 25
            else:
                loot = round((random.randint (10,13) * monsterlvl)*1.5)
                money += loot
                HP += round((random.randint (10,13) * monsterlvl)*1.5)
                print ('You have defeated this monster. After looting it you found [yellow]{} coins[/]'.format(loot))
            printstate()
            if monsterlvl == 3:
                dragonslayer['dragons'] += 1

 
 
 
def game_loop():
    situation = random.randint(0,5)
    
    if situation == 0:
        tavern()
    elif situation == 2:
        monster()
    else:
        input ('You are strolling in the woods. Everything is quiet and only sometimes you hear the sound of wild animals.')




init_game(10,5,1)




while True:
    if HP <= 0:
        answer = input('Unfortunately you could not survive. Do you want to restart the game? (yes/no) ').lower().strip()
        if answer == 'yes':
            init_game(10,5,1)
        elif answer == 'no':
            break
        else:
            print ('Please check the spelling of your input. It seems to be incorrect.')
            continue
    elif dragonslayer['dragons'] == 3:
        print ('You have slain [red]3 elder dragons[/] and [yellow]officially completed[/] this game. [yellow]My congratulations![/] Do you want to start a new game? (yes/no)', end=' ')
        answer = input().lower().strip()
        if answer == 'yes':
            init_game(10,5,1)
        elif answer == 'no':
            break
        else:
            print ('Please check the spelling of your input. It seems to be incorrect.')
            continue
    char_name = ''        
    game_loop()
       
       