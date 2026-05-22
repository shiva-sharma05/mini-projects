import random

print('WELCOME TO DICE ROLLING GAME')

def roll_dice():
    dice = random.randint(1,6)
    print(dice)

while True:
    print('PRESS 1 FOR ROLL THE DICE')
    print('PRESS 0 FOR EXIT')
    option = int(input('ENTER YOUR option :- '))
    if option == 1:
        roll_dice()
    elif option == 0:
        print('THANKS FOR PALYING ')
        break    
    else:
      print('ERROR : INVALID INPUT')