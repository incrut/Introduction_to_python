from random import *
from tkinter import *
from rich import print
from tkinter import messagebox



HP = 0
money = 0
DMG = 0
HPlst = []
HPbattle = None
window_stroll = None
window_shop = None
window_fight = None
window_tavern = None
checking = None
shopcost = None
shopefficiency = None
monsterHP = None
monsterDMG = None
monsterlvl = None
loot = None



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
    
def on_closing_stroll():
    global window_stroll
    if messagebox.askokcancel('quit', 'Are you sure that you want to quit game?'):
        window_stroll.destroy()
        exit()

def on_closing_tavern():
    global window_tavern
    if messagebox.askokcancel('quit', 'Are you sure that you want to quit game?'):
        window_tavern.destroy()
        exit()
        
def on_closing_shop():
    global window_shop
    if messagebox.askokcancel('quit', 'Are you sure that you want to quit game?'):
        window_shop.destroy()
        exit()
        
def on_closing_fight():
    global window_fight
    if messagebox.askokcancel('quit', 'Are you sure that you want to quit game?'):
        window_fight.destroy()
        exit()
        
def on_closing_death():
    if messagebox.askokcancel('quit', 'Are you sure that you want to quit game?'):
        window_death.destroy()
        exit()
        
def button_walking_next():
    global window_stroll
    window_stroll.destroy()
    
def button_shop0():
    global HP
    global DMG
    armour = 5
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
    elif HP <20:
        if purchase(armour):
            HP += 4
            print ('You have [green]{} hp[/] now'.format(HP))
    elif HP >=20:
        if purchase(armour):
            HP += 5
            print ('You have [green]{} hp[/] now'.format(HP))

def button_shop1():
    global checking
    global shopefficiency
    global shopcost
    global HP
    global DMG
    
    if not checking:
        if purchase(shopcost):
                    
            DMG = shopefficiency
            print ('Your [red]damage is {}[/] now'.format(DMG))
    elif checking:
        if purchase(shopcost):
            if HPlst:
                HP -= HPlst[0]
            HP += shopefficiency
            if HPlst:
                HPlst[0] = shopefficiency
            else: HPlst.append(shopefficiency)
            print ('You have [green]{} hp[/] now'.format(HP))
    
def button_shop2():
    try:
        afile = open('Monster script.txt')
        dfile = afile.read()
        print (dfile)
        afile.close()
    except:
        print ('The file does not exist.')
        
