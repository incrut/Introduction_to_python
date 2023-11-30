import random



HP = 0
money = 0
DMG = 0



def printstate():
    print ('You have', HP, 'hp', money, 'coins and your damage equals', DMG)
 
 


def init_game(initHP, initMONEY, initDMG):
    global HP
    global money
    global DMG
    
    HP = initHP
    money = initMONEY
    DMG = initDMG
    
    hfile = open('Lore.txt')
    file = hfile.read()
    print (file,'You have', HP, 'hp', money, 'coins and your damage equals', DMG)
    hfile.close()
   
   
   
   
def tavern():
    global HP
    global money
    global DMG
    
    afile = open('Monster script.txt')
    dfile = afile.read()
    
    def purchase(cost):
        global HP
        global money
        global DMG
        
        
        if money >= cost:
            money -= cost
            return True
        print ('You do not have enough coins for that. Come back later when you get more money!')
        return False
    
    weaponquality = ['old', 'new', 'mythic']
    weapons = ['iron sword', 'wooden hummer', 'shovel', 'dirk', 'cooking knife', 'giant axe']
    weapond = random.randint (1,3)
    weaponqualities = weaponquality [weapond - 1]
    weaponDMG = round(((random.randint (1,5) * weapond) + 1 ) / 1.5)
    weaponcost = (random.randint (1,8) * weapond)
    weapon = random.choice(weapons)
    
    armour = 5
    
    print ('You hear the sound of people laughing and singing songs. You went to watch what is the reason for those noises and saw a tavern.')
    printstate()
    
    while input ('Do you want to enter the tavern or do you want to ignore it? (enter/ignore) ').lower().strip() == 'enter':
        print ('1) Improve your armour (increases your HP by 1) -', armour, 'coins')
        print ('2)', weaponqualities, weapon,'with damage of', weaponDMG, 'for', weaponcost, 'coins')
        print ('3) Read the monster manuscript.')
        print ('4) Nevermind')
        
        try:
            choice = int (input ('Do you want to buy something (1/2), read the monster manuscript (3) or leave (4)? '))
            if choice == 1:
                if purchase(armour):
                    HP += 1
                    print ('You have', HP, 'hp now')
            elif choice == 2:
                if purchase(weaponcost):
                    DMG = weaponDMG
                    print ('Your damage is', DMG, 'now')
            elif choice == 3:
                print (dfile)
            elif choice == 4:
                break
            else:
                print ("I don't sell such thing")
        except:
            print ('please enter only one number')
            continue
    afile.close()
    print ('You continued your adventure')




def monster():
    global HP
    global money
    
    
    monsterlvl = random.randint(1,3)
    monsters = ["Pig Bull", "Lizard archer", "Hedgefrog", "Purple Dragon"]
    monsterchance = random.randint (1,46)
    if monsterchance >= 1 and monsterchance <= 20:
        monster = monsters [0]
    elif monsterchance >= 21 and monsterchance <= 35:
        monster = monsters [1]
    elif monsterchance >= 36 and monsterchance <= 45:
        monster = monsters [2]
    elif monsterchance == 46:
        monster = monsters [3]
    if monster == "Pig Bull":
        monsterHP = monsterlvl
        monsterDMG = monsterlvl + 1
        print ('You have met a Pig Bull. It has', monsterHP, 'hp and it\'s damage is', monsterDMG)
        
        while monsterHP > 0:
            choice = input ('Do you want to fight it or to to try run away (failure to escape leads to death, you\'d better think twice.)(fight/run) ').lower().strip()
        
            if choice == 'fight':
                monsterHP -= DMG
                print ('You hit a monster for', DMG, 'and it has', monsterHP, 'hp left')
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
                print ('Monster hit you for', monsterDMG, 'and you have', HP, 'hp left')
            
            if HP <= 0:
                break
        else:
            loot = random.randint (0,1) + monsterlvl
            money += loot
            HP += monsterlvl
            print ('You have defeated this monster. After looting it you found ', loot, 'coins')
        
        
    elif monster == "Lizard archer":
        monsterHP = monsterlvl
        monsterDMG = monsterlvl * 2 
        print ('You have met a Lizard archer. It has', monsterHP, 'hp and it\'s damage is', monsterDMG)
        
        while monsterHP > 0:
            choice = input ('Do you want to fight it or to to try run away (failure to escape leads to death, you\'d better think twice.)(fight/run) ').lower().strip()
        
            if choice == 'fight':
                if monsterHP > 0:
                    HP -= monsterDMG
                    print ('Monster hit you for', monsterDMG, 'and you have', HP, 'hp left')
                monsterHP -= DMG
                print ('You hit a monster for', DMG, 'and it has', monsterHP, 'hp left')
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
            HP += monsterlvl + 1
            print ('You have defeated this monster. After looting it you found ', loot, 'coins')
            print ('Now you have', money, 'coins')
        
        
    elif monster == "Hedgefrog":
        monsterHP = (monsterlvl + 1) * 3
        monsterDMG = monsterlvl 
        print ('You have met a Hedgefrog. It has', monsterHP, 'hp and it\'s damage is', monsterDMG)
        
        while monsterHP > 0:
            choice = input ('Do you want to fight it or to to try run away (failure to escape leads to death, you\'d better think twice.)(fight/run) ').lower().strip()
        
            if choice == 'fight':
                monsterHP -= DMG
                print ('You hit a monster for', DMG, 'and it has', monsterHP, 'hp left')
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
                print ('Monster hit you for', monsterDMG, 'and you have', HP, 'hp left')
            
            if HP <= 0:
                break
        else:
            loot = random.randint (5,10) + monsterlvl
            money += loot
            HP += monsterlvl*2
            print ('You have defeated this monster. After looting it you found ', loot, 'coins')
            print ('Now you have', money, 'coins')
        
        
    elif monster == "Purple Dragon":
        monsterHP = monsterlvl * 10
        monsterDMG = monsterlvl * 10 
        print ('You have met a Purple Dragon. It is hard to call this meeting pleasant. The best option for you is to beg for mercy... \nIt has', monsterHP, 'hp and it\'s damage is', monsterDMG)
        
        while monsterHP > 0:
            choice = input ('Do you want to fight it or to to try run away (failure to escape leads to death, you\'d better think twice.)(fight/run) ').lower().strip()
        
            if choice == 'fight':
                monsterHP -= DMG
                print ('You hit a monster for', DMG, 'and it has', monsterHP, 'hp left')
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
                print ('Monster hit you for', monsterDMG, 'and you have', HP, 'hp left')
            
            if HP <= 0:
                break
        else:
            loot = random.randint (10,13) * monsterlvl
            money += loot
            HP += 10
            print ('You have defeated this monster. After looting it you found ', loot, 'coins')
            print ('Now you have', money, 'coins')

 
 
 
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
            
    game_loop()
       
       