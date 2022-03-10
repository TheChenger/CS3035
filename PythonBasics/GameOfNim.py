import random

marbles = random.randint(10,100)
#marbles = 1
firstTurn = random.randint(0,1)   #0 is human, 1 is computer
#firstTurn = 0
mode = random.randint(0,1)   #0 is stupid, 1 is smart
removeMarbles = 0

print("Marbles " ,marbles)
print("First Turn ", firstTurn)
print("Mode " , mode)
print("Remove Marbles " , removeMarbles)

while mode == 0:
    while marbles >= 1:
        while firstTurn == 0:
            if marbles == 1:
                print("You lose! You are left with the last marble")
                exit()
            else:
                removeMarbles = int(input('Enter an amount of marbles to take away from the pile '))


            if removeMarbles > marbles/2:
                takeAway = int(input('That is too many, enter a number between 2 and half the marbles left'))

            marbles = marbles - removeMarbles
            print('You chose to take away ', removeMarbles , 'from the pile')
            print('There are ', marbles, ' left in the pile')
            firstTurn += 1

        while firstTurn == 1:
            if marbles == 1:
                print("You win! The CPU was left with the last marble")
                exit()
            else:
                halfMarbles =  int(marbles / 2)
                removeMarbles = random.randint(1, halfMarbles)
            marbles = marbles - removeMarbles
            print('The CPU chose to take away ', removeMarbles, 'from the pile')
            print("There are " , marbles , " left")
            firstTurn -= 1
while mode == 1:
    while marbles >= 1:
        while firstTurn == 0:
            if marbles == 1:
                print("You lose! You are left with the last marble")
                exit()
            else:
                removeMarbles = int(input('Enter an amount of marbles to take away from the pile '))

            if removeMarbles > marbles / 2:
                takeAway = int(input('That is too many, enter a number between 2 and half the marbles left'))

            marbles = marbles - removeMarbles
            print('You chose to take away ', removeMarbles, 'from the pile')
            print('There are ', marbles, ' left in the pile')
            firstTurn += 1

        while firstTurn == 1:
            if marbles == 1:
                print("You win! The CPU was left with the last marble")
                exit()

            elif marbles >= 64:
                removeMarbles = marbles - 63
                marbles = marbles - removeMarbles

            elif marbles == 63:
                halfMarbles = int(marbles / 2)
                removeMarbles = random.randint(1, halfMarbles)
                marbles = marbles - removeMarbles

            elif marbles >= 32 and marbles < 63:
                removeMarbles = marbles - 31
                marbles = marbles - removeMarbles

            elif marbles == 31:
                halfMarbles = int(marbles / 2)
                removeMarbles = random.randint(1, halfMarbles)
                marbles = marbles - removeMarbles

            elif marbles >= 16 and marbles < 31:
                removeMarbles = marbles - 15
                marbles = marbles - removeMarbles

            elif marbles == 15:
                halfMarbles = int(marbles / 2)
                removeMarbles = random.randint(1, halfMarbles)
                marbles = marbles - removeMarbles

            elif marbles >= 8 and marbles < 15:
                removeMarbles = marbles - 7
                marbles = marbles - removeMarbles

            elif marbles == 7:
                halfMarbles = int(marbles / 2)
                removeMarbles = random.randint(1, halfMarbles)
                marbles = marbles - removeMarbles

            elif marbles >= 4 and marbles < 7:
                removeMarbles = marbles - 3
                marbles = marbles - removeMarbles

            elif marbles <= 3:
                marbles = marbles - 1

            print('The CPU chose to take away ', removeMarbles, 'from the pile')
            print("There are ", marbles, " left")
            firstTurn -= 1