def button_tavern0():
    global window_tavern
    global checking
    global shopefficiency
    global shopcost
    global window_shop
    shopquality = ('old', 'new', 'mythic')
    shops = (('iron sword', 'wooden hummer', 'shovel', 'dirk', 'cooking knife', 'giant axe'),('leather pants','cloth coat','plate armor','chainmail helmet','leather gloves','steel boots'))
    shoplvl = randint (1,3)
    shopqualities = shopquality [shoplvl - 1]
    shopefficiency = round(((randint (1,5) * shoplvl) + 1 ) / 1.5)
    shopcost = (randint (1,8) * shoplvl)
    if randint(1,4) == 1:
        shop = choice(shops[1])
        checking = True
    else:
        shop = choice(shops[0])
        checking = False
    armour = 5
    if HP <=10: print ('1) Improve your armour (increases your [green]HP by 1[/]) - [yellow]{} coins[/]'.format(armour))
    elif HP <= 13: print ('1) Improve your armour (increases your [green]HP by 2[/]) - [yellow]{} coins[/]'.format(armour))
    elif HP <= 15: print ('1) Improve your armour (increases your [green]HP by 3[/]) - [yellow]{} coins[/]'.format(armour))
    elif HP <= 20: print ('1) Improve your armour (increases your [green]HP by 4[/]) - [yellow]{} coins[/]'.format(armour))
    elif HP >= 20: print ('1) Improve your armour (increases your [green]HP by 5[/]) - [yellow]{} coins[/]'.format(armour))
    if checking: print ('2)', shopqualities, shop,'with [green]armour of {0}[/] for [yellow]{1} coins[/]'.format(shopefficiency, shopcost))
    else: print ('2)', shopqualities, shop,'with [red]damage of {0}[/] for [yellow]{1} coins[/]'.format(shopefficiency, shopcost))
    print ('3) Read the monster manuscript.')
    print ('4) Leave')
    
    window_tavern.destroy()
    window_shop = Tk()
    window_shop.eval('tk::PlaceWindow . center')
    window_shop.title('Mini-RPG Text Game')
    window_shop.geometry('390x300')
    window_shop.protocol('WM_DELETE_WINDOW', on_closing_shop)
    if HP <=10: tt1 = '1) Improve your armour (increases your HP by 1) - 5 coins'
    elif HP <= 13: tt1 = '1) Improve your armour (increases your HP by 2) - 5 coins'
    elif HP <= 15: tt1 ='1) Improve your armour (increases your HP by 3) - 5 coins'
    elif HP <= 20: tt1 ='1) Improve your armour (increases your HP by 4) - 5 coins'
    elif HP >= 20: tt1 ='1) Improve your armour (increases your HP by 5) - 5 coins'
    if checking: tt2 = ('2)', shopqualities, shop,'with armour of', shopefficiency, '-', shopcost,'coins')
    else: tt2 = ('2)', shopqualities, shop,'with damage of', shopefficiency, '-', shopcost,'coins')
    
    tt3 = '3) Read the monster manuscript'
    tt4 = '4) Leave'
    lbl1 = Label(window_shop, text = tt1)
    lbl1.grid(column = 0, row = 0)
    lbl2 = Label(window_shop, text = tt2)
    lbl2.grid(column = 0, row = 1)
    lbl3 = Label(window_shop, text = tt3)
    lbl3.grid(column = 0, row = 2)
    lbl4 = Label(window_shop, text = tt4)
    lbl4.grid(column = 0, row = 3)
    
    b0 = Button(window_shop, text = '1', command = button_shop0)
    b0.place (x= 140, y = 250) 
    b1 = Button(window_shop, text = '2', command = button_shop1)
    b1.place (x= 180, y = 250)
    b2 = Button(window_shop, text = '3', command = button_shop2)
    b2.place (x = 220, y = 250)
    b3 = Button(window_shop, text = '4', command = window_shop.destroy)
    b3.place (x = 260, y = 250)

def button_tavern1():
    global window_tavern
    window_tavern.destroy()
    
def button_fight0():
    global HP
    global monsterHP
    global DMG
    global monsterDMG
    global monsterlvl
    global money
    global HPbattle
    global loot
    monsterHP -= DMG
    print ('You hit a monster for [red]{0}[/] and it has [green]{1} hp[/] left'.format(DMG, monsterHP))
    if monsterHP > 0:
        HP -= monsterDMG
        print ('Monster [red]hit you for {0}[/] and you have [green]{1} hp[/] left'.format(monsterDMG, HP))
    if monsterHP <= 0:
        money += loot
        HP = HPbattle
        print ('You have defeated this monster. After looting it you found [yellow]{} coins[/]'.format(loot))
        printstate()
        window_fight.destroy()
    if HP <= 0:
        window_fight.destroy()

def button_fight1():
    global HP
    global window_fight
    if randint(1,5) == 1:
        HP = 0
        print ('The monster cought up with you and killed you. Unfortunately you could not survive')
        window_fight.destroy()
    else:
        print ('You managed to run away. Congratulations my fast legs friend! :)')
        window_fight.destroy()
    
def button_death0():
    window_death.destroy()
    init_game(10,5,1)
    
def button_death1():
    window_death.destroy()
    exit()
    

def stroll_window():
    global window_stroll
    print ('You are strolling in the woods. Everything is quiet and only sometimes you hear the sound of wild animals.')

    window_stroll = Tk()
    window_stroll.eval('tk::PlaceWindow . center')
    window_stroll.title('Mini-RPG Text Game')
    window_stroll.geometry('710x300')
    window_stroll.protocol('WM_DELETE_WINDOW', on_closing_stroll)
    lbl = Label(window_stroll, text = ('You are strolling in the woods. Everything is quiet and only sometimes you hear the sound of wild animals.'))
    lbl.grid(column = 0, row = 0)
    b0 = Button(window_stroll, text = 'Go next', command = button_walking_next)
    b0.place (x= 315, y = 250)
    window_stroll.mainloop()
    
