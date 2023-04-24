#* game the numbers 
#todo(modulse)
import random #!random module

#todo:try and except
try:
    #todo:var
    score = 0
    wHile = 2
    #todo:while loop 
    while True:
        chose = int(input('enter a number from 1 to 7')) #! chose the player 
        rand_chose = random.randrange(1,8)
        if chose < rand_chose:
            print('The number you chose is smaller than the computer selected')
            wHile -= 1
            if wHile == 0 : #! lose the player
                print('you lose!')
        elif chose > rand_chose:
            print('The number you chose is greater than the computer selected')
            wHile -= 1
            if wHile == 0 : #! lose the player
                print('you lose!')
        else :
            print('you win!') #! win the player
            score += 1
            wHile += 2
except:
    print('err')
    chose = int(input('enter a number from 1 to 7')) #! chose the player