import re

def display_inventory (dic):
    print ('Total number of items:', (sum(dic.values())))
    
    
def add_to_inventory (inventory, added_items):
    for i in added_items:
        inventory[i] = inventory.get(i, 0) + 1
        
def print_items(inv):
    for k,v in inv.items():
        print (k, v)
        

def invent_from_players (file):
    try:
        hfile = open (file)
    except:
        print ('Error. There is no such file.')
        
    else:
        for line in hfile:
            line = line.strip()
            x = re.split(': |, | \s', line)
            #print (x)
            items = list()
            values = list()
            for i in x[::2]:
                items.append(i)
            for i in x[1::2]:
                values.append(i)
            #print (items)
            #print (values)
            count = 0
            lst = []
            for j in range(len(items)):
                for i in items:
                    lst.append ({})
                    lst [j][i] = int(values[count])
                count += 1
            print (lst)
        

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

display_inventory (inventory)

lst = ['knife', 'rope']

add_to_inventory (inventory, lst)

print_items(inventory)      
            
invent_from_players ('inven.txt')