def tavern_window():
    global window_tavern
    global HP
    global money
    global DMG
    global HPlst
    print ('You hear the sound of people laughing and singing songs. You went to watch what is the reason for those noises and saw a [blue]tavern[/].')
    
    window_tavern = Tk()
    window_tavern.eval('tk::PlaceWindow . center')
    window_tavern.title('Mini-RPG Text Game')
    window_tavern.geometry('865x300')
    window_tavern.protocol('WM_DELETE_WINDOW', on_closing_tavern)
    lbl = Label(window_tavern, text = ('You hear the sound of people laughing and singing songs. You went to watch what is the reason for those noises and saw a tavern.'))
    lbl.grid(column = 0, row = 0)
    b0 = Button(window_tavern, text = 'Enter', command = button_tavern0)
    b0.place (x= 330, y = 250) 
    b1 = Button(window_tavern, text = 'Ignore', command = button_tavern1)
    b1.place (x= 430, y = 250)
    window_tavern.mainloop()
        
    
def purchase(cost):
    global HP
    global money
    global DMG
        
        
    if money >= cost:
        money -= cost
        return True
    print ('You do not have enough [yellow]coins[/] for that. Come back later when you get more money!')
    return False
   
    
def fight_window():
    global window_fight
    global HP
    global money
    global DMG
    global HPlst
    global monsterHP
    global monsterDMG
    global monsterlvl
    global HPbattle
    global loot
    monsterlvl = randint(1,3)
    monsters = ("Pig Bull", "Lizard archer", "Hedgefrog", "Purple Dragon")
    if HP < 25 or DMG < 10:
        monsterchance = randint (1,46)
    elif HP >= 25 and DMG >= 10:
        monsterchance = randint (1,50)
    if monsterchance >= 1 and monsterchance <= 20:
        monster = monsters [0]
        monsterHP = monsterlvl
        monsterDMG = monsterlvl + 1
        loot = randint (0,1) + monsterlvl
    elif monsterchance >= 21 and monsterchance <= 35:
        monster = monsters [1]
        monsterHP = monsterlvl
        monsterDMG = monsterlvl * 2
        loot = randint (3,5) + monsterlvl
    elif monsterchance >= 36 and monsterchance <= 45:
        monster = monsters [2]
        monsterHP = (monsterlvl + 1) * 3
        monsterDMG = monsterlvl
        loot = randint (5,10) + monsterlvl
    else:
        monster = monsters [3]
        monsterHP = monsterlvl * 10
        monsterDMG = monsterlvl * 10
        loot = randint (11,15) * monsterlvl
    print ('You have met a [red]{0}[/]. It has [green]{1} hp[/] and it\'s [red]damage is {2}[/]'.format(monster, monsterHP, monsterDMG))
    print ('Do you want to fight it or to try run away (failure to escape leads to death, you\'d better think twice.)')
    HPbattle = HP
    window_fight = Tk()
    window_fight.eval('tk::PlaceWindow . center')
    window_fight.title('Mini-RPG Text Game')
    window_fight.geometry('664x300')
    window_fight.protocol('WM_DELETE_WINDOW', on_closing_fight)
    lbl = Label(window_fight, text = ('You have met a', monster, 'It has', monsterHP, 'hp and it\'s damage is', monsterDMG))
    lbl2 = Label(window_fight, text = ('Do you want to fight it or to try run away (failure to escape leads to death, you\'d better think twice.)'))
    lbl.grid(column = 0, row = 0)
    lbl2.grid(column = 0, row = 1)
    b0 = Button(window_fight, text = 'Fight', command = button_fight0)
    b0.place (x= 170, y = 250) 
    b1 = Button(window_fight, text = 'Run', command = button_fight1)
    b1.place (x= 430, y = 250)
    window_fight.mainloop()


 
def game_loop():
    situation = randint(0,5)
    
    if situation == 0:
        tavern_window()
    elif situation == 2:
        fight_window()
    else:
        stroll_window()




init_game(10,5,1)




while True:
    if HP <= 0:
        window_death = Tk()
        window_death.eval('tk::PlaceWindow . center')
        window_death.title('Mini-RPG Text Game')
        window_death.geometry('470x300')
        window_death.protocol('WM_DELETE_WINDOW', on_closing_death)
        lbl = Label(window_death, text = ('Unfortunately you could not survive. Do you want to restart the game?'))
        lbl.grid(column = 0, row = 0)
        b0 = Button(window_death, text = 'Yes', command = button_death0)
        b0.place (x= 100, y = 250) 
        b1 = Button(window_death, text = 'No', command = button_death1)
        b1.place (x= 325, y = 250)
    
        window_death.mainloop()
           
    game_loop()
       
       