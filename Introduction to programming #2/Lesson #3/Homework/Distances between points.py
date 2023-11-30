from math import sqrt

def coordinates (point_name):
    pn = (int (input ('Please enter point {} x coordinate: '.format(point_name.upper()))), int (input('Please enter point {} y coordinate: '.format(point_name.upper()))))
    return pn

def distance (m, n):
    d = sqrt((n[0]-m[0])**2 + (n[1]-m[1])**2) #round(sqrt((n[0]-m[0])**2 + (n[1]-m[1])**2)) if we want result to be more elegant
    return d
    
a = coordinates ('a')
b = coordinates ('b')
c = coordinates ('b')

lst = [(distance (a, b), 'A', 'B'), (distance (b, c), 'B', 'C'), (distance (a, c), 'A', 'C')]
lst.sort()
print ('Points {0} and {1} are the closest to each other.'.format(lst[0][1], lst[0][2]))


# Of course this task could be done by using if cases but this one was more elegant
# Morover I think it uses less memory so I have used this one