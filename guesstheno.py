import random
print('--------------- WELCOME TO NUMBER GUESSING GAME ----------------')
print('YOU HAVE 5 TRIES TO GUESS THE NUMBER AND NUMBER IS BETWEEN 1 TO 20')

tries = 0
computer = random.randint(1,20)
for i in range(1,6,1):
    user = int(input('ENTER YOUR NUMBER :- '))
    if user > computer:
        print('YOU ARE GUESSING HIGH')
        tries = tries+1
    elif user < computer:
        print('YOU ARE GUESSING LOW')
        tries = tries+1
    else:
        print('YOU WON YOU GUESS THE NUMBER')   
        print(f'YOU GUESS THE NUMBER IN {tries} try') 
        break
else:
    print('COMPUTER WINS YOU LOSE THE GAME ')
    print(f'NUMBER IS NUM {computer}')

    

    
