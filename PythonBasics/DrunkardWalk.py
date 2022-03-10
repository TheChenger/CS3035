import random

n = int(input('How many intersections did the Drunkard walk? '))
# the variables x and y are supposed to represent a coordinate plane so x is the horizontal axis, y is verticle
#1 = forward 2 = backward 3 = left 4 = right
# 1 = y + 1  2 = y - 1  3 = x - 1  4 = x + 1

x = 0
y = 0

while n > 0:
    direction = random.randint(1,4)
    if direction == 1:
        y = y + 1
        n -= 1
        print('The Drunkard went forward')
        print('The Drunkard is now at intersection (' ,x,',',y,')')
    elif direction == 2:
        y = y - 1
        n -= 1
        print('The Drunkard went backward')
        print('The Drunkard is now at intersection (', x, ',', y, ')')
    elif direction == 3:
        x = x - 1
        n -= 1
        print('The Drunkard went left')
        print('The Drunkard is now at intersection (', x, ',', y, ')')
    elif direction == 4:
        x = x + 1
        n -= 1
        print('The Drunkard went right')
        print('The Drunkard is now at intersection (', x, ',', y, ')')

print('The end coordinates of the Drunkard are (',x,',',y,')')