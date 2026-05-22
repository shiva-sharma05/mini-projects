print('--------------WELCOME TO QUIZ GAME----------------')

mm = 0


print('1. first ruler of khilzi dynasty \n a) allaudin khilzi  \n b) niladhvaj khen \n c) jalal-ud-din khilzin \n d) shihab-ud-bin omar')
ans1 = input("ENTER YOUR OPTION :- ")
if ans1.lower() == "a":
    print("wrong answer")
elif ans1.lower() == 'b':
    print("right answer")  
    mm = mm+10
elif ans1.lower() == "c":
    print("wrong answer") 
elif ans1.lower() == "d":
    print("wrong answer") 
else:
    print('invalid choice')

print("2. which country had second largest population after 2025? \n a) USA \n b) india \n c) chaina \n d) brazil ")
ans2 = input("ENTER YOUR OPTION :- ")
if ans2.lower() == "a":
    print("wrong answer")
elif ans2.lower() == 'c':
    print("right answer")  
    mm = mm+10
elif ans2.lower() == "b":
    print("wrong answer") 
elif ans2.lower() == "d":
    print("wrong answer") 
else:
    print('invalid choice') 

print("3. capital of nepal is \n a) lalitpur \n b) bhaktapur \n c) lumbini \n d) kathmandu")  
ans3 = input("ENTER YOUR OPTION :- ")
if ans3.lower() == "a":
    print("wrong answer")
elif ans3.lower() == 'd':
    print("right answer")  
    mm = mm+10
elif ans3.lower() == "c":
    print("wrong answer") 
elif ans3.lower() == "b":
    print("wrong answer") 
else:
    print('invalid choice')   

print('4. who is the father of mughal emperor jahangir ? \n a) babar \n b) akbar \n c) humayun \n d) aurangjeb ') 
ans4 = input("ENTER YOUR OPTION :- ")
if ans4.lower() == "a":
    print("wrong answer")
elif ans4.lower() == 'b':
    print("right answer")  
    mm = mm+10
elif ans4.lower() == "c":
    print("wrong answer") 
elif ans4.lower() == "d":
    print("wrong answer") 
else:
    print('invalid choice')

print('Who created Python? \n a) Dennis Ritchie \n b) James Gosling \n c) Guido van Rossum \n d) Elon Musk')
ans5 = input("ENTER YOUR OPTION :- ")
if ans5.lower() == "a":
    print("wrong answer")
elif ans5.lower() == 'c':
    print("right answer")  
    mm = mm+10
elif ans5.lower() == "b":
    print("wrong answer") 
elif ans5.lower() == "d":
    print("wrong answer") 
else:
    print('invalid choice')

print(f'You score {mm} out of 50')

