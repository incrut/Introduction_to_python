def child_height(mom, dad, child):
    if child == 'M':
        child_h = (dad + mom + 13) / 2
    else:
        child_h = (dad + mom - 13) / 2
    
    return child_h

parents = [(163, 175, 'F'), (170, 180, 'M'), (153, 184, 'M'), (177, 182, 'F')]

sum_heights = 0

for el in parents:
    height = child_height(el[0], el[1], el[2])
    print ('Child\'s height is', height, 'cm.')
    
    sum_heights += height

average = sum_heights / len(parents)

print ('An average height of the children is',average, 'cm.')